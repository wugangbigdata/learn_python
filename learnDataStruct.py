# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中集合、堆和双端队列的案例

#集合,集合元素无序
#集合可变，集合元素不可变
from collections import deque
from heapq import *
from random import shuffle

list = [0, 1, 2, 3, 4, 0, 1, 2]
setNumber = set(list)
print setNumber

listString = ['wugang', 'love', 'bigdata']
setString = set(listString)
print setString

setUnion = setNumber.union(setString)
print setUnion

#堆
data = range(10)
print "data:",data
#打乱顺序
shuffle(data)
print "data:",data
heap = []
#最小堆
for e in data:
    heappush(heap, e)
print "heap:", heap

heappush(heap, 0.5)
print "heap:", heap
minElement = heappop(heap)
print "minElement:", minElement

#heapify将列表排列成最小堆
heapList = [3,2,1,10,2,5,6,7]
heapify(heapList)
print "heapList:", heapList

#双端队列
doubleQueue = deque(range(6))
print "doubleQueue:", doubleQueue
doubleQueue.append(4)
print "after append(4) doubleQueue:", doubleQueue
doubleQueue.appendleft(3)
print "after appendleft(3) doubleQueue:", doubleQueue
popElement = doubleQueue.pop()
print "popElement:", popElement
popElementLeft = doubleQueue.popleft()
print "popElementLeft:", popElementLeft
#头尾相连，右移3位
doubleQueue.rotate(3)
print "after rotate(3) doubleQueue:", doubleQueue
#头尾相连，左移2位
doubleQueue.rotate(-2)
print "after rotate(-2) doubleQueue:", doubleQueue



