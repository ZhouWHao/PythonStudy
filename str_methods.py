#!/usr/bin/env python
'''
10.9 更多关于字符串的内容
我们已经在前面详细讨论了字符串。我们还需要知道什么呢？那么，你是否知道
字符串也是对象，同样具有方法。这些方法可以完成包括检验一部分字符串和去除空
格在内的各种工作。
你在程序中使用的字符串都是str 类的对象。这个类的一些有用的方法会在下面
这个例子中说明。如果要了解这些方法的完整列表，请参见help(str)。
例子：
'''
name='Swaroop'
if name.startswith('Swa'):
    print('Yes,the string starts with "Swa" ')
if 'a' in name:
    print('Yes,it contains the string "a" ')
if name.find('war')!=-1:
    print('Yes,it contains the string "war" ')
print(name.find('war'));
delimiter = '_*_'
mylist=['Brazil','Russia','India','China']
print(delimiter.join(mylist)) #通过字符串调用join方法来分割列表序列中的每一项
'''
它如何工作
这里，我们看到使用了许多字符串方法。startwith 方法是用来测试字符串是否以
给定字符串开始。in 操作符用来检验一个给定字符串是否为另一个字符串的一部分。
find 方法用来找出给定字符串在另一个字符串中的位置，或者返回-1 以表示找
不到子字符串。str 类也有以一个作为分隔符的字符串join 序列的项目的整洁的方法，
它返回一个生成的大字符串。
'''