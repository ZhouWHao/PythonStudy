#!/usr/bin/env python
class Person:
    def sayHi(self):
        print('Hello, how are you?')

p = Person()
p.sayHi()
'''
如何工作：
这里我们看到了self 的用法。注意sayHi 方法没有任何参数，但仍然在函数定义
时有self。
'''