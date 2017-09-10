# coding:utf-8

from python_tutorial import MyClass1
from python_tutorial import MyClass2


class MySubClass(MyClass1.MyClass, MyClass2.MyClass2):

    def __init__(self):
        pass
