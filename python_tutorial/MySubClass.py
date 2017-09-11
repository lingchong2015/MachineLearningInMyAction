# coding:utf-8

from python_tutorial import MyClass1
from python_tutorial import MyClass2


class MySubClass(MyClass1.MyClass1, MyClass2.MyClass2):

    def __init__(self):
        print 'MySubClass'

    def f(self):
        print 'Hello World, MySubClass!'
