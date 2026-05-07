#image translation 
import cv2
import numpy as np 
import matplotlib.pyplot as plt
image = cv2.imread(r'C:\Users\dpand\Pictures\retriver.webp')
height , width = image.shape[:2]
quarter_height , quarter_width = height/2, width/2

T = np.float32([[1,0,quarter_width],[0,1,quarter_height]])
img_translation = cv2.warpAffine(image,T,(width,height))
cv2.imshow('Translation',img_translation)
cv2.waitKey(0)
cv2.destroyAllWindows()

#different translation onn same image

img = cv2.imread('C:\\Users\\dpand\\Pictures\\retriver.webp')
rows, cols, _ = img.shape

M_left = np.float32([[1, 0, -50], [0, 1, 0]])
M_right = np.float32([[1, 0, 50], [0, 1, 0]])
M_top = np.float32([[1, 0, 0], [0, 1, 50]])
M_bottom = np.float32([[1, 0, 0], [0, 1, -50]])

img_left = cv2.warpAffine(img, M_left, (cols, rows))
img_right = cv2.warpAffine(img, M_right, (cols, rows))
img_top = cv2.warpAffine(img, M_top, (cols, rows))
img_bottom = cv2.warpAffine(img, M_bottom, (cols, rows))

plt.subplot(221), plt.imshow(img_left), plt.title('Left')
plt.subplot(222), plt.imshow(img_right), plt.title('Right')
plt.subplot(223), plt.imshow(img_top), plt.title('Top')
plt.subplot(224), plt.imshow(img_bottom), plt.title('Bottom')
plt.show()