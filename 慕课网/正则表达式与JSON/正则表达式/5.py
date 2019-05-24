# 概况字符集
# \d [0-9]数字字符 \D [^0-9]非数字字符
# \w 单词字符 \W 非单词字符
# \s 空白字符 \S非空白字符
# .匹配除换行符\n之外其它所有字符

import re
a = 'python 11\11java&678\php'

# r = re.findall('\d', a)
# r = re.findall('[0-9]', a)
# r = re.findall('[^0-9]', a)  # 取反操作
# r = re.findall('\w', a)  # 匹配字母和数字
# r = re.findall('\W', a)
r = re.findall('\s', a)
print(r)
