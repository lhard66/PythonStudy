# -*- coding: utf-8 -*-

# 一、位置参数
def power(x, n = 2):
  s = 1
  while n > 0:
    n = n - 1
    s = s * x
  return s

print('位置参数：', power(2, 3))
print('--------------------------------------------------------------------')
# 说明：
# 一是必选参数在前，默认参数在后，否则python的解释器会报错。
# 二是如何设置默认参数

# 技巧：
# 1. 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 2. 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 二、可变参数
def calc(*numbers):
  sum = 0
  for n in numbers:
    sum = sum + n * n
  return sum

nums = [1, 2, 3]
print('可变参数：', calc(nums[0], nums[1], nums[2]))
print('可变参数：', calc(*nums))
print('--------------------------------------------------------------------')

# 三、关键字参数
def person(name, age, **kw):
  print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing')
extra = { 'city': 'Beijing', 'job': 'Enginner' }
person('Jack', 24, **extra)
print('--------------------------------------------------------------------')
# 注意：
# kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

# 四、命名关键字参数（作用：限制传入关键字参数的类型）
def person2(name, age, *, city = 'Tianjing', job):
  print(name, age, city, job)

person2('Jack', 24, city='Beijing', job='Enginner')
person2('Jack', 24, job='Enginner') # 由于命名关键字参数city具有默认值，调用时，可不传入city参数
print('--------------------------------------------------------------------')

# 说明：和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

# 总结：
# 参数顺序：参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 注意：
# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差！