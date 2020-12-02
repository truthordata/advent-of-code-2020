import os

def get_raw_data(dir=None):
    if not dir:
        dir = os.path.dirname(os.path.realpath(__file__))
    with open(f'{dir}/../input.txt', 'r') as f:
        return f.readlines()


def cleaned_data(data):
    return sorted([int(_.strip('\n')) for _ in data])


def get_midpoint_idx(data_list):
    data_len = len(data_list)
    if data_len % 2 == 1:
        return data_len // 2
    return (data_len // 2) - 1


def find_sum_pair(full_data, sum_want, candidate=None, subset_data=None):
    if not candidate:
        candidate = full_data.pop(0)
        subset_data = full_data
    mid_idx = get_midpoint_idx(subset_data)
    check_sum = candidate + subset_data[mid_idx]
    new_subset = []
    if check_sum < sum_want:
        new_subset = subset_data[mid_idx+1:]
    elif check_sum > sum_want:
        new_subset = subset_data[:mid_idx]

    if new_subset:
        return find_sum_pair(full_data, sum_want, candidate, new_subset)
    elif check_sum == sum_want:
        return candidate, subset_data[mid_idx]
    else:
        return find_sum_pair(full_data, sum_want)


if __name__ == '__main__':
    n1, n2 = find_sum_pair(cleaned_data(get_raw_data()), 2020)
    print(f'Numbers are {n1} and {n2}')
    print(f'Solution is {n1 * n2}')
