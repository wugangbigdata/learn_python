# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中random模块的案例
# import time
from random import *

from time import *

date1 = (2008, 1,1,0,0,0,-1,-1,-1)
time1 = mktime(date1)
print "time1:", time1
date2 = (2009, 1,1,0,0,0,-1,-1,-1)
time2 = mktime(date2)
print "time2:", time2

random_time = uniform(time1, time2)
print "random_time:", random_time
randomString = asctime(localtime(random_time))
print "randomString:", randomString

#投色子,计算总共投出骰子点数
num = input("How many dice?")
sides = input("How many sides per dice?")
sum = 0
for i in range(num):
    sum += randrange(sides) + 1
print "The result is ", sum
