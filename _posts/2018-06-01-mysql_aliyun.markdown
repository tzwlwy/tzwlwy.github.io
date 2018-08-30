---
layout: post
category: "other"
title:  "阿里云安装mysql"
header-img: "img/in-post/post-bg-unix-linux.jpg"
tags:
    - Msql
    - 阿里云
---

一直想玩玩linux，刚好又想深入学习一下mysql，然后就合二为一了

**安装mysql**
参考地址：[https://www.cnblogs.com/bigbrotherer/p/7241845.html](https://www.cnblogs.com/bigbrotherer/p/7241845.html)
<pre><code>
安装用的Yum Repository
wget -i -c http://dev.mysql.com/get/mysql57-community-release-el7-10.noarch.rpm 
yum -y install mysql57-community-release-el7-10.noarch.rpm    yum安装
yum -y install mysql-community-server  安装MySQL服务器
systemctl start  mysqld.service  启动mysql服务
systemctl status mysqld.service  查看mysql服务状态
grep "password" /var/log/mysqld.log  查看初始密码
mysql -uroot -p  进入mysql
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';  
这里直接这么设置需要设置密码比较复杂，123456会失败
set global validate_password_policy=0; 改变密码复杂度设置
set global validate_password_length=1; 改变密码长度设置
ALTER USER 'root'@'localhost' IDENTIFIED BY '123456';  这个时候就可以了
exit 退出mysql
yum -y remove mysql57-community-release-el7-10.noarch 卸载Yum Repository，防止它自动更新 
</code></pre>


**设置 访问权限**
详情访问 [http://www.jb51.net/article/121173.html](http://www.jb51.net/article/121173.html)
<pre><code>
mysql -u root -h localhost -p 登录mysql
update user set host='%' where user='root' and host='localhost'; 所有ip都可访问，设置私密性请看详情
</code></pre>

**mysql linux部分指令**
<pre><code>
service mysqld restart 重启sql服务
启动mysql
sudo systemctl start mysqld
停止、重启My SQL 服务的命令如下：
sudo systemctl stop mysqld
sudo systemctl restart mysqld
</code></pre>