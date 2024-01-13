import cv2
import face_recognition
from datetime import datetime
import csv

# Import your custom face recognition module
from modules import custom_face_recognition

# CSV file handling
def add_data_to_csv(file_path, data):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data_with_timestamp = [timestamp] + data
    
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data_with_timestamp)
    print(f'Data added to CSV file "{file_path}": {data_with_timestamp}')

# Initialize CSV file for attendance
attendance_csv_path = 'attendance_records.csv'

def record_attendance(name):
    data = [name]
    add_data_to_csv(attendance_csv_path, data)

# Function to integrate face recognition and attendance recording
def recognize_and_record(frame, known_faces):
    rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = list(known_faces.keys())[first_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
        
        if name != "Unknown":
            record_attendance(name)

# Load known faces (populate this with actual data)
known_faces = {
    # "PersonName": face_encoding,
}

# Start video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    recognize_and_record(frame, known_faces)

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
