'''
参数
1.必须参数
2.关键词参数

'''


# def add(a, b):  # 形式参数 形参
#     result = a + b
#     return result
def add(a=2, b=3):  # 关键字参数
    result = a + b
    return result


c = add(a=3, b=2)  # 关键字参数
