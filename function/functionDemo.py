# -*- coding: utf-8 -*-

def my_abs(x):
  if not isinstance(x, (int, float)):
    raise TypeError('bad operand type')
  if x >= 0:
    return x
  else:
    return -x

# 导入方法：在当前文件目录下执行：from abstest import my_abs
# abstest表示文件名（模块名）；my_abs表示函数名。