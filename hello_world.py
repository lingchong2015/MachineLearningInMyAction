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


def enumerate_it(_sequence, _start=0):
    """
        yield语句仅用于定义生成器函数时在其函数体内使用。当yield在一个函数定义中使用时，该函数不再被视为普通函数，而被编译器看作生成器函
        数使用。调用生成器函数可以返回生成器函数的迭代器对象iterator，调用iterator.next()会重复返回一个yield语句后面跟随的表达式（即：
        yield expression_list，返回的是expression_list），直到迭代完毕或出现异常。
        在返回expression_list的同时，生成器函数会停止执行yield的下一条语句，保留（冻结）所有生成器函数执行的信息，等待下一次的next()
        调用。
        从Python 2.5开始，yield语句支持try...finally语法结构，finally里面的语句会在迭代器函数中的资源会回收（引用计数为0、GC或调用
        iterator.close()函数）时执行。
    """

    try:
        n = _start
        for elem in _sequence:
            yield n, elem
            n += 1
    finally:
        print 'Execute finally clause.'


# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# g = enumerate_it(seasons)
# print g.next()
# print g.next()
# print g.next()
#
# for i in range(10):
#     print datetime.now()
#     time.sleep(1)
#
# g.close()

def print_num(_num):
    print _num


def for_iterator_imitation(_list_index):
    i = 0
    n = len(_list_index)

    while i < n:
        yield _list_index[i]
        i += 1


def for_clause_imitation():
    """
        模拟for...in语法结构。
        注意：当for_iterator_imitation(...)函数执行完毕（即其中的while语句跳出）时，iterator.next()函数会返回（触发）一个
        StopIteration异常，通过捕获该异常可以判断迭代完成。
    """

    i = 3
    list_index = []
    counter = 0
    while counter < i:
        list_index.append(counter)
        counter += 1

    print list_index

    iterator = for_iterator_imitation(list_index)
    while True:
        try:
            j = iterator.next()
            print j
        except StopIteration:
            break

    # for_clause_imitation()

"""
    for与while语句可以配合else语句使用，在这里，else语句是当for语句条件执行完毕或while语句条件为false时执行，但是如果是因为for或while
    语句块内break语句被调用而退出循环的，else的语句块不会被执行到。
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, 'equals', x, '*', n / x
            break
    else:
        print n, 'is a prime number'
