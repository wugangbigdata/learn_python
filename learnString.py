#coding=utf-8
#python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
#这是一个学习字符串操作的实例
#单引号字符串操作
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
