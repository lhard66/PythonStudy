#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
  name1 = str.upper(name[0])
  name2 = str.lower(name[1:])
  return name1 + name2

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)