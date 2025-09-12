import cv2


cap = cv2.VideoCapture('https://192.168.1.65:8080/video')
cv2.namedWindow('live cam', cv2.WINDOW_NORMAL)

while cap.isOpened():
    ret, frame = cap.read()

    cv2.imshow('live cam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()