# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中一些零散的知识的案例

#加载模块中的函数时，可以用as取别名，来区分不同模块中的相同函数名
from math import sqrt as sqrtmath, sqrt

sqrtValue = sqrtmath(100)
print sqrtValue

#赋值的序列解包
# print打印不同类型时，用逗号隔开
value1,value2,string1 = 2,3,"wugang"
print value1, value2, string1

phoneBook = {"john": "1234", "smith": "0123", "judy": "7895"}
key, value = phoneBook.popitem()
print key, value

#解释器认为假值：False,None,0,"",(),[],{};其他都解释为真值
#pase语句做占位用
testName = "wugang"
name = testName
if "wugang" == name:
    print "wugang love bigdata"
else:
    pass

#exec代码用scope来限定作用域
scope = {}
exec 'sqrt = 1' in scope
print scope['sqrt'], sqrt(4), scope.keys()

#eval计算python表达式
evalValue = eval(raw_input("Enter an arithmetic expression:"))
print evalValue