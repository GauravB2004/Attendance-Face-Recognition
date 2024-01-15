# main.py
import add_data_time
import csv_operations as cv
import dict_csv as dict_ops
from datetime import datetime
import detect
import recognize
import os
import cv2

def main():

    image_path= r"/Users/gaurav/Documents/Tech Projects/WiDS-Face-Recognition/Attendance-System/data/known_faces/Example-face-forward-pictures-From-left-to-right-top-to-bottom-anger-contempt.png"
    haar_cascade_path = "/Users/gaurav/Documents/Tech Projects/WiDS-Face-Recognition/Attendance-System/data/haarcascade_frontalface_default.xml" # Replace with the correct path
    
    detect.detect_faces(image_path, haar_cascade_path)

# Path to known face image and the name associated with the known face
    known_image_path = r"/Users/gaurav/Documents/My Documents/Scholarships/New Folder 3/MY PHOTO.jpg"
    known_person_name = "Gaurav"  # Replace with the name of the person in the known face image
# Start face recognition using the webcam
    recognize.recognize_faces_webcam(known_image_path, known_person_name)
 
    




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


