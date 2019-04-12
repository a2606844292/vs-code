#fukter函数
#定义一个列表
#定义判断条件,返回字符串小于20
#fake_name为判断条件,names为可迭代的对象，在names列表中筛选
names=['xiaobai','Tom','Tommy','DDDDDDDDDdddddddddddddddddddd']

def fake_name(name):
    return len(name) <20
fake_name_list=list(filter(fake_name,names))
print(fake_name_list)