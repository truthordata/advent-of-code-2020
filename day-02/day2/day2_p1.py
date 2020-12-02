from day2.helpers import get_raw_data, cleaned_data

data = cleaned_data(get_raw_data())


def get_valid_passwords(data):
    return [pw_check[-1] for pw_check in data if int(pw_check[0]) <= pw_check[-1].count(pw_check[2]) <= int(pw_check[1])]


if __name__ == '__main__':
    print(len(get_valid_passwords(data)))