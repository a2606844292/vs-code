#map(定义的函数,列表)
#把列表的每一个元素都进行调用square函数
#map返回的是迭代器，所以要转换成list
def square(x):
    return x**2
list_1=[1,2,3,4,5,6,7,8,9]

a=map(square,list_1)
print(list(a))

#高阶内置函数map()地区平均信用质量
score_cards=[[1,2,3,4,5,3,4,1,2,4],[6,5,7,6,5,6,7,6,5,5],[9,10,8,10,8,10,9,8,6,10]]
# def mean(score_list):
#     return sum(score_list) / len(score_list)
# average_score=list(map(mean,score_cards))
# print(average_score)

#地区平均信用质量lambda简化
#x为可变参数，执行相加后除于列表的长度得到平均值，score_cards为迭代对象
average_score=list(map(lambda x:sum(x)/len(x),score_cards))
print(average_score)