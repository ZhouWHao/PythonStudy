def total(initial=5,*numbers,**keywords):
    count = initial
    for number in numbers:
        count+= number
    for key in keywords:
        count+= keywords[key]
    return count
print(total(10,1,2,3,vegetables=50,fruits=100))
#当我们定义一个带星的参数，像*param 时，从那一点后所有的参数被收集为一
#个叫做’param’ 的列表。多个无名参数全部放到*param列表中去，有名参数全部放到**param字典中去