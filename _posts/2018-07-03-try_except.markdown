---
layout: post
category: "python"
title:  "try except 对性能的影响"
header-img: "img/in-post/post-bg-unix-linux.jpg"
tags:
    - Python
---
**最近在重温基础知识，看到try except 模块**

```python
try:
    print(1/0)
except Exception as e:
    print(e)
else: #
    print('未出现异常时输出这句话')
finally:
    print('无论是否异常都输出这句话')
```

```python
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        startTime = time.time()
        f = func(*args, **kwargs)
        endTime = time.time()
        passTime = endTime - startTime
        print ("执行函数%s使用了%f秒" % (getattr(func, "__name__"), passTime))
        return f
    return wrapper

def do_something():
    a = 1

@timer
def test1():
    for _ in range(1000000):
        do_something()

@timer
def test2():
    try:
        for _ in range(1000000):
            do_something()
    except Exception:
        do_something()
    else:
        pass
    finally:
        pass

@timer
def test3():
    for _ in range(1000000):
        try:
            do_something()
        except Exception:
            do_something()
        else:
            pass
        finally:
            pass

@timer
def test4():
    zero = 0
    for _ in range(1000000):
        try:
            if zero == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            do_something()
        else:
            pass
        finally:
            pass

@timer
def test5():
    zero = 0
    for _ in range(1000000):
        try:
            if zero == 0:
                raise ZeroDivisionError
        except BaseException:
            do_something()
        else:
            pass
        finally:
            pass

@timer
def test6():
    zero = 0
    for _ in range(1000000):
        try:
            if zero == 0:
                raise ZeroDivisionError
        except:
            do_something()
        else:
            pass
        finally:
            pass


@timer
def test7():
    zero = 0
    try:
        if zero == 0:
            raise ZeroDivisionError
    except ZeroDivisionError:
        for _ in range(1000000):
            do_something()
    else:
        pass
    finally:
        pass


@timer
def test8():
    zero = 0
    for _ in range(1000000):
        if zero == 0:
            do_something()


test1()
test2()
test3()
test4()
test5()
test6()
test7()
test8()

执行函数test1使用了0.109000秒
执行函数test2使用了0.110000秒
执行函数test3使用了0.140000秒
执行函数test4使用了0.407000秒
执行函数test5使用了0.416000秒
执行函数test6使用了0.358000秒
执行函数test7使用了0.114000秒
执行函数test8使用了0.144000秒
```


对比结论
通过对比1和2，可以得知直接执行耗时操作和耗时操作放在try中执行并无异常触发时性能消耗几乎是一样的。
通过对比2和7，可以得知使用异常的使用无论是把代码放在 try 中执行还是在 except 中执行性能消耗几乎是一样的。
通过对比2和3，可以得知当不抛出错误时，把try放耗时操作中比耗时操作放在try中性能消耗要略大。
通过对比3和4，可以得知当使用try时无异常抛出跟使用try时抛出异常性能消耗几乎相差好几倍。
通过对比4和5，可以得知try放耗时操作中时，try每一次操作并进行异常处理(捕捉抛出的特定异常)跟try每一次操作并进行异常处理(捕捉所有异常 try…except BaseException)性能消耗几乎是一样的。
通过对比4和8，可以得知使用防御性方式编码比捕捉异常方式性能消耗几乎相差好几倍。
通过对比5和6，可以得知捕捉所有异常（try…except）方式比捕捉所有异常(try…except BaseException)方式要略快。

总结
由以上对比结论，可以总结为：
增加防御性方式，处理速度更快，在未抛出异常的前提下，是否使用try catch 性能影响很小，在写代码时尽量明确返回的格式，通过效验
格式等方式去进行防御


