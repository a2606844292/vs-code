# match和search
import re

s = '83C3721D8E67'

r = re.match('\d', s)  # 从字符串的首字母开始匹配，首字母不满足的话返回None
print(r.span())  # span方法将返回结果上的原位置
r1 = re.search('\d', s)  # 搜索整个字符串，直到找到这个字符串结束
print(r1.group())  # 把结果返回回来
r2 = re.findall('\d', s)
print(r2)
