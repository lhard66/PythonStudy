# -*- coding: utf-8 -*-

# 切片的几种用法
L = list(range(20))

print(L[0:3])
print(L[:3])
print(L[-3:])
print(L[:10:2])
print(L[:])
print('-----------------------------------------------')

# 字符串也可以使用切片
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])