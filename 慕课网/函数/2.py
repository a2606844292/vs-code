'''
    1.参数列表可以没有
    2.return value None
'''


def add(a, b):  # 形参
    result = a + b
    return result


def print_code(code):
    print(code)
    return None  # 无返回值


def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill2*2+10
    return damage1, damage2


print(add(1, 2))  # 实际参数 实参
print_code('Python')


# damage = damage(3,6)
# print(damage[0], damage[1])  # 不建议这样写
# print(type(damage))

skill1_damage, skill2_damage = damage(3, 6)
# 序列解包
print(skill1_damage, skill2_damage)
