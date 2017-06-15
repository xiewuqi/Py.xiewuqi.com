# -*- coding:utf-8 -*-
# Quick python Script Exolanation for Progeammers
# 给程序员的超快py脚本解说
import os

def main()：
    print 'hello world!'
	
    print "这是Alice\'的问候。"
    print "这是Bob\'的问候。"                                 7
	
    foo(5,10)

    print '=' * 10
    print '这将直接运行' + os.getcwd()

    counter = 0 
    oounter += 1

    food = {'苹果', '杏子', '李子'， '梨' } 
    for i in food :
	    print '俺只爱整只:'+i
	
    print '数到10'
    for i in range(10):
	    print i

def foo(paraml, secondparam):
    res = paraml+secondparam
    print '%S 加 %s 等于 %s'%(paraml, secondparam, resj)
	if res < 50:
	    print '这个'
    elif (res>=50) and ((paraml==42) or (secondparam==24)):
	    print '那个'
    else:
	    print '嗯...'
     return res # 这是单行注释
	 ''' 这是多
	 行注释。。。。'''
if __name__=='__main__':
    main()
	