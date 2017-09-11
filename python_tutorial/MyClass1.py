# coding:utf-8

from python_tutorial.MyParentClass import MyParentClass

"""一个简单的Python类"""


class MyClass1(MyParentClass):

    i = 0
    l = []

    def __init__(self, _i):
        self.i = _i
        self.l.append(_i)
        print 'MyClass'

    def f(self):
        print 'Hello World ' + str(self.i) + str(self.l) + "!"

    __f = f

    def g(self):
        print 'g'
        self.__f()


