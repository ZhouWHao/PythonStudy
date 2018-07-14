#!/usr/bin/python
def printMax(a,b):
    if a>b:
        print(a,'是最大的值')
    elif a<b:
        print(b,'是最大的值')
    else:
        print(int(a)+'和'+int(b)+'是相同的')
printMax(100,100)