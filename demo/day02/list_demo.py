#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'

l = [1,2,3,4,5,6,7,8,9,0]
# 截取某一段内容git
print(l[1:7])
print(l[:6])
print(l[2:])
print(l[:-1])
# 步长
print(l[::2])
print(l[1::2])
# 倒叙
print(l[::-1])

# 拼接 +
#
# # 成员判断 in

# 新增数据
# 在列表最后新增单个数据
l.append(11)
print(l)
# 在列表的某个位置新增单个数据
l.insert(1,11)
print(l)
# 在列表最后新增多个数据
s = [1,2,3,4]
l.extend(s)
print(l)
print(s)

# 删除数据
# 根据下标删除数据
print(l.pop())
print(l)
print(l.pop(11))
print(l)
print(l.pop(-4))
print(l)

# 根据内容删除数据
l.remove(2)
print(l)



# 修改列表中的数据

l[2]=12
print(l)


# index
print(l.index(1))
l[l.index(1)] = 9
print(l)

# 长度

print(len(l))

# 排序 reverse 排序规则 False 升序 默认   True 降序
l.sort(reverse=True)
print(l)




