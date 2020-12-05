from day4.helpers import *

# data = cleaned_data(get_raw_data('/home/tsawicki/gitlab/truthordata/advent-of-code-2020/day-04/day4/'))

if __name__ == '__main__':
    print(len(get_valid_records(
        cleaned_data(get_raw_data()),
        [has_required_fields, valid_byr, valid_iyr, valid_eyr, valid_hgt, valid_hcl, valid_ecl, valid_pid])
    ))
