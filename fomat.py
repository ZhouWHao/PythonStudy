#!/usr/bin/env python
#Filename: fomat.py
age = 20
name="小明"
i = 50
s = '''This is a multi-line string.
7 This is the second line.'''
print(i+1)
print(s)
#优势，转为字符串无需写上数据类型转换方法，format方法自动完成
print("{0}今年{1}岁了。".format(name,age))
print(name + ' is'+str(age)+' years old')

#python只有两种基本数据类型，那就是数字和字符串这两种。