#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/4'

# for循环
'''
for i in range(10):

    代码块
'''

for i in range(10):
    print("重要的事情说n遍")

# 打印出100以内的奇数
for i in range(1,100,2):
    print(i)

for i in range(1,100):
    if(i%2 == 1):
        print(i)
# 求出1+2+3.。。+100和
s = 0
for i in range(1,101):
    s += i
print(s)
# 求出100! 1*2*3*4....*100
s = 1
for i in range(1,101):
    s *= i
print(s)
# 求出100以内的质数

for i in range(2,100):
    f = False # 标记i是否被整除
    for j in range(2,i):
        if(i%j==0):
            f = True #如果i被整除，把f值改成True
            break
    if (not f):
        print(i)

# 打印出九九乘法表（循环嵌套）
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"X",i,'=',i*j,'\t',end='')
    print()
# 冒泡排序
a = [90,43,2,63,6,3,4]
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if(a[j] > a[j+1]):
            a[j],a[j+1] = a[j+1],a[j]
print(a)

# 终止循环  break

# 打印出100以内的数，遇到5就终止
for i in range(100):
    if(i == 5):
        break
    print(i)

# 跳过本次循环 continue
# 打印出100以内的数，如果可被5整除则跳过
for i in range(100):
    if(i%5 == 0):
        continue
    print(i)

# while

'''
i=0
while(判断条件):
    循环体
    i=i+1
'''
for i in range(1,101,1):
    print(i)

i = 1
while(i < 101):
    print(i)
    i = i + 1

