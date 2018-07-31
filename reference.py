#!/usr/bin/env python
'''
引用
    当你创建一个对象并给它赋一个变量得时候，这个变量仅仅引用那个对象，而不是表示这个对象本身！
    也就是说，变量名指向你计算机中存储那个对象得内存。这被称作名称到对象的绑定
    一般说来，你不需要担心这个，只是在引用上有些细微的效果需要你注意。这会通过下面这个例子加以说明。
'''
print('Simple Assignment')
shoplist = ['apple','mango','carrot','banana']
mylist = shoplist #我的MyLIST只是指向另一个同样的对象！
del shoplist[0] #删除第一项
print('shoplist is',shoplist)
print('mylist is',mylist)
#这里引用的是同一个对象，所以删除原对象，第一项，引用该对象的也会受影响

print('Copy by making a full slice')
mylist = shoplist[:] # make a copy by doing a full slice
del mylist[0]
# 这里的删除并不会影响到原来的对象，
# 因为我们上面mylist得到的是shoplist列表的切片
print('shoplist is', shoplist)
print('mylist is', mylist)
'''
如何工作：
大多数解释已经在程序的注释中了。你需要记住的只是如果你想要复制一个列表
或者类似的序列或者其他复杂的对象（不是如整数那样的简单对象），那么你必须使
用切片操作符来取得拷贝。如果你只是想要使用另一个变量名，两个名称都引用同一
个对象，那么如果你不小心的话，可能会引来各种麻烦。
给Perl 程序员的注释：
记住列表的赋值语句不创建拷贝。你得使用切片操作符来建立序列的拷贝。
如果你只是想要使用另一个变量名，两个名称都引用同一
个对象，那么如果你不小心的话，可能会引来各种麻烦。
给Perl 程序员的注释：
记住列表的赋值语句不创建拷贝。你得使用切片操作符来建立序列的拷贝。
'''