account = 'xiaobai'
password = '123456'

print('please input account:')
user_account = input()

print('please input password:')
user_password = input()

if account == user_account and password == user_password:
    print('success')
else:
    print('账号或密码出现错误')
