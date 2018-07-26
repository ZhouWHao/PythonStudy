#!/usr/bin/env python
import sys
print('The command line arguments are:')
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is',sys.path,'\n')
'''首先，用导入了sys 模块。基本上，这句语句告诉Python ，我们想要使用这个模
块。sys 模块包含了与Python 解释器和它的环境有关的函数。
当Python 执行import sys 语句的时候，它会寻找sys 模块。在这个例子中，它是
内置模块，因此Python 知道在哪里找到它。'''