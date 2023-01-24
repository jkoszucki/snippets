import pandas as pd
from subprocess import run
from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.SeqRecord import SeqRecord

print('Script requires: mmseqs pandas subprocess pathlib biopython clustalo')
print('Create env with:\nconda create -n mmseqs -c conda-forge -c bioconda pandas subprocess pathlib biopython clustalo')
print('Runing mmseqs2 search!\n')

def wrap_command(cmd, envname='mmseqs'):
    cmd = f'conda run -n {envname} {cmd}'
    return cmd


def msa(stem, indir, outdir, format='fasta', threads=8):
    """
    stem = 'prot1'
    """

    infile = Path(indir, f'{stem}.fasta')
    outfile = Path(outdir, f'{stem}.fasta')

    cmd = f'clustalo --in="{infile}" --out="{outfile}" --force --outfmt={format} --wrap=60'
    return cmd


                    ############################
                    ########## SEARCH ##########
                    ############################

# paths
query = '/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/WORKING-DIR/DRULIS-KAWA/4_BASIA_SEQ_IN_LYTIC_RBPS/REAL_ID.fasta'
target = '/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/WORKING-DIR/DRULIS-KAWA/4_BASIA_SEQ_IN_LYTIC_RBPS/LYTIC_RBPs.fasta'
working_dir = '/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/WORKING-DIR/DRULIS-KAWA/4_BASIA_SEQ_IN_LYTIC_RBPS'

working_dir = str(Path(working_dir))

# params
SENSITIVITY = 8.5
threads = 8
verbose = False
pidet, qcov, tcov, eval = 30, 0.3, 0, 10**-3


# create mmseqs databases
search_dir = Path(working_dir, '1_SEARCH')
querydb_dir = Path(search_dir, 'MMSEQSDB-QUERY')
targetdb_dir = Path(search_dir, 'MMSEQSDB-TARGET')
results_dir = Path(search_dir, 'RESULTS')

# create directories
Path(querydb_dir).mkdir(exist_ok=True, parents=True)
Path(targetdb_dir).mkdir(exist_ok=True, parents=True)
Path(results_dir).mkdir(exist_ok=True, parents=True)

querydb = f'mmseqs createdb "{query}" "{querydb_dir}/MMSEQSDB-QUERY"'
targetdb = f'mmseqs createdb "{target}" "{targetdb_dir}/MMSEQSDB-TARGET"'
search = f'mmseqs search "{querydb_dir}/MMSEQSDB-QUERY" "{targetdb_dir}/MMSEQSDB-TARGET" "{results_dir}/RESULTS" "{working_dir}/TMP" -s {str(SENSITIVITY)}'
results = f'mmseqs convertalis "{querydb_dir}/MMSEQSDB-QUERY" "{targetdb_dir}/MMSEQSDB-TARGET" "{results_dir}/RESULTS" "{search_dir}/raw_results.tsv" --format-output "query,target,pident,evalue,bits,qcov,tcov,qstart,qend,qlen,tstart,tend,tlen,qseq,tseq"'

# wrap all commands
querydb, targetdb, search, results = list(map(wrap_command, [querydb, targetdb, search, results]))

# search
print('Create mmseqs databases... ', end = '')
if verbose: print('\n' + querydb)
if verbose: print('\n' + targetdb)

run(querydb, shell=True, capture_output=True)
run(targetdb, shell=True, capture_output=True)
print('Done!')

print('Run search... ', end = '')
if verbose: print('\n' + search)
run(search, shell=True, capture_output=True)
print('Done!')

print('Convert results... ', end='')
if verbose: print('\n' + results)
run(results, shell=True, capture_output=True)
print('Done!')

# load
# mmseqs_search_default_cols = ['query', 'target', 'bitscore', 'ident', 'eval', 'qstart', 'qend', 'qlen', 'tstart', 'tend', 'tlen']
cols = ['query','target','pident','eval','bits','qcov','tcov','qstart','qend','qlen','tstart','tend','tlen','qseq','tseq']

results_df = pd.read_csv(f"{working_dir}/1_SEARCH/raw_results.tsv", sep='\t', header=None)
results_df.columns = cols

filt_ident = (results_df['pident'] >= pident)
filt_cov = (results_df['qcov'] >= qcov) & (results_df['tcov'] >= tcov)
filt_eval = (results_df['eval'] <= eval)

results_df = results_df.loc[filt_ident & filt_cov & filt_eval]
results_df.to_csv(f"{search_dir}/results.tsv", sep='\t', index=False)


                    #########################
                    ####### ALIGNMENT #######
                    #########################
# paths & params
alignment_dir = Path(working_dir, '2_ALIGNMENTS')
fasta_dir = Path(alignment_dir, '1_FASTA_PER_QUERY')
msa_dir = Path(alignment_dir, '2_MSA_PER_QUERY')

# create directories
Path(alignment_dir).mkdir(exist_ok=True, parents=True)
Path(fasta_dir).mkdir(exist_ok=True, parents=True)
Path(msa_dir).mkdir(exist_ok=True, parents=True)

### alignment fasta for each query
print('WARNING! Self hits are not filtered.')
query_df = results_df.drop_duplicates('query')
queries = query_df['query'].to_list()
print(f'Generate MSA per query (n={len(queries)})... ')

for i, query in enumerate(queries):
    print(f'Processing {i+1} query out of {len(queries)}')
    # path
    proteins = Path(fasta_dir, f'{query}.fasta')

    # per query
    filt_query = (query_df['query'] == query)
    qseq = query_df.loc[filt_query].iloc[0]['qseq']

    filt_query = (results_df['query'] == query)
    rows_targets = list(results_df.loc[filt_query, ['target', 'tseq']].itertuples(index=False, name=None)) # targets

    # query and its hits
    rows = [(str(query), qseq)] + list(rows_targets)
    records = []
    for target, seq in rows:
        # create records
        record = SeqRecord(Seq(seq), id=target)
        record.annotations['molecule_type'] = 'Protein'
        record.name = ''
        record.description = ''
        record.organism = ''

        records.append(record)

    n = SeqIO.write(records, proteins, 'fasta')

    cmd = msa(query, fasta_dir, msa_dir, threads=threads)
    cmd = wrap_command(cmd)
    if verbose: print(cmd)
    run(cmd, shell=True, capture_output=True)

print('Done!')


print('Save command... ', end='')
commands_file = Path(working_dir, 'commands.txt')
command = '\n'.join([querydb, targetdb, search, results])
with open(commands_file, 'w+') as f:
    f.write(command)
print('Done!')
