# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中模板系统的案例

#模板系统
import fileinput
import re

field_pat = re.compile(r'\[(.+?)\]')
scope = {}
def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code, scope))  #eval求表达式的值
    except SyntaxError:
        exec code in scope  #eval出错，用exec执行命令
        return ''

lines = []
for line in fileinput.input("E:\\fileInput.txt"):
    lines.append(line)
text = ''.join(lines)
print "text:", text
print field_pat.sub(replacement, text)