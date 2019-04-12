#控制流：条件语句1
client=1000
bank=10000000
print('you have'+str(client)+'rmb'+'and you have'+str(bank)+'in bank')
#当你的余额少于2000元时，将在银行扣除1500加到余额里面
if client<2000:
    client+=1500
    bank-=1500
print('you have'+str(client)+'rmb'+'and you have'+str(bank)+'in bank')

#控制流：条件语句2
#判断people是否是Mary，当条件成立正常输出，如果不是将向下执行，全部都不满足就输出else的内容
people='Mary'
if people=='Mary':
    print('Hello-Mary-')
elif people=='Tom':
    print('Hello ton')
else:
    print('go away!')