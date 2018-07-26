#!/usr/bin/env python
#列表、元组和字符串都是序列
'''
序列的主要特点是索成员检验（例如，在和不在表达式中）和索引操作符，索引
操作符让我们可以直接从序列中抓取一个特定项目。
'''
shoplist = ['apple','mango','carrot','banana']
name = 'swaroop'

print('Item 0 is',shoplist[0]) #取索引
print('Item 1 is',shoplist[1]) #取索引
print('Item 2 is',shoplist[2]) #取索引
print('Item 3 is',shoplist[3]) #取索引
print('Item -1 is',shoplist[-1]) #取索引最后一个
print('Item -2 is',shoplist[-2])#取索引倒数第二
'''
索引同样可以是负数，在那样的情况下，位置是从序列尾开始计算的。因此，
shoplist[-1] 表示序列的最后一个元素而shoplist[-2] 抓取序列的倒数第二个项目。
'''
print('Character 0 is',name[0]) #取字符串第一位

#截取列表
print('characters 1 to 3 is',name[1:3])
print('characters 2 to end is',name[2:])
print('characters 1 to 3 is',name[1:-1])
print('Item start to end is',shoplist[:])

#截取字符串
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
'''
切片操作符是序列名后跟一个方括号，方括号中有一对可选的数字，并用冒号分
割。注意这与你使用的索引操作符十分相似。记住数是可选的，而冒号是必须的。
切片操作符中的第一个数（冒号之前）表示切片开始的位置，第二个数（冒号之
后）表示切片到哪里结束。如果不指定第一个数，Python 就从序列首开始。如果没有
指定第二个数，则Python 会停止在序列尾。注意，返回的序列从开始位置开始，刚
好在结束位置之前结束。即开始位置是包含在序列切片中的，而结束位置被排斥在切
片外。
这样，shoplist[1:3] 返回从位置1 开始，包括位置2，但是停止在位置3 的一个序
列切片，因此返回一个含有两个项目的切片。类似地，shoplist[:] 返回整个序列的拷
贝。
你可以用负数做切片。负数用在从序列尾开始计算的位置。例如，shoplist[:-1] 会
返回除了最后一个项目外包含所有项目的序列切片。
你也可以给切片规定第三个参数，就是切片的步长（默认步长是1）。
'''
shoplist = ['apple','mango','carrot','banana']
print(shoplist[::1]) #得到全部
print(shoplist[::2]) #得到0和2的位置
print(shoplist[::3]) #得到0和3的位置
print(shoplist[::-1])#得到数组倒序，从最后一位开始往前取
'''
注意当步长是2 时，我们得到在位置0,2,... 的项，当步长是3 时，得到位置0,3,
等等的项。
使用Python 解释器交互地尝试不同切片指定组合，即在提示符下你能够马上看
到结果。序列的神奇之处在于你可以用相同的方法访问元组、列表和字符串！
'''


#集合
'''
    集合是没有顺序的简单对象的聚集。当在聚集中一个对象的存在比其顺序或者出现的次数重要时使用集合
    使用集合，可以检查是否是成员，是否是另一个集合的子集，得到两个集合的交集等等。
    简单理解就是不需要考虑数据唯一性和数据顺序的时候我们应该尽量使用集合来存储我们的数据    
'''
bri = set(['brazil','russia','india'])
print('india' in bri) #字符串india存在于bri集合中返回True
print('usa' in bri)#字符串usa不存在于bri集合中返回False
bric = bri.copy()  #复制集合给另一个变量
bric.add('china')  #给新集合添加字符串项
print(bric.issuperset(bri)) #判断bric是否是bri的超集
bri.remove('russia')#删除bri集合中的russia
print(bric) #{'russia', 'brazil', 'india', 'china'}
print(bri)  #{'india', 'brazil'}
print(bri & bric)  #得到两个集合得交集{'brazil', 'india'}