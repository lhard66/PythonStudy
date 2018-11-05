# -*- coding: utf-8 -*-
from functools import reduce
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456

strNum = '12388.456123'

# 检查数据合法性，获取小数点分割的两个字符串
def getSplitStr(str):
  splitStr = str.split('.')
  if (len(splitStr) == 2 and splitStr[0] != '' and splitStr[1] != ''):
    return splitStr
  else:
    return None

# 将单个字符类型转换为数字类型
def char2num(key):
  DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
  return DIGITS[key]

# 将一个字符串转转换为数字
def string2num(str):
  return reduce(lambda x, y: x * 10 + y, map(char2num, str))

# 计算小数点的倍数，返回一个10的倍数
def getBaseNum(str):
  baseNum = 1
  for t in range(str.find('.')):
    baseNum *= 10
  return baseNum

# 开始方法，字符串转浮点数
def str2float(str):
  splitStr = getSplitStr(str)
  if (splitStr == None):
    print('error str')
    return
  else:
    intNum = string2num(splitStr[0])
    decimalNum = string2num(splitStr[1])
    return intNum + decimalNum / getBaseNum(str)

print(str2float(strNum))
print(str2float(strNum) + 1) # +1 测试是否成功
