#练习：客户列表中提取姓、名
#创建列表
#将names进行分隔后，将第一个元素统一小写，采用列表推导式
names=['xiao bai','Xiao ming','Jack MO','Mary Wang']
first_name=[name.split()[0].lower() for name in names]
last_name=[name.split()[1].lower() for name in names]
print(first_name)

#练习：信贷打分筛选简化运用
#name后面的是列表推导式，例如之前的for k,v in xxx.item(),后面就是判断条件
scores_card={'xiaobai':90,'Tom':80,'Kim':40}
passed=[name for name,score in scores_card.items() if score >=60]
print(passed)

