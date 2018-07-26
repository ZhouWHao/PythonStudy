#!/usr/bin/env python
'''每个Python 模块都有它的__name__，如果它是’__main__’，这说明这个模块被
用户单独运行，我们可以进行相应的恰当操作。'''
if __name__ == '__main__':
    print('The program is being run by itself')
else:
    print('I am being imported from another module')

import using_name