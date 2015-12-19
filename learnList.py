#coding=utf-8
#python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
#学习列表序列

#字符串变成字符列表
stringToList = list("wugang love bigdata!")
print stringToList
listToString = ''.join(stringToList)
print listToString

#列表元素赋值
stringToList[2] = "hate"
print stringToList
#删除
del stringToList[2]
print  stringToList
#强大的分片赋值操作,可以实现在列表中插入，替换，删除等动作
stringToList[6:11] = list("hate")
print stringToList

#apend方法在列表末尾追加新的对象
stringToList.append("very much")
print stringToList

#count统计某元素出现次数
charNumber = stringToList.count('a')
print  charNumber

#extend操作改变原列表，+操作产生一个全新的列表
listForExtend = [1,2,3,4,5]
stringToList.extend(listForExtend)
print  stringToList

#stringTolist太长了，删除一半元素
stringToList[len(stringToList)/3:len(stringToList)*2/3] = []
print stringToList

#index找出第一个匹配位置
indexForCharA = stringToList.index('a')
element = stringToList[indexForCharA]
print 'index[%d]:%s'%(indexForCharA, element)

#insert方法
insertElement = 'insert'
stringToList.insert(1, insertElement)
print  stringToList

#pop移除一个元素，并还回该元素的值
popElement = stringToList.pop(1)
print popElement

#remove移除某个值得第一个匹配项
stringToList.remove('a')
print stringToList

#reverse反向
stringToList.reverse()
print  stringToList

#sort将原列表就地排序，返回None
stringToList.sort()
print  stringToList