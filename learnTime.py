# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中time模块的案例
import time

timeString = time.asctime()
print "time:", timeString
timeSecond = time.time()
print "second:", timeSecond
timeTuple = time.localtime(timeSecond)
print "timeTuple:", timeTuple
timeSecond = time.mktime(timeTuple)
print "second:", timeSecond
timeTuple = time.strptime(timeString)
print "timeTuple:", timeTuple
