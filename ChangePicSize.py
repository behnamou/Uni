import cv2
import numpy as np

originalImagePath = "image_01.jpg"
originalImage = cv2.imread(originalImagePath)

originalImageHeight, originalImageWidth, originalImageChannels = originalImage.shape

croppedImageHeight = originalImageHeight - (originalImageHeight % 3)
croppedImageWidth = originalImageWidth - (originalImageWidth % 3)

croppedImage = originalImage[:croppedImageHeight, :croppedImageWidth]


sectionsHeight = croppedImageHeight // 3
sectionsWidth = croppedImageWidth // 3


croppedImageArray = []
for i in range(3):
    rowParts = []
    for j in range(3):
        xStart = j * sectionsWidth
        yStart = i * sectionsHeight
        xEnd = (j + 1) * sectionsWidth
        yEnd = (i + 1) * sectionsHeight

        part = originalImage[yStart:yEnd, xStart:xEnd]

        rowParts.append(part)

    croppedImageArray.append(rowParts)


newImages = []
for i in range(3):
    rowParts = []
    for j in range(3):
        tempImage = np.zeros((sectionsHeight, sectionsWidth, 3), dtype=np.uint8)
        tempImage[:] = (255, 255, 255)
        rowParts.append(tempImage)

    newImages.append(rowParts)

newFlatImages = []
for i in range(3):
    rowParts = []
    for j in range(3):
        tempImage = np.zeros((sectionsHeight, sectionsWidth, 3), dtype=np.uint8)
        tempImage[:] = (255, 255, 255)
        tempImage2 = tempImage.reshape(-1, originalImageChannels)
        rowParts.append(tempImage2)
    newFlatImages.append(rowParts)

squareIndex = 0
for i in range(0, croppedImageHeight, 3):
    for j in range(0, croppedImageWidth, 3):
        square = croppedImage[i : i + 3, j : j + 3]

        for row in range(3):
            for col in range(3):
                newFlatImages[row][col][squareIndex] = square[row, col]

        squareIndex += 1


for i in range(3):
    for j in range(3):
        newImages[i][j] = newFlatImages[i][j].reshape(sectionsHeight, sectionsWidth, 3)


for i in range(3):
    for j in range(3):
        cv2.imshow(f"Part {i}_{j}", newImages[i][j])
cv2.waitKey(0)
cv2.destroyAllWindows()
