#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/5'

# range(1,2,1)


# 截取
a = 'aaaaadfsdfjksjfk'
# 截取其中一段
print(a[1:5])
print(a[5:])
print(a[:7])
print(a[:-2])

# 字符串倒叙排列
print(a[::-1])

# dergakio   要求生成两个新的字符串  drai  和egko
b = "dergakio"
print(b[::2])
print(b[1::2])

# 通过下标取出字符串中的字符
print(b[2])

# 重复字符串

print(b * 10)

# + 字符串拼接

# in 成员判断

# 字符串切片
d = '用例名,充值金额,断言'
print(d.split(","))

# 去空格
e = '   sdjfisdjifjis   '
print(e.strip())

# 替换

f = 'ssdfsdf09op"89023489'

print(f.replace('"',"'"))

# 查找

g='guoyasoft'

print(g.find("ya"))

# 长度
print(len(g))


'''
GET https://www.fiddler2.com/UpdateCheck.aspx?isBeta=False HTTP/1.1
拿到请求方法，协议版本，协议名，域名或者ip如果有端口拿到端口，请求地址，请求数

'''
u = "GET https://www.baidu.com/s?ie=utf-8&newi=1&mod=11&isbd=1&isid=e185de6b00203012&wd=python&rsv_spt=1&rsv_iqid=0xb94725970006646d&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&oq=python%2520%25E5%25AD%2597%25E7%25AC%25A6%25E4%25B8%25B2%25E8%25A7%25A3%25E6%259E%2590%25E7%25BB%2583%25E4%25B9%25A0&rsv_t=bd1bKkCI5HcHRBA6dkmZFWPH%2BJV8DBU9qaojGUlxeg1t3Y9bO5jgY%2FlzLDn03NzI9ceZ&inputT=1541&rsv_pq=e185de6b00203012&rsv_sug3=9&rsv_sug1=6&rsv_sug7=000&bs=python%20%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%A7%A3%E6%9E%90%E7%BB%83%E4%B9%A0&rsv_sid=1447_21114_29522_29520_29720_29567_29221&_ss=1&clist=&hsug=python%20%E5%AD%97%E7%AC%A6%E4%B8%B2%E8%A7%A3%E6%9E%90%E7%BB%83%E4%B9%A0%09python%20xlrd%E5%85%B3%E9%97%ADexcel%E6%96%87%E4%BB%B6&csor=6&pstg=5&_cr1=53418 HTTP/1.1"

l = u.split(" ")
method = l[0]
print("请求方法为："+method)
xieyibanben = l[2]
print("协议版本为：" + xieyibanben)
url = l[1]
print(url)
if('?' in url):
    print("请求数据为：" + url.split("?")[1])
    url = url.split("?")[0]
print(url)
print("协议名为：" + url[:url.find("://")])

url = url[url.find("://") + 3:]
print(url)
if(":" in url):
    print("域名或者ip为："+url.split(":")[0])
    url  = url.split(":")[1]
    print(url)
    print("端口号为：" + url[:url.find('/')])
    print("请求地址为：" + url[url.find('/'):])
else:
    print("域名或者ip为：" + url[:url.find('/')])
    print("请求地址为：" + url[url.find('/'):])





