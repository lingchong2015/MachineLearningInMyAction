# -*- coding: utf-8 -*-

"""
内容：决策树算法
作者：Stephen Curry
日期：2017/8/15
"""

from math import log

import operator


"""
Function
"""


def calc_shannon_entropy(_data_set):
    """计算熵，信息增益是熵的减少（数据无序度）。

    :param _data_set: 待计算熵的数据集。
    :return: 输入数据集_data_set以最后一列为分类类别的熵。
    """

    row_num = len(_data_set)
    map_label = {}

    # 以最后一列标签分类，将每一类标签（这里即Yes与No）出现的次数存储到字典map_label中。
    for r in _data_set:
        label = r[-1]
        if label not in map_label.keys():
            map_label[label] = 1
        else:
            map_label[label] += 1

    # 根据计算熵的公式得到信息的数据无序度。
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


def majority_cnt(_list_label):  # 从标签列表中选取出现频率最高的标签。
    map_label_class = {}
    for label in _list_label:
        if label not in map_label_class.keys():
            map_label_class[label] = 1
        else:
            map_label_class[label] += 1

    map_label_class_sorted = sorted(map_label_class.iteritems(), key=operator.itemgetter(1), reverse=True)

    return map_label_class_sorted[0][0]


# 1、这是一个根据树数据结构的特征，使用递归方法构造的决策树。
# 2、遇到下述两种情况结束递归：
#    a. 当输入数据集（_data_set）中的类别都是一类时，表明已经到叶子节点，则返回类别名称并结束递归。
#    b. 当数据集中的所有特征都已经用于构建决策树时，表明已无特征值可用，则选取频率出现最高的类别并结束递归。
# 3、选取一个最佳特征，根据其不同的特征值进行分类递归。
def create_tree(_data_set, _list_col_name):  # 构建决策树。
    list_class = [row[-1] for row in _data_set]

    if list_class.count(list_class[0]) == len(list_class):
        return list_class[0]

    if len(_data_set) == 1:
        return majority_cnt(list_class)

    best_feature = choose_best_feature_to_split(_data_set)
    tree_node_name = _list_col_name[best_feature]
    del(_list_col_name[best_feature])

    decision_tree = {tree_node_name: {}}  # 二维字典。

    # 开始构建树。
    list_feature_val = [row[best_feature] for row in _data_set]
    set_feature_val = set(list_feature_val)
    for i in set_feature_val:
        sub_col_name = _list_col_name[:]
        decision_tree[tree_node_name][i] = create_tree(split_data_set(_data_set, best_feature, i), sub_col_name)

    return decision_tree


def create_data_set():
    """创建测试样本。

    :return:两个列表：测试样本列表与测试样本每一列的列明列表。
    """

    return [[1, 1, 'Yes'],
            [1, 1, 'Yes'],
            [1, 0, 'No'],
            [0, 1, 'No'],
            [0, 1, 'No']], ['No Surfacing', 'Flippers']


def get_label_list(_data_set):
    """获取数据集中的标签。

    :param _data_set:数据集。
    :return:数据集每一行最后一列组成的列表。
    """
    return [row[-1] for row in _data_set]


