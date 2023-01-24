import pandas as pd
from pathlib import Path

PC = 'PC02712'
KL = 'KL24'

table = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/DATABASES/ANNOTATION_IDENT30_COV80-KPH-KBVP1/main_IDENT30_COV80.tsv')
output_dir = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/WORKING-DIR/PROPHAGE_VISUALIZATION/')

# load
main_df = pd.read_csv(table, sep='\t')


# how many genomes having this capsule
temp_df = main_df[['genomeID', 'KL']]
temp_df.drop_duplicates('genomeID', inplace=True)

print(temp_df.loc[(temp_df['KL'] == KL)].head())
ngenomes = temp_df.loc[(temp_df['KL'] == KL)].shape[0]

print(f'{KL} is present in {ngenomes} genomes')

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
prophageID = ' '.join(prophageID)

print(f'All phages sharing {PC}:')
print(prophageID)

# only KL specific phages
filt_kl = (main_df['KL'] == KL)
prophageID = main_df.loc[filt_kl, 'prophageID'].to_list()
prophageID = ' '.join(prophageID)

print(f'Only {KL} phages:')
print(prophageID)
