import cv2 as cv
import numpy as np
def pyramid(image):
    level = 3
    temp = image.copy()
    pyramid_images = []
    for i in range(level):
        dst = cv.pyrDown(temp)
        pyramid_images.append(dst)
        cv.imshow("pyramid_image"+str(i),dst)
        temp = dst.copy()
    return pyramid_images
def lapalian(image):
    pyramid_images = pyramid(image)
    level = len(pyramid_images)
    for i in range(level-1,-1,-1):
        if (i-1)<0:
            expand = cv.pyrUp(pyramid_images[i],dstsize=image.shape[:2])
            lpls = cv.subtract(image,expand)
            cv.imshow("lapali_image" + str(i), lpls)
        else:
            expand = cv.pyrUp(pyramid_images[i], dstsize=pyramid_images[i-1].shape[:2])
            lpls = cv.subtract(pyramid_images[i-1], expand)
            cv.imshow("lapali_image" + str(i), lpls)
img = cv.imread("in000001.jpg")#必须是2的n次方尺寸，否则会出错 
cv.imshow("image",img)
# pyramid(img)
lapalian(img)
cv.waitKey()