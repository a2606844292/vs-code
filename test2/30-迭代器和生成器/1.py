#enumerate() iterator迭代器 list[1,2,3,4,5,6,7] 列表为可迭代对象
#            generator生成器

#迭代器和数据流对象
list_1=[1,2,3,4,5,6,7,8,9]
# for i in enumerate(list_1):
#     print(i)
print(list(enumerate(list_1)))

#例二
list_2=['apple','bananan','fish','candy']
print(list(enumerate(list_2,1)))

#生成器生成迭代器
#yield为返回，每次只会返回一个值，将生成器和函数分开
def my_range(x):
    a=0
    while a<x:
        yield a
        a+=1
for x in my_range(20):
    print(x)        

#编写enumerate()
#1.定义一个列表
#2.定义一个生成器,将start赋值给count后进行迭代返回计数和列表的值后计数每次加一
#3.iterable为可迭代对象
# steps=['Python','Git','Deap','AI']
# def my_enumerate(iterable,start=0):
#     count=start
#     for element in iterable:
#         yield count,element
#         count+=1
# for i,step in my_enumerate(steps,1):
#     print('step{}:{}'.format(i,step))

#编写生成器对大数据进行拆分
def chunker(iterable,size):
        for i in range(0,len(iterable),size):   #从0开始-列表的长度，步长
                yield iterable[i:i+size]        #返回iterable的值，从i开始，i+size结束

for chunk in chunker(range(100),20):
        print(list(chunk))


