---
layout: post
category: "复习"
title:  "面试复习-测试框架介绍"
header-img: "img/in-post/post-bg-unix-linux.jpg"
tags:
    - 复习
---
<pre><code>
测试框架：
测试框架主要分几部分：
第一部分是flask框架，里面就是最基本的flask框架的几个模块，包含static，templates及下面的forms及views，但实际我使用的主要就是static及views，因为我前段用的是饿了么的element框架，所以并不是很需要用他原生的。
然后会有一个DB，这个DB是自己二次封装的pymsql包，主要是用来连接数据库，并进行增删改查操作并转换成list
然后还有一个methods包，里面会放一些常用的方法，例如md5加密，随机数啊，元组转str啊等等。然后再下面就是一个web自动化的框架，核心是selenium，配合unitted框架，这个框架我简历有写，其主要思想是采取object model 的形式，数据分离的形式，
（在UIMap里面放各个页面的元素信息，App.config放一些默认的配置信息，TestCase存放所需要的测试用例，TestData存放一些测试数据，以json或者excel的形式；Modules放每个页面的一些方法；CommonHelper 放一些公用的方法 ，通过二次封装WebApi里的方法，来更好的维护与编写测试用例。）
在下面还有一个servise的包，里面主要是WebsocketServer的一些方法
再然后就是一个配置文件及run启动文件了，启动文件主要是运行两个线程，一个起flask的线程，还有一个起websocket的线程
</code></pre>