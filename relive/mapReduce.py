#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
  # 1. 计算小数点位数
  # 2. map 遍历每个字符，将字符转为数值
  # 3. reduce 除小数点外，每个数值都要乘以10，加上累积数值。
  DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}

  # 生成数值
  def productNum(x, y):
    if y == '.':
      return x
    else:
      return x * 10 + y

  # 计算小数位数
  def getDotNum(str):
    times = 1
    for c in str:
      if c == '.':
        times = 1
      else:
        times = times * 10
    return times

  # 生成结果
  return reduce(productNum, map(lambda x: DIGITS[x], s)) / getDotNum(s)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')