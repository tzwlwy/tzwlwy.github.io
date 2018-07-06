#!/usr/bin/env python
from time import time
def logged(when):
   def log(f, *args, **kargs):
      print ('''Called:
       function: %s
       args: %r
       kargs: %r''' % (f, args, kargs))

def pre_logged(f):
   def wrapper(*args, **kargs):
        log(f, *args, **kargs)
        return f(*args, **kargs)
   return wrapper

def post_logged(f):
    def wrapper(*args, **kargs):
        now = time()
        try:
            return f(*args, **kargs)
        finally:
            log(f, *args, **kargs)
            print(
            "time delta: %s" % (time() - now))
            return wrapper
    try:
             return {"pre": pre_logged,
                     30 "post": post_logged}[when]
         31 except KeyError, e:
         32
         raise ValueError(e), 'must be "pre" or "post"'
         33
         34 @ logged("post")
         35


    def hello(name):
        36
        print
        "Hello,", name
hello("World!