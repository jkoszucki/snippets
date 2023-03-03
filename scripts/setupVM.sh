# customize .profile | .bash_profile | .bashrc


alias ll="ls -l"
alias la="ls -la"
alias sl="ls"
alias dc="cd"
alias cc="clear"
alias vb="vim ~/.profile"
alias sb="source ~/.profile"
alias cp="cp -i"
alias db="cd ~/storage/dbmgg/databases/bacteria"
alias mybase="mamba activate mybase"
alias jkoszucki="cd ~/storage/jkoszucki"
alias vp="vim ~/.profile"
alias sp="source ~/.profile"


# mamba installation guide - https://www.youtube.com/watch?v=yeXDyF6_VwQ
echo 'Check mamba version: https://github.com/conda-forge/miniforge'
MAMBA_DIR='~/mamba'

wget https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-Linux-x86_64.sh
bash Mambaforge*.sh

# mount storage
sudo mount -t ceph 192.168.21.201:6789,192.168.21.202:6789,192.168.21.203:6789:/Projects/BINF/MostowyLab/ storage -o name=jkoszucki,secret=AQBg9fFisk4zNxAAWMvSWi98Smp2I/Z1Ijsg6A==

### ssh sublime text
sudo curl -o /usr/local/bin/rmate https://raw.githubusercontent.com/aurora/rmate/master/rmate
sudo chmod +x /usr/local/bin/rmate
sudo mv /usr/local/bin/rmate /usr/local/bin/rsubls


# ### mirror cloud
# ECF_CLOUD_PATH='/home/MCB/kszczepaniak/storage/dbmgg/project-ECF/phage-ECF-workdir-refseq-hhblits-102022'
# ECF_LOCAL_PATH='/Users/bognasmug/MGG Dropbox/Projects/ECFs/data'
# CLOUD_MACHINE='bsmug@192.168.57.107'

# # copy the structure folder
# mkdir -p "$ECF_LOCAL_PATH"
# rsync -av -f"+ */" -f"- *" "$ECF_CLOUD_PATH_COMPLETE" "$ECF_LOCAL_PATH"

# # sync input files
# INPUT_CLOUD_PATH="$ECF_CLOUD_PATH_COMPLETE/ecf-explorer/input"
# INPUT_LOCAL_PATH="$ECF_LOCAL_PATH/phage-ECF-workdir-refseq-hhblits-102022/ecf-explorer/input"
# rsync -r --progress --exclude 'all-vs-all' "$INPUT_CLOUD_PATH" "$INPUT_LOCAL_PATH"

# OUTPUT_CLOUD_PATH="$ECF_CLOUD_PATH_COMPLETE/ecf-explorer/output"
# OUTPUT_LOCAL_PATH="$ECF_LOCAL_PATH/phage-ECF-workdir-refseq-hhblits-102022/ecf-explorer/output"
# rsync -r --progress  --exclude 'ecfs-dbs' --exclude 'ecfs-final' "$OUTPUT_CLOUD_PATH" "$OUTPUT_LOCAL_PATH"


