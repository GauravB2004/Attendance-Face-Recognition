import cv2
import face_recognition
import numpy 

def recognize_faces_webcam(known_image_path, known_person_name):
    # known_image_path ="/Users/gaurav/Documents/My Documents/Scholarships/New Folder 3/MY PHOTO.jpg"
    # known_person_name="Gaurav"   
    # Load face encoding for the known face
    
    known_image = face_recognition.load_image_file(known_image_path)
    known_face_encoding = face_recognition.face_encodings(known_image)[0]

    # Open the webcam
    video_capture = cv2.VideoCapture(0)
    print("opened")


    while True:
        # Capture each frame from the webcam
        ret, frame = video_capture.read()
        if not ret:
             print("Failed to grab a frame from the webcam")
             break
        # Find all face locations and face encodings in the frame
        rgb_small_frame = numpy.ascontiguousarray(frame[:, :, ::-1])

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations ) # Updated this line
       
        # Loop through each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Check if the face matches the known face
            matches = face_recognition.compare_faces([known_face_encoding], face_encoding)
            name = "Unknown"

            # If a match is found, use the name of the known face
            if matches[0]:
                name = known_person_name

            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 1)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

recognize_faces_webcam("/Users/gaurav/Documents/My Documents/Scholarships/New Folder 3/MY PHOTO.jpg" , "Gaurav")