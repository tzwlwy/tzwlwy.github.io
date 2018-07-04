---
layout:     post
title:      "如何安装Ionic环境"
subtitle:   ""
date:       2016-06-10
author:     "Tesla9527"
header-img: "img/post-bg-unix-linux.jpg"
catalog:    true
tags:
    - Ionic
---

## 安装jdk
[http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

![img](/img/in-post/ionic1.gif)

安装完成后添加jdk的环境变量

系统变量→新建 JAVA_HOME 变量 。

变量值填写jdk的安装目录（本人是 E:\Java\jdk1.7.0)

系统变量→寻找 Path 变量→编辑

在变量值最后输入 %JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;

（注意原来Path的变量值末尾有没有;号，如果没有，先输入；号再输入上面的代码）

检验是否配置成功 运行cmd 输入 java -version （java 和 -version 之间有空格）

若如图所示 显示版本信息 则说明安装和配置成功。

---

## 安装android sdk
[http://developer.android.com/sdk/index.html#Other](http://developer.android.com/sdk/index.html#Other)
![img](/img/in-post/ionic2.jpg)

指定好目录后，需要下载需要的版本的sdk，由于GFW的原因，比较好的办法是下载对应版本的sdk，然后解压后放到sdk安装的目录中。
下面是镜像:
[http://www.cnblogs.com/bjzhanghao/archive/2012/11/14/android-platform-sdk-download-mirror.html](http://www.cnblogs.com/bjzhanghao/archive/2012/11/14/android-platform-sdk-download-mirror.html)

---

## 安装Node.js
[https://nodejs.org/en/](https://nodejs.org/en/)
![img](/img/in-post/ionic3.jpg)

---

## 安装淘宝NPM镜像
由于NPM中的有些源被墙了，所以采用镜像的模式安装，这里我们使用淘宝NPM镜像。
[http://npm.taobao.org/](http://npm.taobao.org/)
![img](/img/in-post/ionic4.jpg)

---

## 安装cordova
![img](/img/in-post/ionic5.jpg)

---

## 安装Ionic
![img](/img/in-post/ionic6.jpg)

---

## 安装Genymotion，用来模拟手机

[https://www.genymotion.com/](https://www.genymotion.com/)
安装完之后新建一个虚拟机并启动

---

## 使用Ionic新建项目
比如说我们计划把项目放在E:\projects\myapps中，项目名称为DemoTest

cmd中切换到目录E:\projects\myapps，

- 执行命令：ionic start DemoTest
- 切换到项目目录DemoTest：cd DemoTest
- 安装android编译环境：ionic platform add android
- 编译项目：ionic build android（在第一次执行这一步的时候，会去下载文件http\\://services.gradle.org/distributions/gradle-2.2.1-all.zip，有44.7M，
又因为有墙，慢到无法忍受。这个时候可以手动把这个文件下载好，部署到自己的一个服务器上，
然后把\platforms\android\cordova\lib\builders\GradleBuilder.js里的var distributionUrl = process.env[‘CORDOVA_ANDROID_GRADLE_DISTRIBUTION_URL’] || ‘http\\://services.gradle.org/distributions/gradle-2.2.1-all.zip’;
后面的http\\://services.gradle.org/distributions/gradle-2.2.1-all.zip改为自己部署的地址就会解决下载慢的问题了）
- 模拟器上运行：ionic run android
- 浏览器中显示：ionic serve
![img](/img/in-post/ionic7.jpg)

---

## 模拟器上安装演示
<iframe width="560" height="315" src="https://www.youtube.com/embed/9ECDsjXkhhc" frameborder="0" allowfullscreen></iframe>
