---
layout: post
category: "tags"
title:  "正则总结"
tags: [总结]
---

*对于不熟悉正则的同学来说，需要对比关照正则一些符号才更为直观，暂时未放图片，更多请访问印象笔记

<pre><code>import re
tt = "Tina is a good girl, she is cOOl, clever, and so on..."
rr = re.compile(r'\w*oo\w*',flags=re.I)
print(rr.findall(tt))   #查找所有包含'oo'的单词</code></pre>

<pre><code>import re
a=re.search(r'(tina)(fei)haha\2','tinafeihahafei tinafeihahatina').group()
//\2 表示取()里面的第二个值，如果改为\1，则匹配tian
//a= tinafeihahafei
print(a)
d=re.search(r'(tina)(fei)haha','tinafeihahafei tinafeihahatina').group()
//这边这么写的话仅取值包含正则的内容
//d = tinafeihaha
print(d)

//这里需要强调一下\b的单词边界的理解：
w = re.findall('\btina','tian tinaaaa')
print(w)
s = re.findall(r'\btina','tian tinaaaa')
print(s)
v = re.findall(r'\btina','tian#tinaaaa')
print(v)
a = re.findall(r'\btina\b','#tina@aaa')
print(a)

//正则特殊分组法
w = re.findall('(?P<name>aa)1','tian tinaa1aa')
//这里find 的是 aa1 ，然后输出的内容是aa；
print(w)
w = re.findall('(?P<id>\d)abc(?P=id)','aa1121abc121aa2')
//这里find 的是 数字abc数字 ，前后数字需要保持一致，然后输出的内容是那个数字；
print(w)
w = re.findall(r'(\d)abc\1','5abc522abc4')
//引用编号为<number>的分组匹配到字符串，也就是说数字abc数字，前后数字需保持一致
print(w)
</code></pre>

<pre><code>import re
result = re.match('you', 'Young Frankenstein')
source = 'Young Frankensteinn1n'
m = re.match('You', source)
print(m, type(m))
print(m.group(), type(m.group()))

m = re.match('.*Frank', source)  #这样返回到需求为止的所有字符串
// 使用. 代表任意除\n 外的字符；
// 使用* 表示任意多个字符（包括0 个）；
//使用? 表示可选字符（0 个或1 个）**
if m:
    print(m.group())

m = re.findall('n', source) #返回一个列表
m = re.findall('n.', source)#返回所有含有n. 的，如果n在最后，那么不匹配
m = re.findall('n.?', source) #这种当最后匹配时，单独输出
m = re.split('n', source) #按照n作为分割符
m = re.sub('n', '?', source)#用？代替n


source2 = '''I wish I may, I wish I might
... Have a dish of fish tonight.a 1 dish1 of fish tonight'''
m=re.findall('wish', source2)
m=re.findall('wish|fish', source2)#对源字符串任意位置查询wish 或者fish
m=re.findall('^wish', source2)#从字符串开头开始匹配wish
m=re.findall('fish$', source2)#从字符串结尾开始匹配fish
m=re.findall('fish tonight\.$', source2)#.$ 可以匹配末尾的任意字符，包括句号
m=re.findall('[wf]ish', source2)#查询以w 或f 开头，后面紧接着ish 的匹配
m=re.findall('[wsh]+', source2)#查询以若干个w、s 或h 组合的匹配['w', 'sh', 'w', 'sh', 'h', 'sh', 'sh', 'h']
m=re.findall('ght\W', source)#查询以ght 开头，后面紧跟一个非数字非字母字符的匹配
m=re.findall('I (?=wish)', source2)# 查询以I 开头，后面跟着wish 的匹配（wish 出现次数尽量少）：
                                   # 我的理解是查找所有i wish 的，但是返回值是i
m=re.findall('\bfish', source2) #输出为 空,因为/b被转义了
m=re.findall(r'\bfish', source2)#/b 表示前面或者后面一个是字母，一个不是，我们现在写的就是前面不是字母，后面是字母
m=m = re.search(r'(. dish\b).*(\bfish)', source2) #search 返回的是一个object，取它的值需要print她的group（）
print(m)
print(m.group())
print(m.groups())
</code></pre>

<pre><code>re.match与re.search与re.findall的区别：
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。

a=re.search('[\d]',"abc33").group()
print(a)
p=re.match('[\d]',"abc33")
print(p)
b=re.findall('[\d]',"abc33")
print(b)
执行结果：
None
['3', '3']

贪婪匹配与非贪婪匹配
*?,+?,??,{m,n}?    前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配（详见上面的表格）
a = re.findall(r"a(\d+?)",'a23b')
print(a)
b = re.findall(r"a(\d+)",'a23b')
print(b)
执行结果：
['2']
['23']
</code></pre>

<pre><code>import re
a = "123abc456d"
print(re.search("([0-9]*)([a-z]*)([0-9]*)d",a).groups())   #groups 返回的是一个元祖，由除了group（0）之外的元素组成
print(re.search("([0-9]*)([a-z]*)([0-9]*d)",a).group(0))   #123abc456,返回整体
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1))   #123
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2))   #abc
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))   #456
//group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。

iter = re.finditer(r'\d+','12 drumm44ers drumming, 11 ... 10 ...')
for i in iter:
    //print(i)
    print(i.group())
    print(i.span())
执行结果如下：
'''
(0, 2)
(8, 10)
(24, 26)
(31, 33)
print(re.split('\d+','one1two2three3four4five5'))
['one', 'two', 'three', 'four', 'five', '']</code></pre>
