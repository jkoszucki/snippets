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
                cats.append(qualifiers['PC'][0])
            except:
                print('Error in qualifiers!!!!')
                print(qualifiers)
    return proteinIDs, cats


genbanks = list(Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/DATABASES/ANNOTATION_IDENT30_COV80-KPH-KBVP1/3_PROPAHGES_GENBANK').glob('*.gb'))
gene_functions_csv = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/DATABASES/ANNOTATION_IDENT30_COV80-KPH-KBVP1/gf-KPH-KBVP1.csv')

records = []
for genbank in genbanks:
    records.append(list(SeqIO.parse(genbank, 'genbank')))

records = list(itertools.chain(*records))
proteinIDs, cats = frame(records)

df = pd.DataFrame({'proteinID': proteinIDs, 'category': cats})
df.to_csv(gene_functions_csv, header=False, index=False)
