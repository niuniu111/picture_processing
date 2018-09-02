import cv2 as cv
import numpy as np
"""
Involves basic operations between pixels.Including add(),sub(),div(),mul() and other 
"""
def add(m1,m2):
    dst =cv.add(m1,m2)
    cv.imshow("dst",dst)
    cv.waitKey()
def sub(m1,m2):
    dst =cv.subtract(m1,m2)
    cv.imshow("dst",dst)
    cv.waitKey()
def div(m1,m2):
    dst =cv.divide(m1,m2)
    cv.imshow("dst",dst)
    cv.waitKey()
def mul(m1,m2):
    dst =cv.multiply(m1,m2)
    cv.imshow("dst",dst)
    cv.waitKey()
def other(m1,m2):
    dst1 = cv.mean(img1)
    dst11 = cv.meanStdDev(img1)
    dst2 = cv.mean(img2)
    dst22 = cv.meanStdDev(img2)
    print(dst1)
    print(dst11)
    print(dst2)
    print(dst22)
def logic(m1,m2):
    # dst = cv.bitwise_and(m1,m2)
    # dst = cv.bitwise_or(m1,m2)
    dst = cv.bitwise_not(m1,m2)
    cv.imshow("dst",dst)
    cv.waitKey()
img1 = cv.imread("in000001.jpg")
img2 = cv.imread("in000002.jpg")
t1 = cv.getTickCount()
# add(img1,img2)
# sub(img1,img2)
# div(img1,img2)
# mul(img1,img2)
# other(img1,img2)
logic(img1,img2)
t2 = cv.getTickCount()
t = (t2-t1)/cv.getTickFrequency()
print(t)