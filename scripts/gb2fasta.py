""" Convert prophage genbank files [input_dir] to fasta files [output_dir] """

from pathlib import Path
from Bio import SeqIO

input_dir = '/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/WORKING-DIR/2_PROPHAGE_VISUALIZATION/tmp'
output_dir = '/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/WORKING-DIR/2_PROPHAGE_VISUALIZATION/tmp/fasta'
extension = 'gb'

print('Convert genbank files to fasta files. Only first contig taken from the genbank file.')

# create out folder
Path(output_dir).mkdir(exist_ok=True, parents=True)

paths = list(Path(input_dir).glob(f'*{extension}'))
rs = [list(SeqIO.parse(p, 'genbank'))[0] for p in paths]


for r in rs:
	fname = r.id.split('||')[1]
	outpath = Path(output_dir, f'{fname}.fasta')
	SeqIO.write(r, outpath, 'fasta')