import os
import json
import random
import matplotlib.pyplot as plt
from numpy.ma.core import append

import generators
import time

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in {"unordered_numbers","ordered_numbers","dna_sequence"}:
        return None
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        seq = json.load(json_file)

    return seq[field]

def linear_search(seq, number):
    """
    :reurn (dict): {'positions': <list of indicies>, 'count': <total count>}
    """
    pozice = []
    pocet = 0

    for i in range(len(seq)):
        if seq[i] == number:
            pozice.append(i)
            pocet += 1

    return {"positions": pozice, "count": pocet}

# def pattern_search(seq, pattern):
#
#     indicies = set()
#     pattern_size = len(pattern)
#
#     left_idx = 0
#     right_idx = pattern_size
#     while right_idx< len(seq):
#         for idx in range(pattern_size):
#             if pattern[idx] != seq[left_idx + idx]:
#                 break
#             else:
#                 indicies.add(left_idx + pattern_size // 2)
#
#             left_idx += 1
#             right_idx += 1
#         return indicies


def binary_search(seq, number):
    indexy = [0, len(seq)-1]
    while True:
        polovica = (indexy[0] + indexy[1])//2
        if indexy[0]+1 == indexy[1] and seq[indexy[1]] != number and seq[indexy[0]] != number:
            return None
        if indexy[0] + 1 == indexy[1] and seq[indexy[0]] == number:
            return indexy[0]
        if indexy[0] + 1 == indexy[1] and seq[indexy[1]] == number:
            return indexy[1]
        if seq[polovica] == number:
            return polovica
        if number > seq[polovica]:
            indexy[0] = polovica
            continue
        if number < seq[polovica]:
            indexy[1] = polovica
            continue

def cas(dlzky):
    zoznamy_ordered = []
    zoznamy_unordered = []
    for dlzka in dlzky:
        zoznamy_ordered.append(generators.ordered_sequence(dlzka))
        zoznamy_unordered.append(generators.unordered_sequence(dlzka))
    targets_ordered = [random.choice(zoznam1) for zoznam1 in zoznamy_ordered]
    targets_unordered = [random.choice(zoznam2) for zoznam2 in zoznamy_unordered]

    casy_lin = []
    for zoznam_ordered, target_ordered in zip(zoznamy_ordered, targets_ordered):
        start1 = time.perf_counter()
        linear_search(zoznam_ordered, target_ordered)
        end1 = time.perf_counter()
        duration1 = end1 - start1
        casy_lin.append(duration1)

    casy_bin = []
    for zoznam_unordered, target_unordered in zip(zoznamy_unordered, targets_unordered):
        start2 = time.perf_counter()
        binary_search(zoznam_unordered, target_unordered)
        end2 = time.perf_counter()
        duration2 = end2 - start2
        casy_bin.append(duration2)

    fig, (lin, bin) = plt.subplots(1, 2)

    lin.plot(dlzky, casy_lin)
    lin.set_xlabel("Velikost vstupu")
    lin.set_ylabel("Čas [s]")
    lin.set_title("Linear Search")

    bin.plot(dlzky, casy_bin)
    bin.set_xlabel("Velikost vstupu")
    bin.set_ylabel("Čas [s]")
    bin.set_title("Binary Search")

    plt.show()


def main():
    # file_name = "sequential.json"
    #
    # seq = read_data(file_name, field="unordered_numbers")
    ordered = read_data("sequential.json", "ordered_numbers")
    unordered = read_data("sequential.json", "unordered_numbers")
    sekvencia = read_data("sequential.json", "dna_sequence")
    print(linear_search(ordered, 13))
    print(binary_search(ordered, 13))
    print(cas([100, 500, 1000, 5000, 10000]))
if __name__ == '__main__':
    main()