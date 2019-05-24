# 匹配模式参数
import re
lanuage = 'PythonC#\nC#\nJavaPHP'
# 4~8
r = re.findall('c#.{1}', lanuage, re.I | re.S)  # re.I忽略字母的大小写,加上re.S匹配到\n
print(r)
