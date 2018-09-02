import cv2 as cv
import numpy as np
def create_image():
    """
    img = np.zeros([400,400,3],np.uint8)#mul_channel
    # img[:,:,0] = np.ones([400,400])*255#blue
    img[:, :, 1] = np.ones([400, 400]) * 255  # green
    cv.imshow("a", img)
    img = np.zeros([400, 400, 1], np.uint8)  # singel_channel
    img[:,:,0] = np.ones([400,400])*255#blue
    img[:, :, 0] = np.ones([400, 400]) * 127  # green

    """
    img = np.ones([400, 400, 1], np.uint8)  # singel_channel
    img = img*127
    cv.imshow("a", img)
def inverse():
    dst = cv.bitwise_not(img)
    cv.imshow("img",dst)
def color_space_image(img):
    dst = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    cv.imshow("img",dst)
def extrace_object_demo():
    capture = cv.VideoCapture("1.avi")
    while(True):
        ret,frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([37, 43, 46])
        upper_hsv = np.array([77, 255, 255])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        dst = cv.bitwise_and(frame,frame,mask=mask)
        cv.imshow("video",frame)
        cv.imshow("video", mask)
        c = cv.waitKey(20)
        if c == 27:
            break
def contrast_brightness(image, c, b):
    h,w,c = image.shape
    black = np.zeros([h,w,c],image.dtype)
    dst = cv.addWeighted(image,c,black,1-c,b)
img = cv.imread("in000001.jpg")
# b,g,r = cv.split(img)
# cv.imshow("b",b)
# cv.imshow("g",g)
# cv.imshow("r",r)
# img[:,:,2] = 0
# img = cv.merge([b,g,r])
cv.imshow("aa",img)
t1 = cv.getTickCount()
# create_image()
inverse()
# color_space_image(img)
# extrace_object_demo()
# contrast_brightness(img,1.2,10)
t2 = cv.getTickCount()
t = (t2-t1)/cv.getTickFrequency()
t = t*1000
# cv.imshow("a",img)
cv.waitKey()
print(t)