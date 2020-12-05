import os
from copy import deepcopy

def get_raw_data(from_dir=None):
    if not from_dir:
        from_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f'{from_dir}/../input.txt', 'r') as f:
        return f.readlines()


def cleaned_data(data):
    recs = []
    rec = {}
    for line in data:
        if line == '\n':
            recs += [deepcopy(rec)]
            rec = {}
        else:
            for pair in line.replace('\n', '').split(' '):
                k,v = pair.split(":")
                rec[k] = v
    if rec:
        recs += [rec]
    return recs


def has_required_fields(rec):
    return not {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} - set(rec.keys())


def check_between(val, minv, maxv):
    return minv <= val <= maxv


def valid_byr(rec):
    return check_between(int(rec['byr']), 1920, 2002)


def valid_iyr(rec):
    return check_between(int(rec['iyr']), 2010, 2020)


def valid_eyr(rec):
    return check_between(int(rec['eyr']), 2020, 2030)


def valid_hgt(rec):
    hgt = rec['hgt']
    if 'cm' in hgt:
        return check_between(int(hgt[:-2]), 150, 193)
    elif 'in' in hgt:
        return check_between(int(hgt[:-2]), 59, 76)
    return False


def valid_hcl(rec):
    hcl = rec['hcl']
    if hcl[0] == '#' and len(hcl) == 7:
        return not set(hcl[1:]) - set('0123456789abcdef')
    return False


def valid_ecl(rec):
    return not {rec['ecl']} - {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def valid_pid(rec):
    pid = rec['pid']
    return len(pid) == 9 and pid.isnumeric()


def valid_record(rec, checks):
    for func in checks:
        valid = func(rec)
        if not valid:
            return False
    return True


def get_valid_records(data, funcs):
    return [rec for rec in data if valid_record(rec, funcs)]

