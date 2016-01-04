# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中re模块正则表达式的案例
#import fileinput
import re

some_text = 'alpha.beta...gamma delta'
splitList = re.split('[. ]+', some_text, maxsplit = 2) #maxsplit参数表示分割部分数目
print splitList

#查找所有的单词
pat = '[a-zA-Z]+'
text = "wugang love bigdata! ... very much"
wordList = re.findall(pat, text)
print "wordList:", wordList
#查找标点符号
pat = r'[.?\-",!]+'
punctuationList = re.findall(pat, text)
print "punctuationList:", punctuationList
#替换字符串
pat = 'wugang'
replaceString = 'yangjuan'
textReplace = re.sub(pat, replaceString, text)
print "textReplace:", textReplace

#escape对自然字符串进行转义转换
naturalString = "www.python.org"
pythonString = re.escape(naturalString)
print "pythonString:", pythonString

#匹配对象和组,组是放置在圆括号内的子模式，组0是整个模式
pat = 'www\.(.*)\..{3}' #两个组，组0为整个模式，组1为（。*）匹配字符串
text = "www.python.org"
matchObject = re.match(pat, text)
matchString1 = matchObject.group(0)
matchString2 = matchObject.group(1)
print "group(0):", matchString1
print "group(1):", matchString2
startIndex = matchObject.start(1)
endIndex = matchObject.end(1)
matchGroup1 = text[startIndex:endIndex]
print "text[%d:%d]:%s"%(startIndex, endIndex, matchGroup1)