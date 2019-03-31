#默认为空格
a='My name is xiaobai.'
b=a.split()
print(b)
c='My\nname\nis\nxiaobai'
d=c.split()
print(d)
e='My\tname\tis\txiaobai'
f=e.split()
print(f)
g='My,name ,is ,xiaobai.'
h=g.split(',')
print(h)
#通过%切割
i='M%yna%me is xiaobai.'
j=i.split('%')
print(j)
#split()有两个参数
#1表示在有空格的地方切一刀
long_string='My name is Monkey Dlufy.The man who is going to be the king'
b1=long_string.split(' ',1)
print(b1)