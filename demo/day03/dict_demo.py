#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/6'


'''
key:value

key唯一
key必须是不可变的，数字，字符串，元组，列表（不可以），字典（不可以）
'''

# 增
# 初次创建
d = {}
d1 = {'name':'小明同学','sex':'女'}
# 新增一对数据
d1['age'],d1['high'] = 18,180

print(d1)

# 删
# 删除key
print(d1.pop("high"))
print(d1)

del d1["sex"]
print(d1)
print("-------")
# 删除整个字典

# del d1
# print(d1)

# 清空
# d1.clear()
# d1 = {}

# 改

d1["name"] = '小红同学'
d1["name"] = '小芳同学'
print(d1)


# 查
print(d1["name"])

# 获取字典长度
print(len(d1))

# 成员判断，只能用key做判断

print("name" in d1)


# 字典拼接
d2 = {"1":'234',"2":'346'}

d3 = {"3":'567',"4":'5789'}

# 在某个字典末尾加上另一个字典
# 拿着d3修改d2，d2中key有则改value，无则新增
# d2.update(d3)
# print(d2)

# 生成一个新的字典
c = dict(d2,**d3)
print(c)
print("2345")

