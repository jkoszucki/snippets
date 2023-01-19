"""
Generate genbank files of prophages.
"""

# modules
import pandas as pd
from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.SeqRecord import SeqRecord

# functions
def get_phrog(row):
    """ get phrog cluster """
    if 'phrog_' in row['target']:
        return int(row['target'].split('_')[-1])
    else:
        return 0


# paths
prophageIDs = ['KBV_PHAGE1521_M', 'KBV_PHAGE0492_M', 'KBV_PHAGE0490_M']
main = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/working_dir/DATA/KL2/5_EASYFIG/main_IDENT30_COV80.tsv')
phrog_annot = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/working_dir/DATA/KL2/5_EASYFIG/phrog_annot_modified.tsv')
genbank_dir = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/working_dir/DATA/KL2/5_EASYFIG/1_GENOMES')

output_dir = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/working_dir/DATA/KL2/5_EASYFIG/2_PHROGs_ANNOTATION')
output_dir.mkdir(exist_ok=True, parents=True)

# load
main_df = pd.read_csv(main, sep='\t')
phrog_annot_df = pd.read_csv(phrog_annot, sep='\t')

main_df = main_df.merge(phrog_annot_df, on='PHROG', how='left')


for prophageID in prophageIDs:

    # paths
    genbank_input = Path(genbank_dir, f'{prophageID}.gb')
    genbank_output = Path(output_dir, f'{prophageID}.gb')

    ### get prophage sequence
    prophage_seq = list(SeqIO.parse(genbank_input,'genbank'))[0].seq

    ### get prophage features
    filt_prophage = (main_df['prophageID'] == prophageID)
    pp_df = main_df.loc[filt_prophage]

    # recordID
    contigID = pp_df['contigID'].unique()[0]
    kl = pp_df['KL'].unique()[0]
    recordID = '||'.join([contigID, prophageID, kl])


    ### get features
    features = []
    for i, row in pp_df.iterrows():

        start, stop, strand = row['start'], row['stop'], row['strand']
        proteinID, protein, PHROG, PHROG_function, PFAM = row['proteinID'], row['protein'], row['PHROG'], row['PHROG_function'], row['PFAM']

        rgb, category = row['rgb'], row['category']
        pc = row['PC']

        # correct for strand
        if strand == '-': start, stop = stop, start

        f = SeqFeature(FeatureLocation(start-1, stop, strand=int(f'{strand}1')), type='CDS')
        qualifiers = {
                'PHROG_function': [PHROG_function],
                'PHROG': [PHROG],
                'PFAM': [PFAM],
                'PC': [pc],
                'proteinID': [proteinID],
                'translation': [protein],
                'note': [category],
                'colour': [rgb]
                }

        f.qualifiers = qualifiers
        features.append(f)

    ### create record
    record = SeqRecord(Seq(prophage_seq), id=recordID)
    record.annotations['molecule_type'] = 'DNA'
    record.features = features
    record.name = ''
    record.description = ''
    record.organism = ''

    SeqIO.write(record, genbank_output, 'genbank')


print('And generate easyfig figure: python2 Easyfig.py -f1 T -o easyfig.png -i 60 -leg_name note -legend double -width 6000 KBV_PHAGE049*')
