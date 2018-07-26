#!/usr/bin/env python
__version__='0.1.2'
import mymodule
mymodule.sayhi()
print('Version',__version__)#当前模块的__version__
print('Version',mymodule.__version__)
#注意我们使用了相同的点号来使用模块的成员。Python 很好地重用了相同的记号
#来，使我们这些Python 程序员不需要不断地学习新的方法。
#下面是一个使用from..import 语法的版本。
from mymodule import sayhi,__version__
sayhi()
print('Version',__version__)
#如果我们在当前模块再创建一个__version__就会发生冲突了
'''注意如果已经在导入mymodule 的模块中申明了一个__version__ 的名字，这就
会有冲突。这也是有可能的，因为从实际情况来看，每个模块会用这个名字来申明它
的版本。因此，推荐选择使用import 语句，虽然会导致程序稍微有点冗长。
你也可以这样使用：'''
print('------')
from mymodule import *
sayhi()
print('Version',__version__)