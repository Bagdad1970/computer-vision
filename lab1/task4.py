import cv2

cap = cv2.VideoCapture('camera-output.avi')

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('copy-camera-output.avi', fourcc, 30, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    out.write(frame)

cap.release()
out.release()
cv2.destroyAllWindows()