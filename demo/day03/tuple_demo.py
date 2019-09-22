#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/6'

# 截取
t = (1,2,3,5,67)
#截取一部分
print(t[1:3])
print(t[:-1])

#倒叙

print(t[::-1])

# 查

print(t[1])


# 拼接

# 成员判断

# 获取元组长度
print(len(t))

# 索引

print(t.index(5))

'''
列表中元素可被更改，元组中的元素不能被修改
元组中只有一个数据的时候，最后需要以逗号结尾，而列表就不需要了
'''