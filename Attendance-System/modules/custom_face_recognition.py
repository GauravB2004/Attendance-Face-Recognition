import cv2
import face_recognition
import os

def recognize_faces_webcam():
    known_faces = {
        # Add your known faces here
    }

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            continue

     # Convert the image from BGR color (which OpenCV uses) to RGB
       # color (face_recognition uses)
        rgb_frame = frame[:, :, ::-1]

        # Find all face locations and face encodings in the RGB frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face matches any known faces
         matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)
         name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = list(known_faces.keys())[first_match_index]

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
        

         video_capture.release()
         cv2.destroyAllWindows()


