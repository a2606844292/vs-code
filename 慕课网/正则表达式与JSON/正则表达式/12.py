# re.sub正则替换
import re
lanuage = 'PythonC#JavaPHPC#C#'


def convert(value):
    matcher = value.group()  # group匹配的整个表达式的字符串
    # print(value)
    return '!!'+matcher+'!!'


r = re.sub('C#', convert, lanuage)

# r = re.sub('C#', 'Go', lanuage, 0)  # 字符串的替换,0为无限替换，默认为0
# lanuage = lanuage.replace('C#', 'Go')  # 内置函数，简单的替换
# pattern正则表达式,repl被替换参数,string被搜索的原字符串，count替换次数，flag匹配模式
print(r)
