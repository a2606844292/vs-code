#复习内容 3种方法
#number_list=[]
# number_list.append(1)
# number_list.append(2)
# number_list.append(3)
# for number in range(1,7):
#     number_list.append(number)
#print(number_list)
# number_list=list(range(1,7))
# print(number_list)

#列表推导式
#第一个number接收元素
# number_list=[number for number in range(1,7)]
# print(number_list)

#列表推导式加条件语句
number_list=[number*number if number %2==0 
                else number+10
                for number in range(1,7)]
print(number_list)