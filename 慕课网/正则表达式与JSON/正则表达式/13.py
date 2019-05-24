import re
s = 'A83C3721D8E67'


def convert(value):
    matched = value.group()  # group匹配的整个表达式的字符串
    if int(matched) >= 6:
        return '9'
    else:
        return '0'


r = re.sub('\d', convert, s)
print(r)
