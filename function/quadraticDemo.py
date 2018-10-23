# -*- coding: utf-8 -*-

# 解一元二次方程

import math

def quadratic(a, b, c):
  # x = (-b +或- 根号(b*b - 4ac)) / 2a
  radical = b * b - 4 * a * c

  if (radical < 0):
    print('无解')
    return
  else:
    x1 = (-b + math.sqrt(radical)) / (2 * a)
    x2 = (-b - math.sqrt(radical)) / (2 * a)
    return x1, x2