# coding:utf-8

"""一个简单的Python类"""


class MyClass:

    _i = 0
    _s = []

    def __init__(self, _i):
        self._i = _i
        self._s.append(_i)

    def f(self):
        print 'Hello World ' + str(self._i) + str(self._s) + "!"
