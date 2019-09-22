#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/6'
username = "薛鹏垒"
phone = "18103909786"
certNo = "444555444888996359"
province="河南省"
city = "平顶山市"
status = 1
a = "insert into `t_cst_customer` (cst_name,phone,certNo,province,city,status) values('%s','%s','%s','%s','%s',%d);"%(username,phone,certNo,province,city,status)
print(a)
d = {"u":username,"c":certNo,"ci":city,"p":phone,"pr":province,"s":status}
b = "insert into `t_cst_customer` (cst_name,phone,certNo,province,city,status) values('{u}','{p}','{c}','{pr}','{ci}',{s});".format(**d)

print(b)

