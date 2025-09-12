import cv2
import numpy as np


def find_the_closest_color(pixel: np.ndarray) -> tuple:
    the_closest_color = np.argmax(pixel)

    if the_closest_color == 0:
        return 255, 0, 0
    elif the_closest_color == 1:
        return 0, 255, 0
    elif the_closest_color == 2:
        return 0, 0, 255

    return 0, 0, 0


cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


rect_width = 200
rect_height = 60

center_x = frame_width // 2
center_y = frame_height // 2

horz_pt1 = (center_x - rect_width // 2, center_y - rect_height // 2)
horz_pt2 = (center_x + rect_width // 2, center_y + rect_height // 2)

vert_pt1 = (center_x - rect_height // 2, center_y - rect_width // 2)
vert_pt2 = (center_x + rect_height // 2, center_y + rect_width // 2)


while True:
    ret, frame = cap.read()
    if not ret:
        break

    central_pixel = frame[frame_height // 2, frame_width // 2]

    the_closes_color = find_the_closest_color(central_pixel)

    cv2.rectangle(frame, horz_pt1, horz_pt2, the_closes_color, -1)
    cv2.rectangle(frame, vert_pt1, vert_pt2, the_closes_color, -1)

    cv2.imshow('result', frame)

    char = cv2.waitKey(5)
    if char == 27:
        break

cap.release()
cv2.destroyAllWindows()