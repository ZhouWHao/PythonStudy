#!/usr/bin/env python
num1 = 12
num2 = 15
while True:
    s = input('输入一些东西吧骚年:')
    if s == 'quit':
        break
    if len(s)<3:
        print('Too small')
        continue
    print('输入长度足够')
