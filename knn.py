# -*- coding: utf-8 -*- #设置源文件编码。

"""
内容：kNN（k Nearest Neighbors）算法
作者：Stephen Curry
日期：2017/8/13
"""

# Python导入模块的方法有两种：import module 和 from module import，区别是前者所有导入的类或函数使用时需加上模块名的限定，而后者不需要。

# 科学计算包。
from numpy import *

# 运算符模块，k邻近算法排序时使用。
import operator

import matplotlib
import matplotlib.pyplot as plt

from os import listdir
from datetime import datetime

"""Function"""


# 函数要距离上一个代码片段2个空行。
# 函数的名称要全小写，并以"_"分隔。
def create_data_set():
    # 缩进为四个空格。
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(_vector_test, _data_set, _labels, _k):  # 基本的k邻近算法实现。
    if (len(_data_set) != len(_labels)) or (_k >= len(_data_set)) or (_k <= 0):
        print '输入参数异常，数据集的长度应与标签集合一致，k值应小于数据集长度但大于0。'
        return

    data_set_size = _data_set.shape[0]
    diff_mat = tile(_vector_test, (data_set_size, 1)) - _data_set
    sqr_diff_mat = diff_mat ** 2
    sqr_distances = sqr_diff_mat.sum(axis=1)
    distances = sqr_distances ** 0.5
    distances_sorted_indicies = distances.argsort()

    class_count = {}
    for i in range(_k):
        label_voted = _labels[distances_sorted_indicies[i]]
        class_count[label_voted] = class_count.get(label_voted, 0) + 1

    class_count_sorted = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return class_count_sorted[0][0]


def file2matrix(_filename):  # 读取约会数据文件。
    fn = open(_filename)
    array_of_lines = fn.readlines()
    number_of_lines = len(array_of_lines)

    ret_mat = zeros((number_of_lines, 3))

    list_label = []
    index = 0
    for item in array_of_lines:
        item = item.strip()
        list_string_from1line = item.split('\t')
        ret_mat[index, :] = list_string_from1line[0: 3]
        list_label.append(list_string_from1line[-1])
        index += 1

    return ret_mat, list_label


def auto_norm(_data_set):  # 归一化特征值。
    min_values = _data_set.min(0)
    max_values = _data_set.max(0)
    ranges = max_values - min_values

    row_num = _data_set.shape[0]
    norm_data_set = (_data_set - tile(min_values, (row_num, 1))) / tile(ranges, (row_num, 1))

    return norm_data_set, ranges, max_values, min_values


def dating_class_test():  # 约会kNN测试。
    mat_dating_data, list_label = file2matrix('/Users/lingchong/documents/development/ai/machinelearning/'
                                              'machinelearninginaction/ch02/datingTestSet2.txt')
    norm_data_set, ranges, max_values, min_values = auto_norm(mat_dating_data)

    row_num = norm_data_set.shape[0]
    hold_out_ratio = 0.1
    test_vecs_num = int(row_num * hold_out_ratio)
    error_count = 0.0
    for i in range(test_vecs_num):
        result = classify0(norm_data_set[i, :], norm_data_set[test_vecs_num:, :], list_label[test_vecs_num:], 3)
        print '第%d行数据返回，分类器测试结果为：%s，实际结果为：%s。' % (i + 1, result, list_label[i])
        if result != list_label[i]:
            error_count += 1.0
    print '分类器正确率为：%f。' % ((row_num - error_count) / row_num)
    print '共有%d个错误。' % error_count


def dating_person_classify():  # 约会交互界面。
    person_class_list = ['完全没感觉', '感觉一般', '非常来电']

    flight_miles = float(raw_input('请输入您每年的飞行公里数：'))
    game_percent = float(raw_input('请输入您在游戏上的时间花费百分比：'))
    ice_cream_weekly = float(raw_input('请输入您每周消耗的冰淇淋公升数：'))

    mat_dating_data, list_label = file2matrix('/Users/lingchong/documents/development/ai/machinelearning/'
                                              'machinelearninginaction/ch02/datingTestSet2.txt')
    norm_data_set, ranges, max_values, min_values = auto_norm(mat_dating_data)

    vec_input = array([flight_miles, game_percent, ice_cream_weekly])
    result = classify0(
        (vec_input - min_values) / ranges,
        norm_data_set,
        list_label,
        3
    )
    print '您属于我%s的人。' % person_class_list[int(result) - 1]


def img2vector(_filename):  # 读取文本格式的图像文件并转换为向量数组。
    ret_vec = zeros((1, 1024))

    fn = open(_filename)
    for i in range(32):
        line = fn.readline()
        for j in range(32):
            ret_vec[0, i * 32 + j] = int(line[j])

    return ret_vec


# 1.获取所有训练样本文件。
# 2.将所有训练样本文件转换为向量矩阵，并记录对应的数字，形成数字列表。
# 3.读入一个测试样本，转换为向量，然后进行测试。
# 4.重复3直到测试样本读取结束。
# 5.输出统计结果。
def handwriting_class_test():  # 手写识别测试。
    start_time = datetime.now()

    training_root_dir = '/Users/lingchong/documents/development/ai/machinelearning/machinelearninginaction/ch02' \
                        '/digits/trainingdigits/'
    training_file_dirs = listdir(training_root_dir)
    mat_train = zeros((len(training_file_dirs), 1024))
    list_fn = []
    index = 0
    for s in training_file_dirs:
        mat_train[index, :] = img2vector(training_root_dir + s)
        index += 1
        list_fn.append(filename2number(s))

    test_root_dir = '/Users/lingchong/documents/development/ai/machinelearning/machinelearninginaction/ch02/digits' \
                    '/testdigits/'
    test_file_dirs = listdir(test_root_dir)
    error_count = 1
    for s in test_file_dirs:
        test_mat = img2vector(test_root_dir + s)
        result = classify0(test_mat, mat_train, list_fn, 3)
        if result != filename2number(s):
            error_count += 1
            print '测试样本与kNN分类器返回结果不符，测试样本名称：%s，分类结果：%s。' % (s, result)
        else:
            print '分类器执行正确，测试样本名称：%s，分类结果：%s。' % (s, result)

    print '测试完毕，分类器正确率为%f。' % (1 - error_count / float(len(test_file_dirs)))

    end_time = datetime.now()
    print '测试时间为：%.2f秒。' % ((end_time - start_time).seconds + (end_time - start_time).microseconds / 1000000.0)


def filename2number(fn):
    fn_without_ex = fn.split('.')[0]
    num = int(fn_without_ex.split('_')[0])
    return num


"""Caller"""

# data_set, label_list = create_data_set()
# print classify0([0, 0], data_set, label_list, 3)
# mat_dating_data, list_label = file2matrix('/Users/lingchong/documents/development/ai/machinelearning/'
#                                           'machinelearninginaction/ch02/datingTestSet2.txt')
# norm_data_set, ranges, max_values, min_values = auto_norm(mat_dating_data)

# print mat_dating_data
# print list_label

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(norm_data_set[:, 1], norm_data_set[:, 2], 15.0 * array(list_label), 15.0 * array(list_label))
# plt.show()

# dating_class_test()
# dating_person_classify()

# num_vec = img2vector('/Users/lingchong/documents/development/ai/machinelearning/machinelearninginaction/ch02/digits/'
#                      'trainingdigits/0_5.txt')
# print num_vec[0, 0:32]
# print num_vec[0, 32:90]

handwriting_class_test()
