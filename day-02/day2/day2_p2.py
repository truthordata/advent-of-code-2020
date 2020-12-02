from day2.helpers import get_raw_data, cleaned_data

data = cleaned_data(get_raw_data())


def compare_str(pw_check, idx):
    return pw_check[-1][int(pw_check[idx])-1] == pw_check[2]


def get_valid_passwords(data):
    return [pw_check for pw_check in data if (compare_str(pw_check, 0) ^ compare_str(pw_check, 1))]


if __name__ == '__main__':
    print(len(get_valid_passwords(data)))