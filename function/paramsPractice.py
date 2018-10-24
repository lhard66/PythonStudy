# -*- coding: utf-8 -*-

# 函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个个并计算乘积

def product(x, *numbers):
  for n in numbers:
    x = x * n
  return x

print(product(3, 5))
print(product(1, *[2, 3, 4, 5]))