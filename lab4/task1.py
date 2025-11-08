import cv2
import numpy as np

from lab3.functions import gauss_kernel, compute_convulation_matrix


def gauss_blur(image: str, kernel_size: int, sigma):
    img = cv2.imread(image)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img_copy = gray_img.copy()

    cv2.imwrite(f"gray_{image}", gray_img)

    kernel = gauss_kernel(kernel_size, sigma)
    new_matrix = compute_convulation_matrix(gray_img_copy, kernel)
    new_matrix_array = np.array(new_matrix, dtype=np.uint8)

    cv2.imwrite(f'blured_{image}', new_matrix_array)


def main():
    gauss_blur("image.jpg", 3, 2)


if __name__ == '__main__':
    main()