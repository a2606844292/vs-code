#列表索引
A_list_of_things=['Hello',1,2,3,4,0,5.0,6.0,True,False]
#找到列表中索引值为0的值
print(A_list_of_things[0])
#找到倒数最后一个，从-1开始
print(A_list_of_things[-1])
print(len(A_list_of_things))
print(A_list_of_things[len(A_list_of_things)-1])

#列表切片
#从1开始切到2结束
print(A_list_of_things[1:3])
#从1开始切到3结束
print(A_list_of_things[1:4])
#从0开始切到7结束
print(A_list_of_things[0:7])
print(A_list_of_things[:7])
#从7开始到结尾
print(A_list_of_things[7:])
#列表和字符串的可变性
Hello='Hello hi~'
print(Hello[1])
list1=[1,2,3,4,5,6]
print(list1[1])
#修改列表里面第一个值
list1[0]='one'
print(list1)
Hello='Mello hi'
print(Hello)

#列表和字符串的可变性2
#xiaobai_said复制给xiaohei_said
xiaobai_said='Hello ,my name is xiaobai'
xiaohei_said=xiaobai_said
print(xiaohei_said)
#xiaobai_said修改值并不影响赋值内容
xiaobai_said='Hello ,my name is dabai'
print(xiaohei_said)
print(xiaobai_said)

#列表和字符串的可变性3
#列表赋值会跟随原值变化
score_card=['B','A','D','A','B','C']
score_card2=score_card
score_card[0]='C'
print(score_card)
print(score_card2)