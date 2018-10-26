# -*- coding: utf-8 -*-

# 列表生成式
# 请个性列表生成式，通过添加if语句保证列表生成式能正确执行。

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]

print(L2)