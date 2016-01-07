# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中中英文不同编码转换的案例
import sys

if len(sys.argv) >= 2:
    filename = sys.argv[1]
else:
    filename = "E:\git_project\learn_python\chinese.txt"

file = open(filename)
text = file.read()
print text