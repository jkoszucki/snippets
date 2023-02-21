# modules
import pandas as pd
from pathlib import Path

from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio.SeqRecord import SeqRecord

prophage_table = '/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/MCB_CLOUD/ANALYSIS/PROPHAGES-KPH-KBV_2023-02/0_INPUT/prophages.tsv'
output_dir = '/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/MCB_CLOUD/ANALYSIS/PROPHAGES-KPH-KBV_2023-02/0_INPUT/2_PROPHAGES'

df = pd.read_csv(prophage_table, sep='\t')

for i, row in df.iterrows():
	record = SeqRecord(Seq(str(row['seq'])), id=str(row['prophageID']))
	record.annotations['molecule_type'] = 'DNA'
	features = []
	record.name = ''
	record.description = ''
	record.organism = ''

	path = Path(output_dir, str(row['prophageID']) + '.fasta')
	SeqIO.write(record, path, 'fasta')