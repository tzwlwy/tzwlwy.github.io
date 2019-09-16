---
layout: post
category: "python"
title:  "Python 奇技淫巧"
header-img: "img/in-post/post-bg-unix-linux.jpg"
tags:
    - python
---

咋一看，五个月没更新博客了，刚好碰到一个有点意思的库，赶快更新一波
```python
import pysnooper

@pysnooper.snoop()
def one(number):
    mat = []
    while number:
        mat.append(number)
        number -= 1
    return mat

one(3)
```
效果如下
![img](/img/in-post/python/locust6.jpg)










