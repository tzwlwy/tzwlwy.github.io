---
layout: post
category: "python"
title:  "python2核心编程笔记"
tags: [python]
---

**最近想把基础重新完善并深入学习一下python，再看python2核心编程**
今天看到了第 337页，共925页。 感覺有點靜不下心來看
```python
range([[start,]stop[,step])  #range的使用方法
b=input('请输入字符:')   #input
x, y, z = 1, 2, 'a string' #一次性声明变量
y = x = x + 3  #赋值 ，常规理解y = (x = x + 3 ) ，这么写在python中是错误的
sqdEvens = [x ** 2 for x in range(8) if not x % 2]
s = 'abcde'
a=[s[:int(len(s)-y)] for y in range(0, len(s))]
object.attribute
'%s %s' % ('Spanish', 'Inquisition')
s = ' '.join(('Spanish', 'Inquisition', 'Made Easy'))
#print 语句中使用逗号来抑制自动生成的换行符号
dict2.pop('name') # 删除并返回键为“name”的条目

dict2= {'host':'earth', 'port':80}
dict3= {'host':'venus', 'server':'http'}
dict2.update(dict3)   #类似新增，但是在dict中相同key只保留dict2的
>>> dict2
{'server': 'http', 'port': 80, 'host': 'venus'}
print(dict2.get('host'))   #venus
dict2.setdefault('host1','venus1') #设置默认dict健值，若存在则失效
smaller = (x < y and [x] or [y])[0]  #等价于 smaller = x if x < y else y
```
```python
w 以写方式打开 (必要时清空)
a 以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+ 以读写模式打开
w+ 以读写模式打开 (参见 w )
a+ 以读写模式打开 (参见 a )
rb 以二进制读模式打开
wb 以二进制写模式打开 (参见 w )
ab 以二进制追加模式打开 (参见 a )
rb+ 以二进制读写模式打开 (参见 r+ )
wb+ 以二进制读写模式打开 (参见 w+ )
ab+ 以二进制读写模式打开 (参见 a+ )
```


迭代器
```python
myTuple = (123, 'xyz', 45.67)
i = iter(myTuple)
print(next(i))
print(next(i))
print(next(i))
# 123
# xyz
# 45.67

#这里的cols也可以用list代替
rows = [1, 2, 3, 17]
def cols(): # example of simple generator
   yield 56
   yield 2
   yield 1
x_product_pairs = ((i, j) for i in rows for j in cols())
print(x_product_pairs)
for pair in x_product_pairs:
   print (pair)


#文件本身就是一个迭代器，之前需要读取所有行  （改造前）
f = open(r'D:\testing\program\interface\test.txt', 'r')
longest = 0
allLines = f.readlines()
f.close()
for line in allLines:
    linelen = len(line.strip())
    a=line.strip()
    if linelen > longest:
       longest = linelen
       print(longest)
       print(a)

#改造后
f = open(r'D:\testing\program\interface\test.txt', 'r')
allLineLens = [len(x.strip()) for x in f]
f.close()
print(allLineLens)

```

albums
```python
albums = ['tales', 'robot', 'pyramid']
for i, album in enumerate(albums):
  print(i, album)
  
0 tales
1 robot
2 pyramid
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

os 模块属性 描述
```python
linesep 用于在文件中分隔行的字符串
sep 用来分隔文件路径名的字符串
pathsep 用于分隔文件路径的字符串
curdir 当前工作目录的字符串名称
pardir (当前工作目录的)父目录字符串名称
```

isinstance用法
```python
num='5'
if isinstance(num, (int,str, float, complex)):
    print('right')
else:
    print('fuck')
```


== 和 is 的区别

```python
你认为type(a) == type(b)和type(a) is type(b)之间的不同是什么？为什么会选者后者？函数isinstance()与这有什么关系？
“==”比较的是值，is比较的是对象。因为每个对象只可能有一种类型的值，所以可以直接比较他们的ID，而不用先计算值再做比较
函数isinstance()用来确定这个对象是否属于这个类型，或者实例是否属于某个类。
```


随笔小程序1
```python
import os
ls = os.linesep  #  linesep = '\r\n'  使用这个可以解决跨系统的问题，因为linux换行符不是 \r\n
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