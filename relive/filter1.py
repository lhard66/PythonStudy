#!/usr/bin/env python
# -*- coding: utf-8 -*-

def _odd_iter():
  n = 1
  while True:
    n = n + 2
    yield n

def primes():
  yield 2
  it = _odd_iter() # 初始化序列
  while True:
    n = next(it)
    yield n
    # 构造新序列，是惰性的，使用next才计算获取序列的第一个值
    it = filter(lambda x: x % n > 0, it)

for n in primes():
  if n < 20:
    print(n)
  else:
    break