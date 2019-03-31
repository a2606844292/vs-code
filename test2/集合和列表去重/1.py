#集合和列表去重
#使用set的方法去重复
place=['Beijing','Shanghai','Hangzhou','Guangdong''Beijing','Hangzhou']
print(len(place))
unique_place=set(place)
print(unique_place)


#判断值是否在列表里面
print('London' in unique_place)
print('Shanghai' in unique_place)
place.append('London')
print(place)

#集合add()pop()
#集合添加
number={1,2,3,4,5,6}
number.add(9)
print(number)
#集合为空默认取出1
number.pop()