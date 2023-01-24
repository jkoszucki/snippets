from pathlib import Path
from Bio import SeqIO

raw = Path('/Users/januszkoszucki/genomes/genomes/raw')
output_dir = Path('/Users/januszkoszucki/genomes/genomes/processed')
files = list(Path(raw).glob('*.fasta'))

for fasta in files:
    print(fasta)
    stem = Path(fasta).stem.replace('.', '_')
    outputfile = Path(output_dir, f'{stem}.fasta')

    r = list(SeqIO.parse(fasta, 'fasta'))[0]
    prophageID = r.id.replace('.', '_')

    r.name = ''
    r.description = ''
    r.id = ''

    r.id = prophageID
    print(r)
    SeqIO.write(r, outputfile, 'fasta')
