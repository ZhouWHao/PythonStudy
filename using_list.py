#!/usr/bin/env python
shoplist = ['apple','mango','carrot','banana'];
print('I have',len(shoplist),'items to purchase.')
print('These items are:',end=' ')
#注意print 函数的end 关键参数来表示以空格结束输出，而不是通常的换行。
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
#从这行物理行我们才开始换的行，所以你会看到这样的效果
'''These items are: apple mango carrot banana 
   I also have to buy rice.'''
shoplist.append('rice')
print('My shopping list is now', shoplist)#输出列表内容，['apple', 'mango', 'carrot', 'banana', 'rice']

print('I will sort my list now')
shoplist.sort()#按26位英文字母排序
print('Sorted shopping list is', shoplist)#输出列表内容，['apple', 'banana', 'carrot', 'mango', 'rice']
print('The first item I will buy is', shoplist[0])#输出列表第一项 'apple'
olditem = shoplist[0] #Python 中从0 开始计算
del shoplist[0]  #移除这一项
print('I bought the', olditem)#删除第一项之后，之前被赋值的这个变量并不会受影响
print('My shopping list is now', shoplist)#第一项被删除后输出了['banana', 'carrot', 'mango', 'rice']

