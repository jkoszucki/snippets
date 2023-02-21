from subprocess import run
from pathlib import Path

def wrap_command(cmd, envname='base'):
    cmd = f'conda run -n {envname} {cmd}'
    return cmd


def get_clinker_cmd(prophageIDs, output, gene_functions=False):
    """ to add gene functions to scipt provide path to the file with groups """

    # list2string
    prophageIDs = ' '.join(prophageIDs)

    # get command
    cmd = f'clinker {prophageIDs} -p "{output}"'
    if gene_functions: cmd = cmd + f' -gf "{gene_functions}"'

    # add environment
    cmd = wrap_command(cmd, envname='clinker')
    return cmd


def get_easyfig_cmd(prophageIDs, output, leg_name='PC', easyfig_py='/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/code/scripts/Easyfig.py'):
    """ ... """

    # list2string
    prophageIDs = ' '.join(prophageIDs)

    # get command
    cmd = f'python2 "{easyfig_py}" -f1 T -o "{output}" -i 60 -leg_name {leg_name} -legend double -width 6000 {prophageIDs}'
    # add environment
    cmd = wrap_command(cmd, envname='easyfig')

    return cmd



print('Script runs clinker and easyfig for indicated prophage identifiers.')
print('Provide prophage file names (identifiers) for visualization: ')

# paths
prophageIDs = input().split()

genbank_dir = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/MCB_CLOUD/ANALYSIS/PROPHAGES-KPH-KBV_2023-02_5KB_EXTENDED/PROPHAGES-KPH-KBV_2023-02_5KB_EXTENDED/3_ANNOTATION_IDENT50_COV80/3_GENBANK')
working_dir = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/WORKING-DIR')
# gene_functions = Path('/Users/januszkoszucki/MGG Dropbox/Janusz Koszucki/data/DATABASES/ANNOTATION_IDENT30_COV80-KPH-KBVP1/gf-KPH-KBVP1.csv')

clinker_output = Path(working_dir, 'clinker.html')
easyfig_output = Path(working_dir, 'easyfig.png')

# create directories
Path(working_dir).mkdir(exist_ok=True, parents=True)

# fnames2paths (escape whitecharacters)
prophageIDs = ['"' + str(Path(genbank_dir, f'{id}.gb')) + '"' for id in prophageIDs]

# get commands
easyfig = get_easyfig_cmd(prophageIDs, easyfig_output, leg_name='PC')
clinker = get_clinker_cmd(prophageIDs, clinker_output)
# clinker = get_clinker_cmd(prophageIDs, clinker_output, gene_functions=gene_functions)

# print commands
print(easyfig)
print('\n')
print(clinker)

# run
run(easyfig, shell=True)
run(clinker, shell=True)
