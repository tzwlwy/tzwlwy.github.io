---
layout: post
category: "python"
title:  "getattribute和默认参数 *args **kwargs"
header-img: "img/in-post/header.jpg"
tags:
    - Python
---

今天再看基础知识的时候看到了一个以前忽略的方法，叫__getattribute__，了解了一下
__getattribute__是属性访问拦截器，就是当这个类的属性被访问时，会自动调用类的__getattribute__方法
每一次调用__getattribute__时，会把参数以str的方式传入，第一版我是这么写的
```python
    def __getattribute__(self,required1, required2, *args,**kwargs):
        print(required1)
        print(required2)
        print(args)
        print(kwargs)
        return object.__getattribute__(self,required1, required2, *args,**kwargs)
```
然后发现这么写报错了
TypeError: __getattribute__() missing 1 required positional argument: 'required2'
我想看这个方法的内部逻辑是什么，很可惜，点不进去，
后来发现它这边每次传入的值都是str，并且其实它每次只传入一个参数
改进后所有的代码如下


```python
class Tree(object):
    count=0
    def __init__(self,required1, required2, *args,**kwargs):
        self.required1=required1
        self.required2=required2
        self.args=args
        print(type(self.args))
        self.kwargs=kwargs
        print(type(self.kwargs))
        self.count+=1

    def print_more(self):
          print(self.required1)
          print(self.required2)
          print(self.args)
          print(self.kwargs)
          print(self.count)
    def __getattribute__(self,args):
        print(args)
        return object.__getattribute__(self, args)

a=Tree('cap', 'gloves', 'scarf',dessert='macaroon',wine= 'merlot')
a.print_more()
print(a.kwargs)
print(type(a.kwargs))
```

另外，以前做过笔记args，**kwargs结合 （这种需要**kwargs 为{}），这个时候如果写的是args，
那么str类型的参数只能是一个，如果是多个的话就必须使用*args，这个时候传入的多个str类型就被整合
成一个tuple了


