#！/usr/bin/env python
'''
元组用来将多样的对象集合到一起。元组和列表十分类似，只不过元组和字符串
一样是不可变的即你不能修改元组。元
组通过圆括号中用逗号分割的项目定义。
元组通常用在使语句或用户定义的函数能够安全地采用一组值的时候，即被使用
的元组的值不会改变。
'''
zoo = ('python','elephant','penguin')
print('Number of animals in the zoo is',len(zoo))
new_zoo = ('monkey', 'camel', zoo)
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))

'''
它如何工作:
    变量zoo是一个元组，我们看到len函数可以用来获取元组的长度。这也表明元组也是一个序列。
    由于老动物园关闭了，我们把动物转移到新动物园。因此，new_zoo元组包含了一些已经在那里的
    动物和从老动物园带过来的动物。回到话题，注意元组之内的元组不会失去它的特性。
    我们可以通过一对方括号来指明某个项目的位置从而来访问元组中的项目，就像我们对列表的用法一样。
    这被称作索引运算符。我们使用new_zoo[2]来访问new_zoo中的第三个项目。我们使用new_zoo[2][2]
    来访问new_zoo元组的第三个项目的第三个项目。如果理解习惯的这相当简单
    圆括号:
    虽然圆括号是随意的,我更喜欢写出它使其明显地表明它是一个元组，尤其因为它会避免歧义。
    例如，print(1,2,3)和print((1,2,3))意义不同————前一个打印三个数字，而后一个打印出一个元组
    (包含三个数)。
含有0个或1个项目的元组:
    一个空的元组由一对空的圆括号组成，如myempty = ()。 然而，含有单个元素的元组就不那么简单了。
    你必须在第一个(唯一一个)项目后跟一个逗号，这样python才能区分元组和表达式中一个带圆括号的对象。
    即如果你想要的是一个包含项目2的元组的时候，你应该指明singleton=(2,)
给perl程序员的注释:
    列表之中的列表不会失去它的身份，即列表不会像Perl中那样被打散。同样元组中的元组，或列表中的元组，
    或元组中的列表等等都是如此，只要是python，它们就只是使用另一个对象存储的对象
'''
