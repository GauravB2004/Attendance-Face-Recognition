# make a folder, put this file in that folder and open that folder with VS code (make that folder as directory).
import csv

fieldnames = ['Name', 'Age', 'City']
with open('dict.csv',mode= 'w', newline='') as file:
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()
    csv_writer.writerow({'Name': 'Gaurav', 'Age': 19, 'City': 'Mumbai'})

def write_dict_to_csv(file_path, fieldnames, data):
    with open(file_path, mode='w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerow(data)
    print(f'Data has been written to {file_path}') 