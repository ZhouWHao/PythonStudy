#!/usr/bin/env python
def printMax(x,y):
    '''Prints the maximum of two numbers.

    The two values must be integers'''
    x = int(x)#convert to integers,if possible
    y = int(y)

    if x > y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')
printMax(3,5)
print(printMax.__doc__)#获取printMax函数的文档属性
help(printMax)#通过help函数获取printMax函数的函数名以及参数和文档属性