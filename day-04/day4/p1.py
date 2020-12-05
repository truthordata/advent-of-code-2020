from day4.helpers import get_raw_data, cleaned_data, get_valid_records, has_required_fields

data = cleaned_data(get_raw_data('/home/tsawicki/gitlab/truthordata/advent-of-code-2020/day-04/day4/'))

if __name__ == '__main__':
    print(len(get_valid_records(cleaned_data(get_raw_data()), [has_required_fields])))