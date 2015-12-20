#coding=utf-8
#python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
#这是一个学习字符串操作的实例，字符串是不可改变值的
#单引号字符串操作
from math import pi
from string import Template
from stringold import maketrans

singleQuotation = 'wugang love "bigdata" !'
print singleQuotation
#双引号字符串操作
doubleQutation = "wugang love 'bigdata' !"
print doubleQutation
#三引号操作，一般用于长字符串，需要分多行
triQutation = """wugang love 'bigdata' once!
wugang love "bigdata" twice!
wugang love "bigdata" many times!
"""
print triQutation
#转义(\\)
errorPath = "c:\npath"
print errorPath
slashPath = "c:\\npath"
print slashPath
#原始字符串r，不会转义(\n,\b,\t)，将字符串原样输出
naturalPath = r"c:\npath1\bpath2\tpath3"
print naturalPath
#unicode字符串，以unicode编码字符
unicodeString = u" wugang love bigdata!"
print unicodeString

#% 字符串格式化
format = "Hello, %s! %s love bigdata!"
value = ("world", "wugang")
print format%value

#Template模板字符串
shouting = Template("$name love ${prefix}data very much!")
#字典提供键/值对
keyValue={}
keyValue['name'] = 'wugang'
keyValue['prefix'] = 'big'
shouting = shouting.substitute(keyValue)
print shouting

#字符串格式化转换类型
#d,i  带符号十进制  o 不带符号八进制  u  不带符号十进制  x X不带符号十六进制
#e E科学计数法浮点数   f F十进制浮点数
#r s字符串
#宽度和精度  %10.2f   #字段宽10，小数点2位
#0,+,-和空格  用来对齐和填充
#0表示用0来填充左边空位
#-表示左对齐，右侧用空格填充
#+表示不管正数还是负数都标示出符号
#空格表示正数前加空格
format = '%010.2f'%pi
print format
format = '%+5d'%10 + '\n' + '%+5d'%-10
print format

#格式化实例，使用给定宽度打印格式化价格列表
#可以用（*）作为字段宽度或者精度，此时数值会从元组参数中读出
#width = input("please input width(width>10):")
width = 30
price_width = 10;
item_width = width - price_width
head_format = '%-*s%*s'
format = "%-*s%*.2f"
print "=" * width
print head_format %(item_width,"Item", price_width, "Price")
print "-" * width
print format % (item_width, "Apple", price_width, 2.2)
print format % (item_width, "Banana", price_width, 6.2)
print "-" * width

#字符串常用方法
#find，查找子串，返回最左端索引
parentString = "wugang love bigdata very much!"
subString = "wugang"
index = parentString.find(subString)
print "find subString in index:%d, subString:%s" %(index, parentString[index:len(subString)])
#join,连接列表元素，必须为字符串
directory = '','usr','bin','env'
slash = '\\'
path = slash.join(directory)
print path
#lower 返回小写字母，upper，返回大写字母
testString = "Wugang love BigData very much !"
upperString = testString.upper()
lowerString = upperString.lower()
print testString + "\n" + upperString + "\n" + lowerString
#replace
replaceFromString = 'love'
replaceToString = "evol"
stringAfterReplace = testString.replace(replaceFromString, replaceToString)
print stringAfterReplace
#split  切割字符串成字符串序列
splitSequence = testString.split(' ')
print splitSequence
#strip 返回去除两侧指定字符参数（默认为空格）的字符串
testStringAddSpace = '  ' + testString + '  '
testStringAfterStrip = testStringAddSpace.strip()
testStringDelete = testString.strip('!')
print testStringAddSpace + "\n" + testStringAfterStrip + "\n" + testStringDelete
#translate，转换单个字符,reverseTable为字符对应转换表
fromString = "abcdefghigklmn"
toString = fromString[::-1]
reverseTable = maketrans(fromString, toString)
translateString = testString.translate(reverseTable)
print fromString + "\n" + toString
print testString + '\n' + translateString
