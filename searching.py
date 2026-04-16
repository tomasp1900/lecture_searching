import os
import json


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

def pattern_search(seq, pattern):

    indicies = set()
    pattern_size = len(pattern)

    left_idx = 0
    right_idx = pattern_size
    while right_idx< len(seq):
        for idx in range(pattern_size):
            if pattern[idx] != seq[left_idx + idx]:
                break
            else:
                indicies.add(left_idx + pattern_size // 2)

            left_idx += 1
            right_idx += 1
        return indicies



def binary_search(seq, number):
    left, right = (0, len(seq) - 1)

    while left <= right:
        middle = (right + left) // 2

        if number < seq[middle]:
            right = middle - 1
        elif number > seq[middle]:
            left = middle + 1
        else:
            return
    return


def main():
    file_name = "sequential.json"

    seq = read_data(file_name, field="unordered_numbers")
    # print(seq)
    print(linear_search([-51, -12, -3, -3, -1, 2, 8, 13, 14, 14, 14, 21, 22, 23, 24, 25, 48, 63, 64, 70, 72, 78, 90, 102, 120], 14))

if __name__ == '__main__':
    main()