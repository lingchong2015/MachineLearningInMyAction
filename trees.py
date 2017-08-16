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


def calc_shannon_entropy(_data_set):  # 计算熵，信息增益是熵的减少（数据无序度）。
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


# 1、提取一个数据元组A。
# 2、如果A中_axis列的值等于_value，则将A中其余列加入返回值列表中。
# 3、重复1，直到_data_set遍历结束。
def split_data_set(_data_set, _axis, _value):  # 根据特征索引（_axis）与特征值（_value）划分数据集（_data_set）。
    list_result = []
    for item in _data_set:
        col_sel_val = item[_axis]
        if col_sel_val == _value:
            list_tmp = item[:_axis]
            list_tmp.extend(item[_axis + 1:])
            list_result.append(list_tmp)

    return list_result


# 1、计算熵作为基本信息增益。
# 2、遍历每一个特征，计算以每个特征为数据集划分标准的子数据集的熵，熵越小表明信息增益越大。
# 3、选取熵最小的特征作为最优划分方案。
def choose_best_feature_to_split(_data_set):  # 选择最优数据集划分方式。
    base_shannon_entropy = calc_shannon_entropy(_data_set)
    best_feature_index = -1
    best_info_gain = 0.0

    feature_num = len(_data_set[0]) - 1
    for i in range(feature_num):
        list_col_val = [row[i] for row in _data_set]
        set_col_val = set(list_col_val)

        sub_data_set_shannon_entropy = 0.0
        for j in set_col_val:
            sub_data_set = split_data_set(_data_set, i, j)
            sub_data_set_shannon_entropy += (float(len(sub_data_set)) / len(_data_set)) * calc_shannon_entropy(
                sub_data_set)

        info_gain = base_shannon_entropy - sub_data_set_shannon_entropy  # 信息增益是熵（数据无序度）的减少。
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature_index = i

    return best_feature_index


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
# shannon_entropy = calc_shannon_entropy(data_set)
# print shannon_entropy
# list_split = split_data_set(data_set, 0, 1)
# print list_split
# list_split = split_data_set(data_set, 0, 0)
# print list_split
ret_best_feature = choose_best_feature_to_split(data_set)
print ret_best_feature