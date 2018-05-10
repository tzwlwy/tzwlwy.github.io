---
layout: post
category: "python"
title:  "test"
tags: [总结]
---

>在以前公司的时候，同事有用TeamCity来做C/S架构app的持续集成，现在公司做的web项目，也考虑用TeamCity来做持续集成，于是花了好几天的时间在网上找资料，不断地尝试，终于把整个流程都跑通了，现在就把各个步骤总结下来。

Configuration和build step的层次结构如下：

-. Configuration：Build and package web app

    Build step: Build solution（编译Project）

    Build step: Publish and package (将Project发布，并将发布之后的文件打包)

-. Configuration: Replace web.config and deploy web app

    Build step: Replace connectionString in web.config（替换连接字符串）

    Build step: Stop-WebAppPool（停掉应用程序池）

    Build step: Stop-Website（停掉站点）

    Build step: Deploy web app to server(用来将最终的文件同步到server上）

    Build step: Start-Website（开启站点）

    Build step: Start-WebAppPool（开启应用程序池）

---

接下来对每一个build step进行分析：

## Build solution
![img](/img/in-post/teamcity1.jpg)

这一步会将source code拿到TeamCity的一个work directory，并完成编译。

## Publish and package
![img](/img/in-post/teamcity2.jpg)

Build file path中填写的文件是publish app时使用的配置文件，我用的是[David Wilson](https://essenceofcode.com/about/)的[文件](https://essenceofcode.com/2012/08/20/using-msbuild-and-team-city-for-deployments-part-2-continuous-integration-build-and-verify/),
代码片段如下：

```xml
<?xml version="1.0" encoding="utf-8"?>
<Project DefaultTargets="Transform"
xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
<Target Name="Publish">
<Message Text="Configuration: $(Configuration)" />
<!-- Platform=Any Cpu for Solution Files, Platform=AnyCpu for project files-->
<MSBuild Projects="$(Projects)"
         Properties="Platform=AnyCPU;
                     Configuration=$(Configuration);
                     AutoParameterizationWebConfigConnectionStrings=False;
                     DeployOnBuild=True;
                     DeployTarget=Package;
                     PackageLocation=_package;
                     PackageAsSingleFile=False;"/>
</Target>
</Project>
```

这一步完成后会在obj/Release/Package/PackageTmp 中生成publish完了之后的文件，这个时候我们将IIS的站点的物理地址指向这里，就完全可以运行起来了。但我们还需要对web.config文件做一些修改，所以暂时我们将生成的相关文件打包好，在下一个configuration中再去修改和部署。

打包发布出来的文件：
![img](/img/in-post/teamcity3.jpg)

## Replace web.config

首先我们需要在这个configuration中添加对上一个configuration的Artifacts的依赖。
![img](/img/in-post/teamcity4.jpg)

这里用的PowerShell来执行连接字符串的替换：

```powershell
$connectionString = "Data Source=shaappt0001;Initial Catalog=Demo.Test;Persist Security Info=true;User ID=YourAccount;PWD=YourPassword;Packet Size=4096;"
$webConfigPath = "%teamcity.build.workingDir%\Demo.Test\web.config"
$xml = [xml](get-content $webConfigPath)
$root = $xml.get_DocumentElement();
$root.connectionStrings.add.connectionString = $connectionString
$xml.Save($webConfigPath)
```

## Stop-WebAppPool
![img](/img/in-post/teamcity5.jpg)

```powershell
Stop-WebAppPool -Name "Demo.Test"
```

## Stop-Website
![img](/img/in-post/teamcity6.jpg)

```powershell
Stop-Website "Demo.Test"
```

## Deploy web app to server
![img](/img/in-post/teamcity7.jpg)

```
"C:\Program Files\IIS\Microsoft Web Deploy V3\msdeploy.exe" -verb:sync -source:contentPath="%teamcity.build.workingDir%\%env.PackagePath%\" -dest:contentPath="%env.DestinationSite%"
```
>Note：记住在填入这个脚本的时候一定不要在里面换行，要不然TeamCity可能会不认识，导致编译不通过。

环境变量的设置：
![img](/img/in-post/teamcity10.jpg)

## Start-Website
![img](/img/in-post/teamcity8.jpg)

```powershell
Start-Website "Demo.Test"
```

## Start-WebAppPool
![img](/img/in-post/teamcity9.jpg)

```powershell
for($i=1; $i -le 10; $i++)
{
    Start-WebAppPool -name "Demo.Test";
    if((get-WebAppPoolState -name "Demo.Test").Value -eq "Started")
    {
        break;
    }
    else
    {
       Start-Sleep -s 30;
    }     
}
```
