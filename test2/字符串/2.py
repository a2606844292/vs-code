given_name='xiaobai'
middle_name='D'
family_name='Monkey'
#判断name_length是否小于或者等于name_charcter_limt的长度
name_length=len(given_name+middle_name+family_name)
name_charcter_limt=15
print(name_length<=name_charcter_limt)
#如果在后面修改赋值需要重新执行
middle_name='DDDDDDD'
name_length=len(given_name+middle_name+family_name)
print(name_length<=name_charcter_limt)