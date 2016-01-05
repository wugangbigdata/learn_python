# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中fileInput模块的案例

# fileinput模块可以对一个或多个文件中的内容进行迭代、遍历等操作。该模块的input()函数有点类似文件
# readlines()方法，区别在于前者是一个迭代对象，需要用for循环迭代，后者是一次性读取所有行。
# 用fileinput对文件进行循环遍历，格式化输出，查找、替换等操作，非常方便

# fileinput.input()       #返回能够用于for循环遍历的对象
# fileinput.filename()    #返回当前文件的名称
# fileinput.lineno()      #返回当前已经读取的行的数量（或者序号）
# fileinput.filelineno()  #返回当前读取的行的行号
# fileinput.isfirstline() #检查当前行是否是文件的第一行
# fileinput.isstdin()     #判断最后一行是否从stdin中读取
# fileinput.close()       #关闭队列

# 利用fileinput读取一个文件所有行
import fileinput

import sys

argc = len(sys.argv)
if argc >= 2:
    filename = sys.argv[1]
else:
    filename = "E:\\git_project\\learn_python\\file.txt"
for line in fileinput.input(filename):
    print line.strip('\n')

print '\n'
for line in fileinput.input(filename):
    print fileinput.filename(),'|','Line Number:',fileinput.lineno(),'|: ',line.strip('\n')