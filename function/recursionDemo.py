# -*- coding: utf-8 -*-

# 一、传统递归
def fact(n):
  if n == 1:
    return 1
  return n + fact(n - 1)

print('1+2+3+4=', fact(4))
print('1+2+...+100=', fact(100))
print('---------------------------------------------')
# 二、尾递归
def fact2(n):
  return fact_iter(n, 1)

def fact_iter(num, product):
  if num == 1:
    return product
  return fact_iter(num - 1, num + product)
# 说明：尾递归是指：在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。强调：return返回的是函数本身，而不是表达式。
# 优点：尾递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
print('1+2+3+4=', fact2(4))
print('1+2+...+100=', fact2(100))

