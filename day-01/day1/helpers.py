import os


def get_raw_data(from_dir=None):
    if not from_dir:
        from_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f'{from_dir}/../input.txt', 'r') as f:
        return f.readlines()


def cleaned_data(data):
    return sorted([int(_.strip('\n')) for _ in data])
