import cv2 as cv

img = cv.imread('photo_2024-06-02_23-34-49.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"

rows, cols, _ = img.shape
res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

M = cv.getRotationMatrix2D(((cols - 1) / 2.0, (rows - 1) / 2.0), 90, 1)

dst = cv.warpAffine(res, M, (cols, rows))

res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

cv.imshow('Original Image', img)
cv.imshow('Resized Image', res)
cv.imshow('Rotated Image', dst)

cv.waitKey(0)