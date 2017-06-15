# -*- coding:UTF-8 -*-
# this one is like your scripts with argv                     这一个就像你的脚本与argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this   确定，* args实际上是无意义的，我们可以这样做
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)
	 
# this just takes one argument                                 这只是一个参数
def print_one(arg1):
    print "argl: %r" % arg1
	
# this one takes no arguments                                 这个没有参数
def print_none():
    print "I got nothin'."
	
	
print_two("zed","Shaw")
print_two_again("zed","Shaw")
print_one("First!")
print_none()