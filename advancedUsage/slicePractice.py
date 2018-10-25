# -*- coding: utf-8 -*-

#...hello
#hello...
#   hello   

def trimLine(s):
  while s[:1] == '-':
    s = s[1:]
  while s[-1:] == '-':
    s = s[:-1]
  return s

print(trimLine('---hello'))
print(trimLine('hello---'))
print(trimLine('---hello---'))