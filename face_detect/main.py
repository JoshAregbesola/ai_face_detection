import cv2

# Load Haar Cascade model for face detection
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_faces(img):
    if img is None:
        return None  # No frame captured from camera
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    # If no faces detected, just return the image
    if len(faces) == 0:
        return img

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return img


# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam. Make sure it's connected and not in use.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame. Check your camera or permissions.")
        break

    frame = detect_faces(frame)
    if frame is None:
        continue

    cv2.imshow('Face Detection', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()