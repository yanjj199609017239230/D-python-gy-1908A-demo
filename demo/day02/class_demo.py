#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'

class ClassDemo():
    def aaa(self):
        print("我是aaa")
    def bbb(self):
        print("我是bbb")
        self.aaa()

if __name__ == '__main__':
    c = ClassDemo()
    c.aaa()
    c.bbb()
