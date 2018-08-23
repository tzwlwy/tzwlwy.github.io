---
layout: post
category: "other"
title:  "阿里云安装redis"
header-img: "img/in-post/post-bg-unix-linux.jpg"
tags:
    - redis
    - 阿里云
---

一直想玩玩linux，刚好又想深入学习一下mysql，然后就合二为一了

**安装redis**

<pre><code>
首先添加EP EL 仓库，然后更新yum 源：
sudo yum install epel release
sudo yum update
然后安装R e d i s 数据库：
sudo yum -y install redis
安装好后启动Re di s 服务即可：
sudo systemctl start redis
</code></pre>