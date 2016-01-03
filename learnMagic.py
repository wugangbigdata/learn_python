# coding=utf-8
# python 默认ASCII码，不支持中文，第一句表示用utf-8字符编码方式
# 这是一个学习python中魔法方法的案例
__metaclass__ = type

#__eq__(self, other) 定义相等符号的行为，==
#__ne__(self,other) 定义不等符号的行为，！=
#__lt__(self,other) 定义小于符号的行为，<
#__gt__(self,other) 定义大于符号的行为，>
#__le__(self,other) 定义小于等于符号的行为，<=
#__ge__(self,other) 定义大于等于符号的行为，>=

class Word(str):
    #'''Class for words, defining comparison based on word length.'''

    def __new__(cls, word):
        # Note that we have to use __new__. This is because str is an immutable
        # type, so we have to initialize it early (at creation)
        if ' ' in word:
            print "Value contains spaces. Truncating to first space."
            word = word[:word.index(' ')] # Word is now all chars before first space
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)
    def __lt__(self, other):
        return len(self) < len(other)
    def __ge__(self, other):
        return len(self) >= len(other)
    def __le__(self, other):
        return len(self) <= len(other)

compare = (Word('foo  hase') <= Word('bar'))
print compare

#自定义序列
class FunctionalList:
    '''A class wrapping a list with some extra functional magic, like head,    tail, init, last, drop, and take.'''

    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        # if key is of invalid type or value, the list values will raise the error
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __delitem__(self, key):
        del self.values[key]

    def __iter__(self):
        return iter(self.values)

    def __reversed__(self):
        return FunctionalList(reversed(self.values))

    def append(self, value):
        self.values.append(value)
    def head(self):
        # get the first element
        return self.values[0]
    def tail(self):
        # get all elements after the first
        return self.values[1:]
    def init(self):
        # get elements up to the last
        return self.values[:-1]
    def last(self):
        # get last element
        return self.values[-1]
    def drop(self, n):
        # get all elements except first n
        return self.values[n:]
    def take(self, n):
        # get first n elements
        return self.values[:n]

stringToList = list("wugang love bigdata!")
print stringToList

#自定义序列使用实例
functionList = FunctionalList(stringToList)
print functionList[10]