from day3.helpers import get_raw_data, cleaned_data, get_path_combos

if __name__ == '__main__':
    print(get_path_combos(cleaned_data(get_raw_data()), (3,1)))