import pandas as pd
from pathlib import Path

PC = 'PC01174'
KL = 'KL2'

table = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/working_dir/DATA/KASPAH_KLEBPAVIAP1/5_ANNOTATION_IDENT30_COV80/main_IDENT30_COV80.tsv')
output_dir = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/working_dir/DATA/KL2/TABLE')

# load
main_df = pd.read_csv(table, sep='\t')


# how many genomes having this capsule
# main_df = main_df[['genomeID', 'KL']]
# main_df.drop_duplicates('genomeID', inplace=True)
#
# print(main_df.head())
# print(main_df.shape)
#
# print(main_df.loc[(main_df['KL'] == 'KL2')].head())
# print(main_df.loc[(main_df['KL'] == 'KL2')].shape)

# filter
filt_pc = (main_df['PC'] == PC)
filt_kl = (main_df['KL'] == KL)

# extract & get command
main_df = main_df.loc[filt_pc, ['PC', 'prophageID', 'KL', 'ST', 'PHROG', 'PFAM', 'PHROG_function']]

# all phages sharing PC
prophageID = main_df.loc[filt_pc, 'prophageID'].to_list()

# prompt
print(f'{len(prophageID)} prophages found in the {KL} that share {PC}')
main_df.to_csv(Path(output_dir, PC + '.tsv'), sep='\t', index=False)

prophageID = [pp + '.gb' for pp in prophageID]
prophageID = ' '.join(prophageID)

print(f'All phages sharing {PC}:')
print(f'clinker {prophageID} -p {PC}.html\n')


# only KL specific phages
filt_kl = (main_df['KL'] == KL)
prophageID = main_df.loc[filt_kl, 'prophageID'].to_list()
prophageID = [pp + '.gb' for pp in prophageID]
prophageID = ' '.join(prophageID)

print(f'Only {KL} phages:')
print(f'clinker {prophageID} -p {PC}.html\n')
