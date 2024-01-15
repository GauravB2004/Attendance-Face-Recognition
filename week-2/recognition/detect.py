import cv2

def detect_faces(image_path, cascade_path):
    # Load the image and resize it for better display
    img = cv2.imread("/Users/gaurav/Documents/Tech Projects/WiDS-Face-Recognition/Attendance-System/data/known_faces/Example-face-forward-pictures-From-left-to-right-top-to-bottom-anger-contempt.png")
    img = cv2.resize(img, (640, 480))

    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Load the Haar Cascade Classifier for face detection
    face_cascade = cv2.CascadeClassifier("/Users/gaurav/Downloads/haarcascade_frontalface_default.xml")
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=3)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    # Display the image with rectangles around detected faces
    cv2.imshow("Detected Faces", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
