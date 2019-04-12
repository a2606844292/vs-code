stock_prince=[1,4,6,9,5,3,7,4,8]
print(len(stock_prince))
#最大值
print(max(stock_prince))
#最小值
print(min(stock_prince))
#重复的会并列在一起
print(sorted(stock_prince))
#列表倒过来
print(sorted(stock_prince,reverse=True))
card=['a','b','c','d','e','f','c','a']
print(sorted(card))
print(sorted(card,reverse=True))

#列表方法join
#加入\n会替换掉, 然后进行换行
a=['A','B','C','D','E']
b='\n'.join(a)
print(b)
c='---'.join(a)
print(c)

#列表方法append
#将Tom追加到列表的末尾
name=['xiaobai','xiaohei','dabai','xiaoming']
name.append('Tom')
print(name)