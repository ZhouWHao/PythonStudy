#!/usr/bin/env python
def total1(initial=5, *numbers, vegetables):
    count = initial
    for number in numbers:
        count += number
    count += vegetables
    return count
print(total1(10, 1, 2, 3, vegetables=50))
# 在带星号的参数后面声明参数会导致keyword-only 参数报错。如果这些参数没有默认
# 值，且像上面那样不给关键参数赋值，调用函数的时候会引发错误。
# 如果你想使用keyword-only 参数，但又不需要带星的参数，可以简单地使用不使
# 用名字的空星，如def total(initial=5, *, vegetables)。
# 参数中有一个 “*” 号，在该符号之后的所有参数（可一至多个）均被称为强制关键字参数，
def total(initial=5,*,numbers,vegetables):
    print(initial,numbers,vegetables);
total(10,numbers=20,vegetables=30)