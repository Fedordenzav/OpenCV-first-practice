import cv2
import numpy as np

background = cv2.imread('your picture.jpg')
overlay = cv2.imread('your picture.jpg')


if background is None or overlay is None:
    print("Ошибка загрузки изображений.")
    exit()


overlay_resized = cv2.resize(overlay, (background.shape[1], background.shape[0]))

mask = overlay_resized[:, :, 2] 
mask_inv = cv2.bitwise_not(mask)


roi = background[0:overlay_resized.shape[0], 0:overlay_resized.shape[1]]

img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

img_fg = cv2.bitwise_and(overlay_resized, overlay_resized, mask=mask)

dst = cv2.add(img_bg, img_fg)

background[0:overlay_resized.shape[0], 0:overlay_resized.shape[1]] = dst

cv2.imshow('Result', background)
cv2.waitKey(0)
cv2.destroyAllWindows() 
