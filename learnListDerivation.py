# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中列表推导式的案例

#列表推导式标准操作方法
a = [1,2,3,4,5,6,7,8,9,10]
list = [3*x for x in a]
print list
#加入if条件判断语句的列表推导式
evenNumber = [x for x in a if x % 2 == 0]
print evenNumber
#多个for语句列表推导;如果没有给定列表，也可以用range()方法
listSet = [[x, y] for x in a for y in range(10)]
print listSet

#找出2-50内的质数(素数)
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print "noprimes:", noprimes
print "primes:", primes

#嵌套列表降维
matrix = [[0,1,2,3], [4,5,6,7], [8,9,10,11]]
flatten = [i for row in matrix for i in row]
print "matrix:", matrix
print "flatten:", flatten

#模拟多个掷硬币事件(随机生成多个0-1)
from random import random
results = [int(round(random())) for x in range(10)]
print "results:", results

#移除句子中的元音字母
sentence = "wugang love bigdata!"
vowels = "aeiou"
nonvowles = [a for a in sentence if not a in vowels ]
nonvowlesString = ''.join(nonvowles)
print "nonvowels:", nonvowles
print "nonvowelsString:" + nonvowlesString