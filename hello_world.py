# coding: utf-8

# from numpy import *
#
# print "Hello World, Python And Machine Learning!"
#
# arrayRand = random.rand(4, 4)
# print arrayRand
#
# matRand = mat(arrayRand)
# print matRand
#
# invMatRand = matRand.I
# print invMatRand
#
# print matRand * invMatRand
#
# print matRand * invMatRand - eye(4)

import sys

from datetime import datetime
import time


# while True:
#     s = raw_input('请输入一个数字：')
#     if s == 'quit':
#         break
#     else:
#         try:
#             i = float(s)
#             if i < 0:
#                 print '这是一个负数。'
#             elif i == 0:
#                 print '输入为0。'
#             else:
#                 print '这是一个正数。'
#         except ValueError:
#             print sys.exc_info()[0]
#             print '您输入的不是一个数字。'
#             raise

# list_word = [1, 2, 3]
# for w in list_word:
#     print w


def enumerate_it(sequence, start=0):

    """
        yield语句仅用于定义生成器函数时在其函数体内使用。当yield在一个函数定义中使用时，该函数不再被视为普通函数，而被编译器看作生成器函
    数使用。调用生成器函数可以返回生成器函数的迭代器对象iterator，调用iterator.next()会重复返回一个yield语句后面跟随的表达式（即：
    yield expression_list，返回的是expression_list），直到迭代完毕或出现异常。
        在返回expression_list的同时，生成器函数会执行到下一个yield语句为止，保留（即冻结）所有生成器函数执行的信息，等待下一次的next()
    调用。
        从Python 2.5开始，yield语句支持try...finally语法结构，finally里面的语句会在迭代器函数中的资源会回收（引用计数为0、GC或调用
    iterator.close()函数）时执行。
    """

    try:
        n = start
        for elem in sequence:
            yield n, elem
            n += 1
    finally:
        print 'Execute finally clause.'


seasons = ['Spring', 'Summer', 'Fall', 'Winter']
g = enumerate_it(seasons)
print g.next()
print g.next()
print g.next()

for i in range(10):
    print datetime.now()
    time.sleep(1)

g.close()
