---
layout: post
category: "linux"
title:  "linux安装python"
header-img: "img/in-post/post-bg-unix-linux.jpg"
tags:
    - linux
---


**linux 下安装 python 环境(未完成）
**
<pre><code>
首先python 官网下载 python 包（tgz文件）
mkdir  /usr/local/python3   新建文件夹
tar -xvzf  Python-3.7.1.tgz   解压文件
cd Python-3.7.1/              进入目录
./configure --prefix=/usr/local/python3 /usr/bin/python3   编译安装
make
make install
ln -s /usr/local/python3/bin/python3 /usr/bin/python3   建立python 软链接
执行下面两个命令，把path添加进去
vim ~/.bash_profile
.bash_profile


# Get the aliases and functions
if [ -f ~/.bashrc ]; then
. ~/.bashrc
fi
# User specific environment and startup programs
PATH=$PATH:$HOME/bin:/usr/local/python3/bin
export PATH

wq！保存退出
安装pip需要前置安装setuptools
wget --no-check-certificate  https://pypi.python.org/packages/source/s/setuptools/setuptools-19.6.tar.gz#md5=c607dd118eae682c44ed146367a17e26
tar -zxvf setuptools-19.6.tar.gz
cd setuptools-19.6
python3 setup.py build
python3 setup.py install

</code></pre>

<pre><code>
pip3 install -r  /app/requirements.txt
sudo pip3 uninstall certifi
sudo pip3 install certifi==2015.11.20
pip3 install --upgrade distribute
</code></pre>