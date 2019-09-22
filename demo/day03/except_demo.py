#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/6'



def div(a,b):
    # try:
    #     c = a/b
    # except :
    #     print("除数不能为0")
    #     return
    #
    # return c
    c = a / b



def operate_file():
    try:
        # open("test", 'r')
        g = open("test.txt", 'w')
        g.read()
        g.close()
        g.write("sssss")
    except FileNotFoundError:
        print("文件不存在")
    except ValueError:
        print("文件已关闭")

operate_file()