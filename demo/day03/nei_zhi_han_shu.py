#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/6'


'''
自定义模块
复制到项目里边
然后在使用import语法导入
使用

python提供的内置模块
直接import导入
使用

第三方模块

'''
'''
a = 1
print("sss")   
    作用，输入到控制台
    参数：要打印的对象，end 修改结尾符号
type(a)
    作用：返回变量类型
    参数：变量
b = '11111'
len(b)
    作用：查看查看 str list tuple dict长度
    参数：变量
range(1,2)
    作用：返回一个可迭代对象，可以使用in来取值
    参数1：起始值
    参数2：结束值
    参数3：步长
int(b)
    作用：把变量从其他类型转换为整型
    参数：要转换的变量
str()
    作用：把变量从其他类型转换为字符串类型
    参数：要转换的变量
list()
    作用：把变量从其他类型转换为列表类型
    参数：要转换的变量
dict()
    作用：合并两个字典，生成一个新的字典
    参数1：字典变量1
    参数2：**字典变量2
tuple()
    作用：把变量从其他类型转换为元组类型
    参数：要转换的变量
'''

# # 作用，打开一个文件
# # 参数1：文件路径
# # 参数2：打开方式，r 读 w 先清空文件内容，然后在写入 a 追加写入 b 二进制模式
# # 参数3：encoding 编码格式
# f = open("E:\\softwaredata\\python\\gy-1908A\\demo\\day03\\test.txt","r",encoding='utf-8')
# # 按行读取文件内容，返回一个列表
# print(f.readlines())
# # 读取文件所有内容，返回一个字符串
# # print(f.read())
# # 关闭文件
# f.close()

#
f = open("E:\\softwaredata\\python\\gy-1908A\\demo\\day03\\test.txt","w",encoding='utf-8')

# f.write("sdjfisdjfijsdifasldfk")
f.writelines(["sdfisjdifusidf\n",'sjdifjsidfjisd\n','sjdfsdjifjsdiff\n'])
# 关闭文件
f.close()

