# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中类的案例
__metaclass__ = type

class Person:
    #构造函数
    def __init__(self, personName = "wugang"):
        self.name = personName
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, World! I am %s." %self.name

person = Person()
person.greet()
person.setName("yangjuan")
person.greet()

#类变量和类方法私有化，只要在它的名字前面加上双下划线
class Secretive:
    def __inaccessible(self):
        print "The function is private"

    def accessible(self):
        print "The scret message is:"
        self.__inaccessible()

secret = Secretive()
secret.accessible()

#继承
class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SAMP(Filter):
    def init(self):
        self.blocked = ["SAMP"]

sampFilter = SAMP()
sampFilter.init()
filter = sampFilter.filter(["SAMP", 1, "WU", "SAMP", "samp", [1, "SAMP"]])
print filter

#旧版本中的未绑定方法实现子类调用超类的构造方法
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print "hungry..."
            self.hungry = False
        else:
            print "No, thanks!"

class SongBird(Bird):
    def __init__(self):
        #旧版本用非绑定方法
        #Bird.__init__(self)
        #新版本用super函数
        super(SongBird, self).__init__()
        self.sound = "gojigoji"
    def sing(self):
        print self.sound

songBird = SongBird()
songBird.eat()
songBird.sing()