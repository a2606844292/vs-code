import re


a = 'C0C|C++|C#|9Python6|Javascript'
r = re.findall('Python', a)
print(r)
# 规则
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')
