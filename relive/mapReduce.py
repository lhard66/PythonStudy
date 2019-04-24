#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
form functools import reduce
def str2float(s):


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')