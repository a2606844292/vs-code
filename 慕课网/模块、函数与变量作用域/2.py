# 主要是用来遍历/循环 序列或者集合、字典

a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        if y == 'orange':  # 当y的值等于orange的时候会跳出列表的循环，而不影响元组的值
            break
        print(y)
else:
    print('fruit is gone')


# a = [1, 2, 3]
# for x in a:
#     if x == 2:
#         break  # break结束 continue跳过
#     print(x)
# else:
#     print('break结束不会输出else的内容')


# for循环嵌套
# items = [(1, 2), 3, "book", 3.14]
# tests = [100, (1, 2)]
# for k in tests:       # 先遍历第二个列表
#     for v in items:   # 再遍历第一个列表
#         if k == v:
#             print(k, "WAS FOUND!")
#     else:                               # 未找到处理方式
#         print(k, "NOT FOUND!")
