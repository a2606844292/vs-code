# 字符集
import re
s = 'abc,acc,adc,aec,afc,ahc'

# r = re.findall('a[^cfd]c', s)
r = re.findall('a[c-f]c', s)
print(r)
# 普通字符加上元字符，a,c为普通字符定界，[]中为包含的条件,或
# ^匹配的是不包含的字符，取反
