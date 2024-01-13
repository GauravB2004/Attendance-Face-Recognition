# main.py
import cv2
from modules.face_detection import detect_faces
from modules.face_recognition import create_known_faces, recognize_face
from modules.attendance_recorder import record_attendance

# Load Haar cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Paths
known_faces_dir = "data/known_faces"
attendance_log_path = "data/attendance_logs/attendance.csv"

# Create known faces data
known_faces, known_names = create_known_faces(known_faces_dir)

# Start video capture
cap = cv2.VideoCapture(0)

while True:
 ret, frame = cap.read()
 if not ret: break

# Detect faces
faces = detect_faces(frame, face_cascade)

# Loop through faces and recognize them
for (x, y, w, h) in faces:
    face_frame = frame[y:y+h, x:x+w]
    gray_face = cv2.cvtColor(face_frame, cv2.COLOR_BGR2GRAY)

    name = recognize_face(gray_face, known_faces, known_names)
    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Record attendance
    if name != "Unknown":
        record_attendance(name, attendance_log_path)

# Display the resulting frame
cv2.imshow('Video', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):

 cap.release()
 cv2.destroyAllWindows()

