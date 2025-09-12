import cv2


def main():
    filename = "image.jpeg"

    img1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    img2 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread(filename, cv2.IMREAD_COLOR)

    cv2.namedWindow("orig_image", cv2.WINDOW_NORMAL)
    cv2.namedWindow("gray_image", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("color_image", cv2.WINDOW_NORMAL)

    cv2.imshow("orig_image", img1)
    cv2.imshow("gray_image", img2)
    cv2.imshow("color_image", img3)

    cv2.waitKey(5)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
