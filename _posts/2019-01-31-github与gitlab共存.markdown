---
layout: post
category: "git"
title:  "github与gitlab共存"
header-img: "img/in-post/post-bg-unix-linux.jpg"
tags:
    - git
---

**windows下github与gitlab共存**
个人倾向gitlab用于公司项目，github用于自己博客及demo编写
网上百度看这两者是可以共存的，今天终于把这个问题解决了
<pre><code>
第一步 生成gitlab ssh key
1、找到/c/Users/you（系统名称）/.ssh文件夹。
2、在本文件夹【右键】点击【Git Bash Here】
3、在命令行输入：ssh-keygen -t rsa -b 4096 -C "your_email@example.com"。
其中your_email@example.com是你注册gitlab的邮箱地址。回车。
4、当看到Enter a file in which to save the key (/c/Users/you/.ssh/id_rsa):时，
括号里提示的是生成ssh的默认文件名id_rsa，在这里gitlab就可以使用默认的文件名
（我自己由于原来就有了gitlab的ssh，所以我使用了默认名）。回车。
5、后面步骤就是设置密码了，连续回车即可
6、完成后就在本文件夹里看到id_rsa和id_rsa.pub两个文件，其中，id_rsa是私钥文件，id_rsa.pub是公钥文件。
7、将id_rsa.pub中的内容复制出来，并添加到gitlab 【settings】中的【SSH keys】中。

第二步 生成github ssh key
生成github ssh文件时，与生成gitlab的步骤是一样的，不同的是在：
    第3步的邮箱更改为注册github的邮箱
    第4步生成的文件名要与生成gitlab的文件名有所区分，我这里为id_rsa_github
    然后将id_rsa_github.pub中的内容复制出来添加到github 【settings】->【SSH Keys】

第三步 建立config文件
    在/c/Users/you（系统名称）/.ssh文件夹 中新建config文件
    填入信息：
<pre><code>
#gitlab
Host gitlab
        HostName 192.*.*.*（更改为本地gitlab的服务器ip地址。如果有域名的话填写域名地址）
        IdentityFile ~/.ssh/id_rsa

#github
Host github
        HostName github.com
        IdentityFile ~/.ssh/id_rsa_github
</code></pre>

运行以下命令（期间可能要你输入密码，按照提示输入密码即可
<pre><code>
ssh-add id_rsa #添加gitlab私钥
ssh-add id_rsa_github #添加github私钥
ssh-add -L #查看公钥
ssh-add -l #查看私钥
</code></pre>
测试是否配置成功
1、找到/c/Users/you（系统名称）/.ssh文件夹。
2、在本文件夹【右键】点击【Git Bash Here】
3、ssh -T git@192.*.*.*    #gitlab的地址或者域名
Welcome to GitLab, ***! #“***”表示你注册的用户名  这样表示成功

ssh -T git@github.com
Hi ***! You've successfully authenticated, but GitHub does not provide shell access.
这样表示成功

配置成功之后不代表万事大吉，我们每一个项目都需要为他配置用户名和邮箱
gitlab由于是经常使用的，所以用户名和邮箱配置为全局的
<pre><code>
cd **/gitlab #存放gitlab代码的路径
git init
git config --global user.name 'gitlab注册用户名'
git config --global user.email 'gitlab注册邮箱'
</code></pre>
github使用较少，所以用户名和邮箱配置为局部的
<pre><code>
cd **/github #存放github代码的路径
git init
git config --local user.name 'github注册用户名'
git config --local user.email 'github注册邮箱'
</code></pre>
这样，万事大吉了。








</code></pre>
