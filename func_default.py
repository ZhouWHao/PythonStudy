#!/usr/bin/env python
def say1(message,times =1):
    print(message * times)
say1('Hello')
say1('World',5)
def say2(message,times1 =2,times =2):
    print(message * times * times1)
say2('World')

def say3(times1 =2,times2 =2,times =2):
    print(times1 * times2 * times)
say3('123')

#在给形参里面设置默认参数值的时候，所有默认参数值只能放在没有默认值参数的后面,否则会报语法错误


