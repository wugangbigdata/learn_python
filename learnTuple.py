#coding=utf-8
#python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
#学习元组序列

##有了列表后，为何又需要元组，元组有两个不可替代的作用：
##1：元组可以在映射中当做键使用
##2：元组作为很多内建函数和方法的返回值使用

#，逗号
tupleElement = (1,2,3,)
print tupleElement

#tuple()函数
listToTuple = tuple([1,2,3,'one','two'])
print listToTuple