from math import prod
from itertools import combinations
from day1.helpers import get_raw_data, cleaned_data


def dumb_brute_force(data, n_count, desired_sum):
    return [tup for tup, s in {tup: sum(tup) for tup in combinations(data, n_count)}.items() if s == desired_sum][0]


if __name__ == '__main__':
    n = dumb_brute_force(cleaned_data(get_raw_data()), 3, 2020)
    print(f'Numbers are {n}')
    print(f'Solution is {prod(n)}')
