# -*- coding: utf-8 -*-

def triangles():
  row1 = [1]
  while True:
    yield(row1)
    row1, row2 = row1 + [0], [0] + row1
    for i in range(len(row1)):
      row1[i] += row2[i]

def triangles2():
  row = [1]
  while True:
    yield(row)
    row = [1] + [row[k] + row[k + 1] for k in range(len(row) - 1)] + [1]

def show1():
  n = 0
  for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
      break

def show2():
  g = triangles2()
  for t in range(10):
    print(next(g))

show2()
