from math import prod
from itertools import combinations
from day1.helpers import get_raw_data, cleaned_data
import timeit
from copy import deepcopy

def dumb_brute_force(data, n_count, desired_sum):
    return [tup for tup, s in {tup: sum(tup) for tup in combinations(data, n_count)}.items() if s == desired_sum][0]


if __name__ == '__main__':
    # n = dumb_brute_force(cleaned_data(get_raw_data()), 3, 2020)
    # print(f'Numbers are {n}')
    # print(f'Solution is {prod(n)}')
    data = cleaned_data(get_raw_data())
    print(timeit.timeit('dumb_brute_force(deepcopy(data), 2, 2020)', number=10, globals=globals()))
    print(timeit.timeit('dumb_brute_force(deepcopy(data), 3, 2020)', number=10, globals=globals()))