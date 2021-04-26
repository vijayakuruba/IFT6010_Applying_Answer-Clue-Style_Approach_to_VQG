# -*- coding: utf-8 -*-
import numpy as np
import random


def common(list1, list2):
    return list(set(list1).intersection(list2))


def substract(list1, list2):
    return list(set(list1) - set(list2))


def remove_values_from_list(l, val):
    return [value for value in l if value != val]


def del_list_indexes(l, id_to_del):
    somelist = [i for j, i in enumerate(l) if j not in id_to_del]
    return somelist


def del_list_inplace(l, id_to_del):
    for i in sorted(id_to_del, reverse=True):
        del(l[i])


def del_list_numpy(l, id_to_del):
    arr = np.array(l, dtype='int32')
    return list(np.delete(arr, id_to_del))


def weighted_sample(choices, probs):
    """
    Sample from `choices` with probability according to `probs`
    :param choices: list of any kinds of elements
    :param probs: a list of probs. Can be not normalized.
    :return: a sampled element from choices.
    """
    probs = [x / sum(probs) for x in probs]
    probs = np.concatenate(([0], np.cumsum(probs)))
    r = random.random()
    for j in range(len(choices) + 1):
        if probs[j] < r <= probs[j + 1]:
            return choices[j]


# def weighted_sample(choices, probs, k=3):
#     probs = np.array(probs)
#     probs = (probs - np.min(probs)) / (np.max(probs) - np.min(probs))
#     MAX_DIFF = 0.25
#     p = 0.90
#     k = min(k, len(choices))
#     while p >= 0.0:
#         indexes = (np.argwhere(probs >= p)).flatten()
#         if indexes.shape[0] >= k or (indexes.shape[0] == 2 and np.max(probs) - (p*.90) > MAX_DIFF):
#             r = random.randint(0, indexes.shape[0]-1)
#             idx = indexes[r]
#             return choices[idx]
#         else:
#             p = p*.90
