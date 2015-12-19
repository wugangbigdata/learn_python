#coding=utf-8
#python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
#这是一个学习字符串操作的实例，字符串是不可改变值的
#单引号字符串操作
from string import Template

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
