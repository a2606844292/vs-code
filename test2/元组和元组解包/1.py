#元组和元组解包
#输出place_1的第一个元素值
place_1=(1,2)
print('Longitude：',place_1[0])
print('Longitude：',place_1[1])
#元祖解包
dimensions=1,2,3
length,width,height=dimensions
print(length)
print(width)
print(height)

#元组和format介绍
print('The dimensions are:'+str(length)+'*'+str(width)+'*'+str(height))
print('The dimensions are:{0}*{1}*{2}'.format(length,width,height))
