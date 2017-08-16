# -*- coding: utf-8 -*-

"""
内容：决策树算法
作者：Stephen Curry
日期：2017/8/15
"""

from math import log

"""
Function
"""


def calc_shannon_entropy(_data_set):  # 计算entropy。
    row_num = len(_data_set)
    map_label = {}

    for r in _data_set:
        label = r[-1]
        if label not in map_label.keys():
            map_label[label] = 1
        else:
            map_label[label] += 1

    result = 0.0
    for k in map_label.keys():
        prop = (float(map_label[k]) / row_num)
        result -= prop * log(prop, 2)

    return result


def create_data_set():  # 创建测试样本。
    return [[1, 1, 'Yes'],
            [1, 1, 'Yes'],
            [1, 0, 'No'],
            [0, 1, 'No'],
            [0, 1, 'No']], ['No Surfacing', 'Flippers']


"""
Caller
"""


data_set, label_list = create_data_set()
shannon_entropy = calc_shannon_entropy(data_set)
print shannon_entropy

