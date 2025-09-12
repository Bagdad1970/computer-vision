import cv2


def main():
    filename = "image.jpeg"

    rgb_image = cv2.imread(filename)
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HSV)

    cv2.namedWindow("rgb_image")
    cv2.namedWindow("hsv_image")

    cv2.imshow('rgb_image', rgb_image)
    cv2.imshow('hsv_image', hsv_image)

    cv2.waitKey(5)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()