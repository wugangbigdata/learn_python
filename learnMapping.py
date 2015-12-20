# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习映射操作的实例
# 1、键可以为任何不可变类型

# 一些字典比列表更适用的场合
# 1、表征游戏棋盘的状态，每个键都是由棋盘坐标值组成的元组
# 2、存储文件修改次数，用文件名作为键
# 3、数字电话/地址薄

# 初始化一个字典
from copy import deepcopy

phoneBook = {"john": "1234", "smith": "0123", "judy": "7895"}
print phoneBook
items = [("name", "wugang"), ("age", "28")]
person = dict(items)
print person

# 字典的格式化字符串
template = """<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>
"""
data = {"title": "My Home Page", "text": "wugang love bigdata!"}
htmlText = template % data
print htmlText

# 字典方法
# clear,就地清空字典
phoneBook.clear()
print phoneBook
# copy，潜复制,不是全部保存为副本，类似于C中的指针值复制了，但是指针指向的内容没有被复制
person["score"] = ['30', '89', '66', '100']
personCopy = person.copy()
personCopy["name"] = "xiaoming"
personCopy["score"].remove('30')
print personCopy
#改变值，原字典不变，改变值序列中的元素，原字典也改变
print person
# deepCopy,深复制,全部都有副本，对副本的修改不会改变原字典内容
personDeepCopy = deepcopy(person)
personDeepCopy["name"] = "john"
personDeepCopy['score'].append('90')
print personDeepCopy
print person
#fromkeys 使用给定的键建立新的字典
fromkeysDict = dict.fromkeys(["name", "age", "class", "score"])
print fromkeysDict
#get,访问不存在的键，返回None
value = person.get("name")
valueUnkownKey = person.get("haha")
print "'name':%s"%value + "  'haha':%s"%valueUnkownKey
#has_key ,python3中无该函数
keyTrue = person.has_key("name")
keyFalse = person.has_key("haha")
print "has key 'name':%s"%keyTrue + "  has key 'haha':%s"%keyFalse
#iterms和iteritems
personList = person.items()
print personList
personIter = person.iteritems()
personIterList = list(personIter)
print personIter
print personIterList
#keys将键以列表形式返回，iterkeys则返回键的迭代器
personKeysList = person.keys()
print personKeysList
personKeysIter = person.iterkeys()
print personKeysIter
personKeysIterList = list(personKeysIter)
print personKeysIterList
#values将值以列表形式返回，itervalues则返回值的迭代器
personValuesList = person.values()
print personValuesList
personValuesIter = person.itervalues()
print personValuesIter
personValuesIterList = list(personValuesIter)
print personValuesIterList
#pop移除键值对，返回值为键对应的值
personCopyForPop = deepcopy(person)
popName = personCopyForPop.pop("name")
print popName
print person
print personCopyForPop
#popitem随机弹出一项
randomPop = personCopyForPop.popitem()
print randomPop
#setdefault,返回给定键的值，如果没有键，则返回默认值，同时将改键值对添加到字典
setDefaultValue = person.setdefault("bigdata", "good")
print setDefaultValue
print person
#updata用一个字典项更新另外一个字典项,相同的键则覆盖，新键则添加
updatePerson = {"bigdata":"bad", "course":["dataMining", "math", "english"]}
person.update(updatePerson)
print person
