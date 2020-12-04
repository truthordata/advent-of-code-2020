import os
from math import prod


def get_raw_data(from_dir=None):
    if not from_dir:
        from_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f'{from_dir}/../input.txt', 'r') as f:
        return f.readlines()


def cleaned_data(data):
    return [_.strip('\n') for _ in data]


def get_right_idx(row_size, idx, right_size):
    return ((idx*right_size + 1) % row_size) - 1


def use_down_idx(idx, down_size):
    if down_size > 1:
        return not ((idx + 1) % down_size) - 1
    return True


def get_r_d_path(data, right_size, down_size):
    row_size = len(data[0])
    new_data = [row for idx, row in enumerate(data) if use_down_idx(idx, down_size)]
    return ['X' if row[get_right_idx(row_size, idx, right_size)] == '#' else 'O' for idx, row in enumerate(new_data)]


def get_path_combos(data, *paths):
    counts = []
    for path in paths:
        counts += [len([x for x in get_r_d_path(data, *path) if x=='X'])]
    return prod(counts)
