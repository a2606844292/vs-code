# 数量词
# *匹配0次或者无限多次
# +匹配1次或者无限多次
# ?匹配0次或者1次
import re


a = 'pytho0python1pythonn2'

# r = re.findall('python*', a)  # 匹配0次n
# r = re.findall('python+', a)  # 匹配1次n
r = re.findall('python?', a)  # 匹配0次或者1次n,多的n会去掉
print(r)
