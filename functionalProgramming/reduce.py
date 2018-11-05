# -*- coding: utf-8 -*-

# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。

from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def prod():
  return reduce(add, l)

def add(a, b):
  return a + b

print(prod())