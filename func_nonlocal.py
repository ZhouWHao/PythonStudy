def func_outer():
    x = 2
    print('x is',x)
    def func_inner():
        nonlocal x  #现在，我们在func_inner函数的顶部添加了nonlocal x语句。这个语句的作用，就是告诉Python解释器在碰到为x赋值的语句时，
                    # 应该向外层作用域的变量赋值，而不是声明一个重名的新变量。
        x = 5
    func_inner()
    print('Changed local x to',x)
func_outer()


#所以最后输出的结果为 x is 2
#                  Changed local x to 5