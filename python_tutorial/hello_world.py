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

from python_tutorial import *
import json

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


# def enumerate_it(_sequence, _start=0):
#     """
#         yield语句仅用于定义生成器函数时在其函数体内使用。当yield在一个函数定义中使用时，该函数不再被视为普通函数，而被编译器看作生成器函
#         数使用。调用生成器函数可以返回生成器函数的迭代器对象iterator，调用iterator.next()会重复返回一个yield语句后面跟随的表达式（即：
#         yield expression_list，返回的是expression_list），直到迭代完毕或出现异常。
#         在返回expression_list的同时，生成器函数会停止执行yield的下一条语句，保留（冻结）所有生成器函数执行的信息，等待下一次的next()
#         调用。
#         从Python 2.5开始，yield语句支持try...finally语法结构，finally里面的语句会在迭代器函数中的资源会回收（引用计数为0、GC或调用
#         iterator.close()函数）时执行。
#     """
#
#     try:
#         n = _start
#         for elem in _sequence:
#             yield n, elem
#             n += 1
#     finally:
#         print 'Execute finally clause.'


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

# def print_num(_num):
#     print _num
#
#
# def for_iterator_imitation(_list_index):
#     i = 0
#     n = len(_list_index)
#
#     while i < n:
#         yield _list_index[i]
#         i += 1
#
#
# def for_clause_imitation():
#     """
#         模拟for...in语法结构。
#         注意：当for_iterator_imitation(...)函数执行完毕（即其中的while语句跳出）时，iterator.next()函数会返回（触发）一个
#         StopIteration异常，通过捕获该异常可以判断迭代完成。
#     """
#
#     i = 3
#     list_index = []
#     counter = 0
#     while counter < i:
#         list_index.append(counter)
#         counter += 1
#
#     print list_index
#
#     iterator = for_iterator_imitation(list_index)
#     while True:
#         try:
#             j = iterator.next()
#             print j
#         except StopIteration:
#             break
#
#     # for_clause_imitation()
#
# """
#     for与while语句可以配合else语句使用，在这里，else语句是当for语句条件执行完毕或while语句条件为false时执行，但是如果是因为for或
#     while语句块内break语句被调用而退出循环的，else的语句块不会被执行到。
#     与循环语句配合使用else同与try语句配合使用else类似，但同if语句配合使用else不同，在try语句中执行到else语句块的条件是在try语句块中没
#     有异常发生，在循环语句中执行到else语句块的条件是没有break语句被执行且跳出循环。
# """
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print n, 'equals', x, '*', n / x
#             break
#     else:
#         print n, 'is a prime number'


# """
#     Python的代码执行流程按照（Line 146->Line 149->Line 154->...）顺序执行的，而且只赋值一次，也就是说，当执行到第149行时，i等于5，
#     所以即使在第153行将i重新赋值为6，当第154行调用函数f1(...)时，第149行的i还是为5。
#     或者这样理解也可以，当代码顺序执行到第149行时，已经在函数f1(...)的本地符号表中将行参arg赋值为5，这个赋值只执行一次，所以当在154行调
#     用f1(...)函数，由于使用的是f1(...)函数的默认参数值，所以arg为5。
#     对于函数f2(...)同样可以这样理解，行参l的初始化值为指向一个列表对象的引用，这个引用会被写进函数f2(...)的本地符号表中，之后每一次调用
#     f2(...)函数，只要l用的是默认参数，那么都是往同一个列表对象中添加元素。
#     函数f3(...)就不同了，行参l在f3(...)的本地符号表中的值为None，也就是一个不指向任何对象的空值，那么每次调用时只要l使用的是默认参数，
#     那么l就为None，根据f3(...)中167行～168行的代码就会让l成为一个新的列表的引用。
# """
#
# i = 5
#
#
# def f1(arg=i):
#     print arg
#
#
# i = 6
# f1()
#
#
# def f2(a, l=[]):
#     l.append(a)
#     return l
#
# print f2(1)
# print f2(2)
# print f2(3)
#
#
# def f3(a, l=None):
#     if l is None:
#         l = []
#     l.append(a)
#     return l
#
# print f3(1)
# print f3(2)
# print f3(3)


# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print "-- This parrot wouldn't", action,
#     print "if you put", voltage, "volts through it."
#     print "-- Lovely plumage, the", type
#     print "-- It's", state, "!"

# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# def make_incrementor(n):
#     return lambda x: x + n
#
#
# f = make_incrementor(1)
# print f


# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'),]
# pairs.sort(key=lambda pair: pair[1])
# print pairs


# empty = ()
# print empty
# print len(empty)
# singleton = '1', '2',
# print singleton
# print len(singleton)


# fib.fib_print(10)
# print fib.fib_list(10)
# print fib.__name__
# print fib.fib_print.__doc__
# print fib.fib_list.__doc__

# print sys.path


# print dir(fib)
# print dir(fib.__builtins__)
# print fib.__doc__
# print fib.__file__
# print fib.__name__
# print fib.__package__
# print fib.fib_list.__doc__
# print fib.fib_print.__doc__


# print dir()


# for elem in dir(__builtin__):
#     print elem


# print dir()


# for x in range(1, 11):
#     print repr(x).rjust(2), repr(x * x).rjust(3), repr(x * x * x).rjust(4)
#
# for x in range(1, 11):
#     print '{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x)
#
# print 1, 2
# print '1', '2'

# print '{}{}'.format(1, 2)
# print '{1}{1}'.format(1, 2)
# print '{one}{two}'.format(one=1, two=2)
# print '{0}{two}'.format(1, two=2)
#
# table = {'凌冲': 123, '朗朗': 333}
# for k, v in table.items():v
#     print '{k:10}==>{v:10d}'.format(k=k, v=v)
#
# print '{凌冲},{朗朗}'.format(**table)
# print '{0[凌冲]},{0[朗朗]}'.format(table)

# print file.__doc__

# f = open('Reflector 7.0\Reflector.exe', 'r')
# f.write('Hello World, Python!')
# f.write('123')
# content = f.read()
# print content

"""
    open函数是Python的内置函数，一般推荐用open函数打开文件，open函数使用file()类型返回一个file对象。
    
    一个文本文件每一行都会有一个换行符'\n'，但最后一行没有，下面这个1.txt中一共有三行：
    123
    （空行）
    （空行）
    执行下面279~285行代码会得到下面的输出：
    '123'
    '\n'
    ''
    这种方法用于判断文件的空行与结尾，空行用'\n'表示，结尾用''表示。
"""
# f = open('1.txt', 'w+')
# line = f.readline()
# print repr(line)
# line = f.readline()
# print repr(line)
# line = f.readline()  # 在文件中这已经是结尾了，但是再进行f.readline()调用，还是会得到''的结果。
# print repr(line)
#

"""
    以for...in...的方法枚举f得到的是123等字符串，以list(f)或f.readlines()的方法得到的是list，list中的字符串是'123\n'等
    字符串。
    
    open函数返回的是file对象，file对象应该是一种流，读过的行不能被同一个open函数打开的file对象再次读取。
"""
# # 结尾在遍历中不会被枚举。
# for l in f:
#     print repr(l)

# listFile = list(f)
# print listFile

# f.write('凌冲')
# f.flush()  # 在f.write()之后不加f.flush()会出现乱码。
# lines = f.readlines()
# print lines
# print f.tell()  # 前面因为调用了f.write()，这里f.tell()的值为文件大小，因为f对象的指针在写操作之后指向了文件的结尾。
# print repr(f.readline())  # 因为f对象的指针指向了文件的结尾，所以这里的输出为''。

# value = ('The answer is ', 39)
# s = str(value)
# f.write(s)
# f.flush()

# f.seek(3, 0)
# print f.readline()

# with open('1.txt', 'a+') as f:
#     f.write('123')
#     f.flush()
#     f.seek(0, 0)
#     print f.readline()
# print f.closed

# f = open('1.txt', 'w+')
# obj1 = {'name': '凌冲', 'age': 33}
# json.dump(obj1, f)
# obj2 = json.load(f)
# print str(obj1)
# print obj2
# json.dump(obj1, f)
# obj2 = json.load(f)
# print obj2

# dic1 = {'type': 'dic1', 'username': '凌冲', 'age': 16}
# json_dic1 = json.dumps(dic1)
# print json_dic1
# json_dic2 = json.dumps(dic1, sort_keys=True, indent=4, separators=(',', ': '), ensure_ascii=False)
# print json_dic2
#
# f = open('1', 'w+')
# json.dump(json_dic1, f, encoding='utf-8', ensure_ascii=False)
# jsonDic3 = json.load(f, encoding='utf-8')
# print jsonDic3


# j = {'username': '凌冲'}
# with open("test.json", "w") as outfile:
#     json.dump(j, outfile, indent=4, ensure_ascii=False)
#
# with open("test.json") as infile:
#     j = json.load(infile)
#
# print j

# x = 0
# while True:
#     try:
#         x = int(raw_input('请输入一个数字：'))
#         break
#     except ValueError:
#         print '输入的不是有效数字，请重新输入。'
#
# print x

# print fib.__name__

# print fib.a
# print fib.b
# del fib.a
# try:
#     print fib.a
# except AttributeError as e:
#     print e.__str__()

# print fib.__doc__

# fib.fib_print(3)

# print abs.__module__

# global x
# x = 3
#
#
# def print_x(i):
#     # x = i + 1
#     # del x
#     print x
#     if x == 3:
#         del x
#         print_x(5)
#
# print_x(2)
# print x


# cls1 = MyClass.MyClass(123)
# print MyClass.__doc__
# print MyClass.__name__
# print MyClass.MyClass.f  # 未绑定类方法
# print cls1.f  # 绑定实例方法
#
# cls1.f()
#
# cls2 = MyClass.MyClass(333)
# # cls2.i = 333
#
# cls1.f()
# cls2.f()
#
# print cls1.__class__
# print cls2.__class__


# cls = MySubClass.MySubClass()
# cls.f()
# cls.g()


s = '123,333'
setString = set(s1 for s1 in s.split(','))
print setString
