import cv2 as cv
import numpy as np
#全局阈值
def threshold(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    # ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_TRIANGLE)#用于单峰波
    ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)#自己指定,常用
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY_INV)
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TRUNC)#截断
    # ret, binary = cv.threshold(gray, 127, 255, cv.THRESH_TOZERO)
    print("value %s"%ret)
    cv.imshow("bin",binary)
    cv.waitKey()
def local_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,25,10,)#25必须是奇数
    cv.imshow("bin", dst)
    cv.waitKey()

def custom_threshold(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    h,w = gray.shape[:2]
    m = np.reshape(gray,[1,w*h])
    mean = m.sum()/(w*h)
    print("mean:%s"%mean)
    ret,binary = cv.threshold(gray,mean,255,cv.THRESH_BINARY)
    cv.imshow("bin", binary)
    cv.waitKey()
def big_image(image):
   cw = 128
   ch = 128
   h,w = image.shape[:2]
   gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
   for row in range(0,h,ch):
       for col in range(0,w,ch):
           roi = gray[row:row+ch,col:col+cw]
           dst = cv.adaptiveThreshold(roi,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,127,20)
           # ret,dst = cv.threshold(roi,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
           gray[row:row + ch, col:col + cw] = dst
           print(np.std(roi),np.mean(roi))
   cv.imwrite("ma.jpg",gray)
img = cv.imread("in000001.jpg")
# img = cv.imread("1.jpg")
# threshold(img)
# local_threshold(img)
# custom_threshold(img)
big_image(img)