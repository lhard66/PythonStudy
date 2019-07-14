#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

def name_of_email(addr):
  # 简单版
  m = re.match(r'^(<([\w\s]+)>\s+)?(\w+)@\w+\.\w+$', addr)

  # 复杂版
  # m = re.match(r'^(<([\w\d\s]+)>[\s]+)?([\w\d]+[\w\d\.]*)@([\w\d]+\.)+[\w\d]+$', addr)

  # print(m.group(1))
  # print(m.group(2))
  # print(m.group(3))

  if m.group(1):
    return m.group(2)
  elif m.group(3):
    return m.group(3)
  else:
    return None


# 测试:
# name_of_email('<Tom Paris> tom@voyager.org')
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')