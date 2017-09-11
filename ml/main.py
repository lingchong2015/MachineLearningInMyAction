# coding:utf-8

from decision_tree import *

data_set, label_list = create_data_set()
shannon_entropy = calc_shannon_entropy(data_set)
print shannon_entropy
# print shannon_entropy
# list_split = split_data_set(data_set, 0, 1)
# print list_split
# list_split = split_data_set(data_set, 0, 0)
# print list_split
# ret_best_feature = choose_best_feature_to_split(data_set)
# print ret_best_feature

# test_label_list = get_label_list(data_set)
# result_majority_label = majority_cnt(test_label_list)
# print result_majority_label

# ret_decision_tree = create_tree(data_set, label_list)
# print ret_decision_tree
