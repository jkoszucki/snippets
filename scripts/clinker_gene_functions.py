import pandas as pd
from Bio import SeqIO
from pathlib import Path
import itertools

def frame(records):
    proteinIDs, cats = [], []
    for r in records:
        for f in r.features:
            qualifiers = f.qualifiers
            try:
                proteinIDs.append(qualifiers['proteinID'][0])
                cats.append(qualifiers['note'][0])
            except:
                print('Error in qualifiers!!!!')
                print(qualifiers)
    return proteinIDs, cats


genbanks = list(Path('/Users/januszkoszucki/tmp').glob('*.gb'))
gene_functions_csv = Path('/Users/januszkoszucki/tmp/gf.csv')

records = []
for genbank in genbanks:
    records.append(list(SeqIO.parse(genbank, 'genbank')))

records = list(itertools.chain(*records))
records = records[:2]

proteinIDs, cats = frame(records)

df = pd.DataFrame({'proteinID': proteinIDs, 'category': cats})
df.to_csv(gene_functions_csv, header=False, index=False)
