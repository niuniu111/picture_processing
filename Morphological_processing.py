import cv2 as cv
import numpy as np
def dilate(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.dilate(binary,kernel)
    cv.imshow("dst",dst)

def erode(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.erode(binary,kernel)
    cv.imshow("dst",dst)
def open(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dst = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
    cv.imshow("dst", dst)
def close(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
    dst = cv.morphologyEx(binary,cv.MORPH_CLOSE,kernel)
    cv.imshow("dst", dst)
def top_gray_hat(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.morphologyEx(gray,cv.MORPH_TOPHAT,kernel)
    cimage = np.array(gray.shape,np.uint8)
    cimage = 100
    dst = cv.add(dst,cimage)
    cv.imshow("dst", dst)
def top_hat(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT,(5,5))
    dst = cv.morphologyEx(binary,cv.MORPH_TOPHAT,kernel)
    cimage = np.array(gray.shape,np.uint8)
    cimage = 100
    dst = cv.add(dst,cimage)
    cv.imshow("dst", dst)
def water():
    blurred = cv.pyrMeanShiftFiltering(img,10,100)
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("dst", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel,iterations=2)
    bg = cv.dilate(mb,kernel)
    cv.imshow("dst", bg)
    #distance_transform
    dist =cv.distanceTransform(mb,cv.DIST_L2,3)
    dist_output =  cv.normalize(dist,0,1.0,cv.NORM_MINMAX)
    cv.imshow("distance",dist_output)
    ret,surface = cv.threshold(dist,dist.max()*0.6,255,cv.THRESH_BINARY)
    cv.imshow("surface",surface)
    surface_fg = np.uint8(surface)
    unknow = cv.subtract(bg,surface_fg)
    ret,markers = cv.connectedComponents(surface_fg)
    print(ret)

    #wateredtransfrom
    markers = markers+1
    markers[unknow==255]=0
    markers = cv.watershed(img,markers=markers)
    img[markers==-1]=[0,0,255]
    cv.imshow("result",img)
img = cv.imread("in000001.jpg")
# erode(img)
# dilate(img)
kernel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
# dst = cv.erode(img,kernel)
# dst = cv.dilate(img,kernel)
# open(img)
# close(img)
# cv.imshow("dst",dst)
# top_hat(img)
water()
cv.waitKey()