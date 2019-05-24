# 数量词
# \d [0-9]数字字符 \D [^0-9]非数字字符
# \w 单词字符 \W 非单词字符
# \s 空白字符 \S非空白字符

import re


a = 'python 11\11java&678\php'

r = re.findall('[a-z]{3,6}', a)  # {}为数量词,匹配3-6个字符的字符串
print(r)
