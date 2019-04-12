# msg=input('Please enter your name:.....')
# print('Welcome'+msg)

# num=int(input('Enter a number....'))
# num+=10
# print(num)

#处理错误和异常
#如果try无法执行的话，会执行下面语句
while True:
    try:
        x=int(input('Enter a number please:'))
        break
    except:
        print('That is not a number')
    finally:
        print('You have enter a number.')




