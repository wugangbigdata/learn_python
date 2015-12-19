#coding=utf-8
#python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
#container:sequence/map
#sequence:list,tuple
#这是一个学习序列操作的实例
#列表可以修改，元组则不能
sequenceNumbers = ['one', 'two', 'three', 'four', 'five', 1, 2, 3, 4, 5]
#索引操作
element = sequenceNumbers[3]
print element
#分片
segment = sequenceNumbers[2:7]
print segment
#从开始到第三个
startToThird = sequenceNumbers[:3]
print startToThird
#从倒数第三个到末尾
reverseThirdToEnd = sequenceNumbers[-3:]
print reverseThirdToEnd
#步长
stepElement = sequenceNumbers[::3]
print  stepElement
#步长为负数，为从右往左遍历
stepNegtive = sequenceNumbers[::-3]
print  stepNegtive
#加法，序列的连接(两种相同类型的序列才能连接)
sequenceName = ['wugang', "yangjuan", "xiaoming", "xiaoqiang"]
sequenceAdd = sequenceNumbers + sequenceName
print  sequenceAdd
#初始化10个元素的空列表
initNoneSequence = [None]*10
print  initNoneSequence
#in
flag = "wugang" in sequenceName
print  flag

#打印一个wugang love bigdata的盒子
sentence = '|'+" "*3 + "wugang love bigdata !"+" "*3 + '|'
spaceLength = len(sentence) - 2;
print "+"+"-" * spaceLength + "+"
print "|" + " " * spaceLength + "|"
print sentence
print "|" + " " * spaceLength + "|"
print "+"+"-" * spaceLength + "+"