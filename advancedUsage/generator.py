# -*- coding: utf-8 -*-

# generator的演变
# 使用场景：当一个List有很多个元素，而这些元素是可以通过计算得到的，此时可以使用generator。
# 例如：[1, 2, 3, 5, 8, 13, 21, ...]这个list是前后者是前两个的和。

# generator的演变过程

# 斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    print(b)
    a, b = b, a + b
    n = n + 1
  return 'done'

fib(10)
print('------------------------------')

# 注意：
# a, b = b, a + b
# 相当于
# t = (b, a + b) t是一个tuple
# a = t[0]
# b = t[1]

# 变为generator的方法：
# 只需将print(b)改为yield b

def fib2(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n = n + 1
  return 'done'

print(fib2(10))
print('------------------------------')
for n in fib2(10):
  print(n)

# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。