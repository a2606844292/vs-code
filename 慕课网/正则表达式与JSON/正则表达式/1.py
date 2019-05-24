import re


a = 'C|C++|C#|Python|Javascript'
r = re.findall('Python', a)
print(r)
# 规则
if len(r) > 0:
    print('字符串中包含Python')
else:
    print('No')

# 内置查找函数方法
# print(a.index('Python') > -1)
# print('Python' in a)
