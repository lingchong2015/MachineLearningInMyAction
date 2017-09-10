# coding:utf-8


class MyParentClass:

    s = 'MyParentClass'

    def __init__(self):
        print self.s
        pass

    def print_hello(self):
        print self.s + ' says \'Hello\'!'
