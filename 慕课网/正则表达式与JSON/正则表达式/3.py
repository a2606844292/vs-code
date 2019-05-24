import re


a = 'C0C|C++|C#|9Python6|Javascript'

r = re.findall('\D', a)  # \d可以表示数字1-9 \D匹配一个非数字字符
print(r)

'''
python'普通字符 '\d'元字符    
'''
