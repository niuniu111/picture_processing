import cv2 as cv
import numpy as np
def fill_color(image):
    copying = image.copy()
    h,w = image[:2]
    mask = np.zeros([h+2,w+2],np.uint8)
    cv.floodFill(copying,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
    cv.imshow("fill",copying)
    cv.waitKey()
#denosing
def blur(image):
    dst = cv.blur(image,(3,3))#(3,3) representing horizontal ambiguity and total ambiguity.
    cv.imshow("blur",dst)
#denosing of spiced salt and random noise
def median(image):
    dst = cv.blur(image,(3,3))##(3,3) representing horizontal ambiguity and total ambiguity.
    cv.imshow("blur",dst)
def custom_blur(image):
    # dst = cv.medianBlur(image,(3,3))##(3,3) representing horizontal ambiguity and total ambiguity.
    # kernel = np.ones([5,5],np.float32)/25
    kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
    dst = cv.filter2D(image,-1,kernel=kernel)
    cv.imshow("blur",dst)
def clamp(pv):
    if pv>255:
        return 255
    if pv<0:
        return 0
    else:
        return pv
def gaussian_noise(image):
    h,w,c = image.shape
    for row in range(h):
        for col in range(w):
            s = np.random.normal(0,20,3)
            b = image[row,col,0]#blue
            g = image[row, col, 1]#green
            r = image[row,col,2]#red
            image[row,col,0]=clamp(b+s[0])
            image[row, col, 1] = clamp(g + s[1])
            image[row, col, 2] = clamp(r + s[2])
    cv.imshow("noise",image)
def bf_gaussian(image):
    dst = cv.bilateralFilter(image,0,100,15)
    cv.imshow("bi",dst)
    cv.waitKey()
def bf_gaussian1(image):
    dst = cv.pyrMeanShiftFiltering(image,10,15)
    cv.imshow("bi",dst)
    cv.waitKey()
img = cv.imread("in000001.jpg")
t1 = cv.getTickCount()
# roi = img[50:900,29:800]
# blur(img)
# median(img)
# custom_blur(img)
# gaussian_noise(img)
dst = cv.GaussianBlur(img,(0,0),15)
t2 = cv.getTickCount()
t = (t2-t1)/cv.getTickFrequency()
print(t)
cv.imshow("aa",dst)
cv.waitKey()