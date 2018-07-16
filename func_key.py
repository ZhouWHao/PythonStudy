#!/usr/bin/env python
def func(a,b=5,c=10):
    print('a is',a,'and b is',b,'and c is',c)
func(3,7)
func(25,c=24)
func(c=50,a=100)
#通过命名的方式来为参数赋值，被称为关键参数，不需要按照顺序来指定实参。

