import cv2

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


rect_width = 200
rect_height = 60
rect_thickness = 2

while True:
    ret, frame = cap.read()
    if not ret:
        break

    center_x = frame_width // 2
    center_y = frame_height // 2

    horz_pt1 = (center_x - rect_width // 2, center_y - rect_height // 2)
    horz_pt2 = (center_x + rect_width // 2, center_y + rect_height // 2)
    cv2.rectangle(frame, horz_pt1, horz_pt2, (0, 0, 255), rect_thickness)

    vert_pt1 = (center_x - rect_height // 2, center_y - rect_width // 2)
    vert_pt2 = (center_x + rect_height // 2, center_y + rect_width // 2)
    cv2.rectangle(frame, vert_pt1, vert_pt2, (0, 0, 255), rect_thickness)

    cv2.imshow('result', frame)

    char = cv2.waitKey(5)
    if char == 27:
        break

cap.release()
cv2.destroyAllWindows()