# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中魔法方法，属性和迭代器的案例

#魔法方法，基本的序列和映射规则
#没搞太懂，下次接着弄明白
#__len__(self), __getitem__(self,key),  __setitem__(self,key, value),  __delitem__(self,key)
#__getattr__(self, name), __setattr__(self, name ,value)
#用继承来实现一个和内建列表相似的行为
__metaclass__ = type

#记录列表元素访问次数
class CounterList(list):
    def __init__(self, *args):
        super(CounterList, self).__init__(*args)
        self.counter = 0;

    def __getitem__(self, index):
        self.counter += 1;
        return super(CounterList, self).__getitem__(index)

counterList = CounterList(range(10))
counterList.reverse()
value = counterList[2] + counterList[9]
print value, counterList.counter

#property函数
class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self, size):
        self.width, self.height = size
    def getSize(self):
        return self.width, self.height
    size = property(getSize, setSize)

rectangle = Rectangle()
rectangle.width = 5
rectangle.height = 10;
print rectangle.size
rectangle.size = 120, 200
print  rectangle.size

#静态方法和类方法
#从实际运行效果来看，不清楚静态方法和类方法有何不同
class MyClass:
    @staticmethod
    def smeth():
        print "This is a static method"

    @classmethod
    def cmeth(cls):
        print "This is a class method"

myclass = MyClass()
MyClass.smeth()
MyClass.cmeth()
myclass.cmeth()
myclass.smeth()

#iter迭代器
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def next(self):
        self.a, self.b = self.b, self.a + self.b
        return  self.a
    def __iter__(self):
        return self

fib =Fibs()
for f in fib:
    if f > 100:
        print f
        break

#生成器
#任何包含yield语句的函数叫生成器
