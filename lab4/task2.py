import cv2
import numpy as np

def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def gaussian_blur(gray_image, kernel_size=5, sigma=2.5):
    return cv2.GaussianBlur(gray_image, (kernel_size, kernel_size), sigma)

def compute_gradients(blurred_image):
    sobel_x = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]], dtype=np.float32)
    sobel_y = np.array([[-1, -2, -1],
                        [ 0,  0,  0],
                        [ 1,  2,  1]], dtype=np.float32)

    padded = np.pad(blurred_image, pad_width=1, mode='edge')
    rows, cols = blurred_image.shape
    grad_x = np.zeros_like(blurred_image, dtype=np.float32)
    grad_y = np.zeros_like(blurred_image, dtype=np.float32)

    for i in range(rows):
        for j in range(cols):
            roi = padded[i:i+3, j:j+3]
            grad_x[i, j] = np.sum(roi * sobel_x)
            grad_y[i, j] = np.sum(roi * sobel_y)

    return grad_x, grad_y

def compute_magnitude_and_direction(grad_x, grad_y):
    magnitude = np.sqrt(grad_x ** 2 + grad_y ** 2)
    direction = np.arctan2(grad_y, grad_x)
    return magnitude, direction

def non_maximum_suppression(magnitude, direction):
    suppressed = np.zeros_like(magnitude, dtype=np.float32)
    angle = direction * 180.0 / np.pi
    angle[angle < 0] += 180

    for i in range(1, magnitude.shape[0] - 1):
        for j in range(1, magnitude.shape[1] - 1):
            q = 255
            r = 255

            if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                q = magnitude[i, j + 1]
                r = magnitude[i, j - 1]
            elif 22.5 <= angle[i, j] < 67.5:
                q = magnitude[i + 1, j - 1]
                r = magnitude[i - 1, j + 1]
            elif 67.5 <= angle[i, j] < 112.5:
                q = magnitude[i + 1, j]
                r = magnitude[i - 1, j]
            elif 112.5 <= angle[i, j] < 157.5:
                q = magnitude[i - 1, j - 1]
                r = magnitude[i + 1, j + 1]

            if magnitude[i, j] >= q and magnitude[i, j] >= r:
                suppressed[i, j] = magnitude[i, j]
            else:
                suppressed[i, j] = 0

    return suppressed


def double_threshold(suppressed_image, low_level, high_level):
    strong = suppressed_image >= high_level
    weak = (suppressed_image >= low_level) & (suppressed_image < high_level)

    edges = np.zeros_like(suppressed_image, dtype=np.uint8)
    edges[strong] = 255
    edges[weak] = 75
    return edges


def hysteresis(edges):
    rows, cols = edges.shape
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if edges[i, j] == 75:
                if np.any(edges[i-1 : i+2, j-1 : j+2] == 255):
                    edges[i, j] = 255
                else:
                    edges[i, j] = 0

    return edges


def canny_edge_detector(image, blur_kernel_size=5, sigma=2.5):
    gray = grayscale(image)
    blurred = gaussian_blur(gray, blur_kernel_size, sigma)
    grad_x, grad_y = compute_gradients(blurred)
    magnitude, direction = compute_magnitude_and_direction(grad_x, grad_y)
    suppressed = non_maximum_suppression(magnitude, direction)

    cv2.imwrite("custom-canny-suppressed.jpg", suppressed)

    max_grad = np.max(suppressed)
    low_level = max_grad // 15
    high_level = max_grad // 8

    edges = double_threshold(suppressed, low_level, high_level)

    cv2.imwrite("custom-canny-double-thresholding.jpg", edges)

    final_edges = hysteresis(edges)
    return final_edges

def main():
    image = cv2.imread('image.jpg')

    edges = canny_edge_detector(image, sigma=2.5)

    cv2.imwrite("custom-canny.jpg", edges)
    cv2.imwrite("built-in-canny.jpg", cv2.Canny(image, 100, 150))


if __name__ == "__main__":
    main()