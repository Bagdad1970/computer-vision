import cv2


cap = cv2.VideoCapture("copy-camera-output.avi")

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    b,g,r = cv2.split(frame)
    new_frame = cv2.merge((b, g, r + 100))

    new_frame = cv2.resize(new_frame, (1280, 960))

    cv2.imshow('result', new_frame)

    char = cv2.waitKey(5)
    if char == 27:
        break


cap.release()
cv2.destroyAllWindows()