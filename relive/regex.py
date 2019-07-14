#!usr/bin/env python
# -*- coding: utf-8 -*-
import re

def is_valid_email(addr):
  return re.match(r'^[\w\d\.\-]+@[\w]+\.[\w]+$', addr)

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
print(is_valid_email('bob#example.com'))
print(is_valid_email('bob-mr@example.com'))
print('ok')