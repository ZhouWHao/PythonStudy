#!/user/bin/python

number = 23
running = True
while running:
    guess = int(input("输入一些整数吧骚年："))
    if guess == number:
        print("你输入的整数正好等于我们预先准备的number")
        running = False
    elif guess > number:
        print("你输入的整数正好大于我们预先准备的numebr")
    else:
        print("你输入的整数正好小于我们预先准备的numebr")
else:
    print("结束while循环结束")
print("done")