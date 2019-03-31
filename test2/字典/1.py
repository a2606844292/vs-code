#字典
#字典中关于xiaobai的值
names={'xiaobai':'18','xiaohei':'19'}
print(names)
print(names['xiaobai'])

#字典get()
#用get方法找到key是否存在，存在的话将输出值，Python不会报错
print(names.get('xiaoming'))

#字典及恒等运算符
#判断x是否是None，返回布尔值
x=names.get('xiaoming')
print(x is None)
print(x is not None)

#字典get()自定义返回值
dic={'xiaobai':'18','xiaohei':'19'}
a=dic.get('xiaoming','此处添加自定义信息')
print(a)

#“=”，“==”，“is”辨析
#a 和 b 的值是完全相等的，返回true
a=[1,2,3,4,5,6,7,8]
b=a
print(a==b)
print(a is b)

#修改字典
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8;               # 更新 Age
dict['School'] = "教程"  # 添加信息
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#删除字典元素
dict1= {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#del dict1['Name'] # 删除键 'Name'
#dict1.clear()     # 清空字典
#del dict1        # 删除字典
print ("dict['Age']: ", dict1['Age'])

#补充
#items()方法语法：
dict2 = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
print("字典值 : %s" %  dict2.items()) 
# 遍历字典列表
for key,values in  dict.items():
    print (key,values)
