#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
	args = sys.argv
	if len(args)==1:
		print('Hello, world!')
	elif len(args)==2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')
		
if __name__=='__main__':
	test()
	
	
#第 1 行和第 2 行是标准注释，第 1 行注释可以让这个 hello.py 文件直接在 Unix/Linux/Mac 上运行，
#第 2 行注释表示.py 文件本身使用标准 UTF-8编码；
#第 4 行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
#第 6 行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

#以上就是 Python 模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错

#最后，注意到这两行代码：
#if __name__=='__main__':
#	test()
#当我们在命令行运行 hello 模块文件时， Python 解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该 hello 模块时， 
#if 判断#将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。