import cv2


def zoom_image(image_path, zoom_factor):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]

    if zoom_factor > 1:
        center_x, center_y = width // 2, height // 2
        radius_x, radius_y = int(width / zoom_factor / 2), int(height / zoom_factor / 2)
        cropped_image = image[
            center_y - radius_y : center_y + radius_y,
            center_x - radius_x : center_x + radius_x,
        ]
    else:
        padding_x, padding_y = int(width * (1 - zoom_factor) / 2), int(
            height * (1 - zoom_factor) / 2
        )
        cropped_image = cv2.copyMakeBorder(
            image,
            padding_y,
            padding_y,
            padding_x,
            padding_x,
            cv2.BORDER_CONSTANT,
            value=[0, 0, 0],
        )

    zoomed_image = cv2.resize(
        cropped_image, (width, height), interpolation=cv2.INTER_LINEAR
    )

    return zoomed_image


image_path = "image.JPG"
zoom_factor = 1.5
zoomed_image = zoom_image(image_path, zoom_factor)

cv2.imshow("Zoomed Image", zoomed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
