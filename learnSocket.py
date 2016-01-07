# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中网络编程的案例

#urllib模块
from urllib import *

webpage = urlopen("http://www.qq.com")
#gb2312之至此简体中文，gbk支持简体繁体和日文假文
# text = webpage.read().decode('gb2312')
# UnicodeDecodeError: 'gb2312' codec can't decode bytes in position 142927-142928: illegal multibyte sequence
text = webpage.read().decode('gbk')
textUtf8 = text.encode("utf-8")
searchString = "QQ空间"
findIndex = textUtf8.find(searchString)
textFind = textUtf8[findIndex:findIndex+len(searchString)]
print textFind

#获取远程文件
saveName = "E:\git_project\learn_python\qq.html"
urlretrieve("http://www.qq.com", saveName)