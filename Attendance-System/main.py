# main.py
import add_data_time
import csv_operations as cv
import dict_csv as dict_ops


def main():
    # Using functions from add_data_time.py
    csv_file_path = 'example_with_timestamp.csv'
    csv_header = ['Timestamp', 'Name', 'Age', 'City']
    add_data_time.create_csv_file(csv_file_path, csv_header)
    add_data_time.add_data_to_csv(csv_file_path, ['Alice', 25, 'New York'])
    add_data_time.add_data_to_csv(csv_file_path, ['Bob', 30, 'San Francisco'])
    add_data_time.read_csv_file(csv_file_path)

    # Using functions from cv.py
    cv_data = [
        ['Name', 'Age', 'City'],
        ['Alice', 25, 'New York'],
        ['Bob', 30, 'San Francisco'],
        ['Charlie', 22, 'Chicago']
    ]
    cv.write_data_to_csv('example.csv', cv_data)

    # Using functions from dict.py
    dict_data = {'Name': 'Alice', 'Age': 25, 'City': 'New York'}
    dict_fieldnames = ['Name', 'Age', 'City']
    dict_ops.write_dict_to_csv('dict.csv', dict_fieldnames, dict_data)

if __name__ == "__main__":
    main()
