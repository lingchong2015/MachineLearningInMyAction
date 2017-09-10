# coding:utf-8

"""一个简单的Python类"""


class MyClass:

    i = 0
    s = []

    def __init__(self, _i):
        self.i = _i
        self.s.append(_i)

    def f(self):
        print 'Hello World ' + str(self.i) + str(self.s) + "!"
