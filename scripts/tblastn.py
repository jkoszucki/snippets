import pandas as pd
from subprocess import run
from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.SeqRecord import SeqRecord

# # functions
# def wrap_command(cmd, envname='mmseqs'):
#     cmd = f'conda run -n {envname} {cmd}'
#     return cmd
#
#
# # paths
# query = ''
# target = ''
# woring_dir = ''
#
# results_tsv = Path(working_dir, '')
# msa = Path(working_dir)




#### TBLASTN ####
# query & target are fasta files
# cmd = f'tblastn -query {query} -subject {target} -outfmt "6 qseqid sseqid pident evalue bitscore qcovs sstart send"'

# paths
working_dir = '/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/code/analysis/2_ZDK'

results_tsv = Path(working_dir, 'results.tsv')
subject = Path(working_dir, 'pgw.fasta')
msa = Path(working_dir, 'raw_msa.fasta')

cols = ['query','subject', 'pident','evalue','bitscore','qcov','sstart','send']
df = pd.read_csv(results_tsv, sep='\t')
df.columns = cols

filt_eval = (df['evalue'] <= 10**-3)
filt_pident = (df['pident'] >= 80)
filt_qcov = (df['qcov'] >= 0.3)

df = df.loc[filt_eval & filt_pident]

# extract nucleotide sequences
records = SeqIO.parse(subject, 'fasta')
hits = df['subject'].to_list()

msa_records = []
for r in records:
    if r.id in hits:
        start, end = df.loc[df['subject'] == r.id, ['sstart', 'send']].iloc[0]

        # strand
        if start <= end: seq = r.seq[start-1:end]
        else: seq = r.seq[end-1:start].reverse_complement()

        new_record = SeqRecord(Seq(seq), id=r.id)
        new_record.annotations['molecule_type'] = 'Nucleotide'
        new_record.name = ''
        new_record.description = ''
        new_record.organism = ''

        msa_records.append(new_record)

msa_records = query_record + msa_records
n = SeqIO.write(msa_records, msa, 'fasta')

print('Add query to raw_msa.fasta file!!!\n')
print('Generate MSA:')
print('clustalo --in="raw_msa_query.fasta" --out="msa.aln" --force --outfmt="fasta" --wrap=60')
