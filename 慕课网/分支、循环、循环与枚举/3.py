#a = x
# a = 1 print('apple')
# a = 2 print('orange')
# a = 3 print('banana')

a = int(input('请输入数字:'))  # 转换成int数字类型
#print('a is' + a) //测试代码
print(type(a))
if a == 1:
    print('apple')
elif a == 2:
    print('banana')
elif a == 3:
    print('orange')
else:
    print('shopping')
