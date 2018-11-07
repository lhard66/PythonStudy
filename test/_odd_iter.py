# -*- coding -*-

def odd():
  n = 1
  while True:
    n += 2
    yield n

t = odd() # 需要先调用返回一个generator，然后再next

print(next(t))
print(next(t))
print(next(t))
print(next(t))