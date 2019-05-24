# group分组
import re

s = 'life is short,i use python,i love python'
# None
# r = re.search('life(.*)python', s)
r = re.search('life(.*)python(.*)python', s)
# r = re.findall('life(.*)python(.*)python', s)
# print(r.group(1))
print(r.group(0, 1, 2))
print(r.groups())  # 只返回括号括起来的内容
print(r.group(0))
print(r.group(1))
print(r.group(2))
# print(r)
