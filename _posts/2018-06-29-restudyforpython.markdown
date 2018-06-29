---
layout: post
category: "python"
title:  "python2核心编程笔记"
tags: [python]
---

**最近想把基础重新完善并深入学习一下python，再看python2核心编程**
今天看到了第 87页，共925页。
```python
range([[start,]stop[,step])  #range的使用方法
b=input('请输入字符:')   #input
x, y, z = 1, 2, 'a string' #一次性声明变量
y = x = x + 3  #赋值 ，常规理解y = (x = x + 3 ) ，这么写在python中是错误的

```

下划线
```python
class Student:
    def __init__(self, name, age):
        self._name = name
        self.age=age

stu=Student('Alvin','30')
#当要输入_name时，pycharm不会进行_name的提示
print(stu._name)
#当要显示age时，pycharm会进行age的提示
print(stu.age)

#下划线__

class Person:
    def __init__(self, name):
        self.__name=name

per=Person('Young')
# print(per.__name)  __表示私有的，只能通过下面这种形式访问
print(per._Person__name)
```

isinstance用法
```python
num='5'
if isinstance(num, (int,str, float, complex)):
    print('right')
else:
    print('fuck')
```


随笔小程序1
```python
import os
ls = os.linesep  #  linesep = '\r\n'
print(ls)
# get filename
while True:
 fname = input('Enter filename: ')
 if os.path.exists(fname):
    print ("ERROR: '%s' already exists" % fname)

 else:
    break

 # get file content (text) lines
all = []
print ("\nEnter lines ('.' by itself to quit).\n")
 # loop until user terminates input
while True:
 entry = input('> ')
 if entry == '.':
   break
 else:
   all.append(entry)
 # write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()
print ('finish!')
```