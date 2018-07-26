#!/usr/bin/env python
ab = {
    'swaroop':'123@qq.com',
    'wwaroop':'456@qq.com',
    'awaroop':'789@qq.com',
    'bwaroop':'101112@qq.com',
}
print("swaroop's address is",ab['swaroop'])
del ab['swaroop']
print('\n删除掉swaroop键值对后，这个字典的长度为{0}\n'.format(len(ab)))

print(ab.items())
for name,address in ab.items():
    print('键{0}和值{1}'.format(name,address))

ab['wwaroop'] = 'zhouwh@qq.com'
if 'wwaroop' in ab: #或者使用ab.has_key('wwaroop')
    print("wwaroop的邮箱为",ab['wwaroop'])
print(ab);
'''
如何工作：
    我们使用已经介绍过的标记创建了字典ab。然后我们使用在列表和元组章节中
    已经讨论过的索引操作符来指定键，从而使用键/值对。我们可以看到字典的语法同
    样十分简单。
    我们可以使用索引操作符来寻址一个键并为它赋值，这样就增加了一个新的
    键/值对，就像在上面的例子中我们对wwaroop 所做的一样。
    我们可以使用我们的老朋友|——del 语句来删除键/值对。我们只需要指明字典
    和用索引操作符指明要删除的键，然后把它们传递给del 语句就可以了。执行这个操
    作的时候，我们无需知道那个键所对应的值。
    接下来，我们使用字典的items 方法，来使用字典中的每个键/值对。这会返回一
    个元组的列表，其中每个元组都包含一对项目—— 键与对应的值。我们抓取这个对，
    然后分别赋给for..in 循环中的变量name 和address 然后在for －块中打印这些值。
    我们可以使用in 操作符来检验一个键/值对是否存在，或者使用dict 类的has_key
    方法。你可以使用help(dict) 来查看dict 类的完整方法列表。
关键字参数与字典:
    如果换一个角度看待你在函数中使用的关键字参数的话，你已经使用了字典了！
    只需想一下————你在函数定义的参数列表中使用的键/值对。当你在函数中使用
    变量的时候，它只不过是使用了一个字典的键(这在编译器设计的术语中被称作符号表)。
'''