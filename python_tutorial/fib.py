# coding:utf-8

"""斐波那契序列操作模块。

@author: Stephen Curry
@date: 2017/08/23
"""


def fib_print(n):
    """打印斐波那契序列。
    
    :param n: 斐波那契序列最终值的临界点（不包含n）。
    :return: None。
    """

    a, b = 0, 1

    while b < n:
        print b

        a, b = b, a + b  # a与b是同时赋值的，a被赋予b的值，b被赋予a在没有被赋予b的值的之前的值。


def fib_list(n):
    """获取斐波那契序列列表。
    
    :param n: 斐波那契序列最终值的临界点（不包含n）。
    :return: 斐波那契序列列表。
    """

    a, b = 0, 1
    result = []

    while b < n:
        result.append(b)

        a, b = b, a + b

    return result
