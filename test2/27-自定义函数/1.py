#函数
#add为函数的名称，num1和num2是形参
#return返回值
def add(num1,num2):
    result=(num1+num2)*2
    print('I am Monkey Lufy')
    return result
#这里的2和8是实参
print(add(2,8))    

#自定义函数默认参数
def super_add(num1,num2,super_num3=10000):
    result=(num1+num2)*super_num3
    return result
#修改实参会改变默认值    
print(super_add(40,50,1))

#练习：贷款到期日拆分提醒
def remainder(days):
    years=days // 365
    months=(days %365)//30
    day_rem=(days % 365) %30
    return '{}year(s){}moth(s) and {}day remain'.format(years,months,day_rem)
print(remainder(957))
