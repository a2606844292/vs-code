def PE(Price,Earning):
    '''
    calculate PE ratio

    INPUT:
    Price:int or float.The price of the stock you choose.
    Earning:int or float. The earning og the stock you choose.

    OUTPUT:
    PE:Price/Earing .The PE ratio of the stcok you choose.
    '''
    PE=Price/Earning
    return PE
print(PE(20,6))
#调出注释内容文档
print(PE.__doc__)