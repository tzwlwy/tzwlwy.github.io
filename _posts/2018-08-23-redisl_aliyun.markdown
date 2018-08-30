---
layout: post
category: "other"
title:  "阿里云安装redis和mongodb"
header-img: "img/in-post/post-bg-unix-linux.jpg"
tags:
    - redis
    - 阿里云
---

爬虫必装环境 redis

**安装redis**

<pre><code>
首先添加EP EL 仓库，然后更新yum 源：
sudo yum install epel release
sudo yum update
然后安装Redis 数据库：
sudo yum -y install redis
安装好后启动Redis 服务即可：
sudo systemctl start redis
</code></pre>


**安装mongodb**
参考地址：[https://www.cnblogs.com/layezi/p/7290082.html](https://www.cnblogs.com/layezi/p/7290082.html)
<pre><code>
sudo vi /etc/yum .repos.d/mongodb-org.repo
写入
[mongodb-org-3.4]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc

sudo yum install mongodb-org

启动命令:
service mongod start
 停止命令:
service mongod stop
 重启命令:
service mongod stop
查看日志文件
cat /var/log/mongodb/mongod.log
</code></pre>