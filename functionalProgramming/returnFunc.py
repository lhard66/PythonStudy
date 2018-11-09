# -*- coding: utf-8 -*-

# 如果不需要立刻求和，而是在后面的代码中，可以不返回求和的结果，而是返回求和的函数。

def calc_sum(*args):
  ax = 0
  for n in args:
    ax = ax + n
  return ax

def lazy_sum(*args):
  def sum():
    ax = 0
    for n in args:
      ax = ax + n
    return ax
  return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())