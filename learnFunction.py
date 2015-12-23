# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中函数定义的案例

def fibs(num):
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result

number  = 10
result = fibs(number)
print result

#python中形参改变不会改变实参，如果想改变实参值，有两种方式
#1、重新赋值
def increment(number):
    return number + 1
foo = 10
incValue = increment(foo)
print foo
foo = increment(foo)
print foo
#用元组
foo = [10]
def increment(number):
    number[0] += 1
increment(foo)
print foo

#尽量避免使用位置参数和关键字参数
#关键字参数
def hello_parameter(name="wugang", greeting="Hello", punctuation="!"):
    print "%s, %s%s" %(greeting, name, punctuation)
hello_parameter()
hello_parameter(name = "yangjuan")

#可变参数，*收集其余的位置参数， **收集关键字参数
def print_parameter(parameter1, parameter2, *locationParameter, **keyParameter):
    print parameter1, parameter2
    print locationParameter
    print keyParameter
print_parameter("wugang", 32, 1, 2, "love", name = "wugang", greeting = "Hello")

#vars()返回全局变量的字典，globas获取全局变量的值，重绑定全局变量（global x）
#递归
#二分查找为例子
def search(sequence, number, lower, upper):
    if lower == upper:
        if number == sequence[upper]:
            return upper
        else:
            print "number %d is not inside sequence!" %number
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
             return search(sequence, number, lower, middle)

seq = [100, 20, 300, 35, 3, 27, 14, 234, 254]
seq.sort()
print seq
number = input("Enter the number you want to search:")
index = search(seq, number, 0, len(seq) - 1)
print index
