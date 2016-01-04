# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中文件操作的案例

#自动创建文件，写入字符串
file = open(r'F:\git_project\file.txt', 'r+')
file.seek(0)
file.write("Hello, ")
file.write("World!")
file.close()

# 读取字符
file = open(r'F:\git_project\file.txt', 'r')
fileString = file.read(4)
print "read String:", fileString
fileString = file.read(10)
file.close()
print "read String:", fileString

#seek设置文件指针偏移，tell返回当前文件指针位置
file = open(r'F:\git_project\file.txt', 'r+')
file.seek(6)
file.write("0123456")
fileLocation = file.tell()
file.close()
print "fileLocation:", fileLocation
file = open(r'F:\git_project\file.txt', 'r')
file.seek(3)
fileString = file.read()
print "read String:", fileString


#读取行
file = open(r'F:\git_project\file.txt', 'r')
fileLines = file.readlines()
print "fileLines:", fileLines
file.seek(0)
for i in range(len(fileLines)):
    print  str(i) + ":" + file.readline().strip("\n")
file.close()

#修改行
file = open(r'F:\git_project\file.txt', 'r')
fileLines = file.readlines()
file.close()
file = open(r'F:\git_project\file.txt', 'w')
fileLines[1] = "wugang love bigdata!\n"
file.writelines(fileLines)
file.close()
file = open(r'F:\git_project\file.txt', 'r')
fileLines = file.readlines()
print "fileLines:", fileLines
file.close()

