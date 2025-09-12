import cv2


cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('camera-output.avi', fourcc, 30.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('result', frame)
    out.write(frame)

    char = cv2.waitKey(5)
    if char == 27:
        break



cap.release()
out.release()
cv2.destroyAllWindows()