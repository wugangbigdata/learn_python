# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中文件操作的案例
import sys

#自动创建文件，写入字符串
argc = len(sys.argv)
if argc >= 2 :
    print "argv[0]:%s, argv[1]:%s"%(sys.argv[0], sys.argv[1])  #用参数输入文件名
    filename = sys.argv[1]
else:
    filename = "E:\\git_project\\learn_python\\file.txt"
# filename = raw_input("Input the fileName:")  #输入文件名
print "filename:", filename
file = open(filename, 'r+')
file.seek(0)
file.write("Hello, ")
file.write("World!")
file.close()

# 读取字符
file = open(filename, 'r')
fileString = file.read(4)
print "read String:", fileString
fileString = file.read(10)
file.close()
print "read String:", fileString

#seek设置文件指针偏移，tell返回当前文件指针位置
file = open(filename, 'r+')
file.seek(6)
file.write("0123456")
fileLocation = file.tell()
file.close()
print "fileLocation:", fileLocation
file = open(filename, 'r')
file.seek(3)
fileString = file.read()
print "read String:", fileString


#读取行
file = open(filename, 'r')
fileLines = file.readlines()
print "fileLines:", fileLines
file.seek(0)
for i in range(len(fileLines)):
    print  str(i) + ":" + file.readline().strip("\n")
file.close()

#修改行
file = open(filename, 'r')
fileLines = file.readlines()
file.close()
file = open(filename, 'w')
fileLines[1] = "wugang love bigdata!\n"
file.writelines(fileLines)
file.close()
file = open(filename, 'r')
fileLines = file.readlines()
print "fileLines:", fileLines
file.close()

#d对文件内容进行迭代
#按字节处理
file = open(filename, 'r')
char = file.read(1)
wordList = list()
while char:
    wordList.append(char)
    char = file.read(1)
file.close()
print "wordList:", wordList

#文件迭代器
file = open(filename)
lineNumber = 1
for line in file:
    print "lineNumber:", lineNumber, '|', line.strip()
    lineNumber += 1

