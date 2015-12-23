# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中异常的案例

while True:
    try:
        divisionNumber1 = input("Enter the first number:")
        divisionNumber2 = input("Enter the first number:")
        value = divisionNumber1 / divisionNumber2
        print "x/y = %d"%value
    ##内建异常类：ZeroDivisionError, NameError(跟教材中说的输入字符串用TypeError来捕获不一样，使用python2.7,根据IDE提示用NameError)
    except (ZeroDivisionError,NameError, SyntaxError), e:
        print "The enter number is not correct! Please try again", e
    else:
        break;
    finally:
        print "finally is always run"
