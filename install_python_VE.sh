# AMI
#Deep Learning Base AMI (Ubuntu 18.04) Version 21.0 (ami-0b98d7f73c7d1bb71)

# Basic Install
sudo apt -y update 
sudo apt -y upgrade
sudo apt install -y curl wget tree
sudo apt install -y build-essential checkinstall libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev zlib1g-dev openssl libffi-dev python3-dev python3-setuptools 
# Locale 셋팅
x=$(cat ~/.bashrc|grep LC_ALL)
if [ ${#x} -eq 0 ]; then
    cd
    cat <<EOF>> ~/.bashrc
export LC_ALL="en_US.UTF-8"
EOF
    . ~/.bashrc
fi

# # Python Install
# export pythonVersionFull=2.17.15
# export pythonVersion=${pythonVersionFull:0:3}
# x=$(which python$pythonVersion)
# if [ ${#x} -eq 0 ];then 
#     wget https://www.python.org/ftp/python/$pythonVersionFull/Python-$pythonVersionFull.tar.xz
#     tar xvf Python-$pythonVersionFull.tar.xz
#     cd Python-$pythonVersionFull
#     ./configure
#     sudo make altinstall
#     cd
#     sudo rm -rf Python-$pythonVersionFull
#     sudo rm -rf Python-$pythonVersionFull.tar.xz
#     sudo update-alternatives --install /usr/bin/python python /usr/local/bin/python3.7 3
#     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
#     sudo python get-pip.py
#     rm get-pip.py
#     # sudo rm -f /usr/bin/python3
#     sudo ln -s $(which python$pythonVersion) /usr/bin/python3

# fi

# Pip install 
sudo pip3 install jupyter

# Python Virtual Env 설치 
sudo apt install -y python-virtualenv
sudo pip3 install virtualenvwrapper
x=$(cat ~/.bashrc|grep VIRTUALENVWRAPPER_PYTHON)
if [ ${#x} -eq 0 ]; then
    sudo apt install python-virtualenv
    sudo pip3 install virtualenvwrapper

    cat <<EOF>> ~/.bashrc
VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=~/.virtualenvs
. /usr/local/bin/virtualenvwrapper.sh
EOF
    . ~/.bashrc
fi

# Python Virtual Env Setting
x=$(workon)
if [ ${#x} -eq 0 ]; then
    mkvirtualenv --python=/usr/bin/python3 p3 
fi

workon p3
pip3 install jupyter
python -m ipykernel install --user --name=p3
pip3 install tensorflow-gpu==1.15
pip3 install pylab
pip3 install opencv-python
pip3 install matplotlib

# for Example
wget https://raw.githubusercontent.com/Finfra/TensorflowStudyExample/master/s1.12/2.keras_jupyter/CNN/CNN.ipynb


# Cuda Env Setting
x=$(cat ~/.bashrc|grep LD_LIBRARY_PATH)
if [ ${#x} -eq 0 ];then 
    echo "export PATH=/usr/local/cuda/bin:\$PATH" >>~/.bashrc
    echo "export LD_LIBRARY_PATH=\"\$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64\"" >>~/.bashrc
    echo "export CUDA_HOME=/usr/local/cuda">>~/.bashrc
fi

# cuDNN install
cd
#wget http://j.finfra.com/_file/cudnn-10.0-linux-x64-v7.6.5.32.tar
wget https://nowagefs3.s3.amazonaws.com/cudnn/cudnn-10.0-linux-x64-v7.6.5.32.tar
tar xf cudnn-10.0-linux-x64-v7.6.5.32.tar
sudo mv cuda/include/* /usr/local/cuda/include/
sudo mv cuda/lib64/* /usr/local/cuda/lib64/
rm -rf cuda
echo "Do reboot Command"
