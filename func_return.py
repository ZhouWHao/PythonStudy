#!/usr/bin/env python
def maximum(x,y):
    if x>y:
        return x
    else:
        return y
print(maximum(2,3))

def someFunction():
    pass

print(someFunction())  #python的函数都在结尾暗含有return None,默认返回None
print(max(2,3)) #如果内置函数能实现同样功能的话，尽量使用内置函数，不要自己去手写。