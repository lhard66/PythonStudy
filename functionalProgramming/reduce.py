# -*- coding: utf-8 -*-

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。

from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def prod():
  return reduce(add, l)

def add(a, b):
  return a + b

# print(prod())


# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

strNum = '123.456' # [1, 2, 3, ., 4, 5, 6]

def char2num(s):
  digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.': '.'}
  return digits[s]

def str2float(str):
  return reduce(makeNum, map(char2num, str))

def makeNum(a, b):
  if (b == '.'):
    isSign = True
    return a
  else:
    if (isSign == True):
      return a + b / 10
    else:
      return a * 10 + b

print(str2float(strNum))