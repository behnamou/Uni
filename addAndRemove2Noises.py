import cv2 as cv
import numpy as np
import random
import math

img_path = "dog.jpg"
img = cv.imread(img_path)
img_gaussian = img.copy()
img_uniform = img.copy()
img_gaussian_denoised = img.copy()
img_uniform_denoised = img.copy()

height = img.shape[0]
width = img.shape[1]


def add_gaussian_noise(image, height, width, mean=0, std_dev=25):
    for y in range(height):
        for x in range(width):
            noise = random.gauss(mean, std_dev)
            for c in range(3):
                noisy_value = image[y, x, c] + noise
                image[y, x, c] = max(0, min(255, noisy_value))
    return image


def remove_gaussian_noise(image, height, width):
    output = np.zeros_like(image)
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            for c in range(3):
                neighborhood = [
                    image[y - 1, x - 1, c],
                    image[y - 1, x, c],
                    image[y - 1, x + 1, c],
                    image[y, x - 1, c],
                    image[y, x, c],
                    image[y, x + 1, c],
                    image[y + 1, x - 1, c],
                    image[y + 1, x, c],
                    image[y + 1, x + 1, c],
                ]
                output[y, x, c] = int(np.mean(neighborhood))
    return output


def add_uniform_noise(image, height, width, intensity=50):
    for y in range(height):
        for x in range(width):
            noise = random.uniform(-intensity, intensity)
            for c in range(3):
                noisy_value = image[y, x, c] + noise
                image[y, x, c] = max(0, min(255, noisy_value))
    return image


def remove_uniform_noise(image, height, width):
    output = np.zeros_like(image)
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            for c in range(3):
                neighborhood = [
                    image[y - 1, x - 1, c],
                    image[y - 1, x, c],
                    image[y - 1, x + 1, c],
                    image[y, x - 1, c],
                    image[y, x, c],
                    image[y, x + 1, c],
                    image[y + 1, x - 1, c],
                    image[y + 1, x, c],
                    image[y + 1, x + 1, c],
                ]
                output[y, x, c] = int(np.median(neighborhood))
    return output


img_gaussian = add_gaussian_noise(img_gaussian, height, width)
img_uniform = add_uniform_noise(img_uniform, height, width)

img_gaussian_denoised = remove_gaussian_noise(img_gaussian, height, width)
img_uniform_denoised = remove_uniform_noise(img_uniform, height, width)

cv.imshow("Original Image", img)
cv.imshow("Gaussian Noise", img_gaussian)
cv.imshow("Gaussian Noise Removed", img_gaussian_denoised)
cv.imshow("Uniform Noise", img_uniform)
cv.imshow("Uniform Noise Removed", img_uniform_denoised)

cv.waitKey(0)
cv.destroyAllWindows()
