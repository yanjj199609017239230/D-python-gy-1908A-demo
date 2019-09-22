#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'
'''
#方法定义
def 方法名(变量1,变量2,..):
方法体

#方法调用
方法名(参数1,参数2,...)

'''

#无参数，无返回值的方法
#方法定义
def jia_fa():
    a = 1
    b = 2
    print(a+b)

# 方法调用
jia_fa()



#有参数，无返回值的方法
#方法定义
def jia_fa(a,b):
    print(a+b)

# 方法调用
jia_fa(3,5)
jia_fa(4,10)


#无参数，有返回值的方法
def jia_fa(x,y):
    a = x
    b = y
    return a + b
c = jia_fa()
print(c)
# 有参数，有返回值
def jia_fa(a,b):
    return a + b
c = jia_fa(4,7)
print(c)

def bbb(a,b=10):
    return a+b
print(bbb(11))
print(bbb(11,30))
print(bbb(1,b=20))


def aaa(*args,**kwargs):
    print(args)
    print(kwargs)


aaa({'name':'xuepl'},4,7,8,9,34,b=100,c=1000)


if __name__ == '__main__':
    #程序的入口
    print("我是main方法")
