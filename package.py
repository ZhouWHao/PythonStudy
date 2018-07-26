#!/user/bin/env python
'''
到目前为止，你一定已经开始看到了组织你的程序的层次。变量通常在函数内部
运行。函数和全局变量通常在模块内部运行。如果你想自己组织模块呢？那" 包" 就
会进入到你的视野中。
包是模块的文件夹，有一个特殊的__init__.py 文件，用来表明这个文件夹是特殊
的因为其包含有Python 模块。
加入你想创建一个叫做’world’ 的包，有子包’asia’,’africa’ 等等，并且，这些子包
又包含模块，如’india’,’madagascar’ 等等。
这就是你像构造的文件夹：
- <some folder present in the sys.path>/
    - world/
        - __init__.py
        - asia/
             __init__.py
             - india/
                 - __init__.py
                 - foo.py
             - africa/
                 - __init__.py
                 - madagascar/
                     -__init__.py
                     - bar.py
'''
#包仅仅是为了方便层次化地组织模块。你会看到在标准库中看到许多这样的实例。
#就像函数是在程序块中能在利用一样，模块是可在利用的程序。包是另一个组织
#模块的层次。伴随Python 的标准库是这样一个包集和模块的例子。
