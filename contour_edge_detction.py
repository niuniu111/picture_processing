import cv2 as cv
import numpy as np
def edge(image):
    blurred = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    gradx = cv.Sobel(gray,cv.CV_16SC1,1,0)
    grady = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(gradx,grady,50,150)
    cv.imshow("canny_edage", edge_output)
    return edge_output
def contours(image):
    """
    dst = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    cv.imshow("binary",binary)

    """
    binary = edge(image)
    cloneImage, contours, heriachy = cv.findContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        cv.drawContours(image,contours,i,(0,0,255),2)
        # print(i)
        cv.imshow("detection",image)
def measure_object(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY|cv.THRESH_OTSU)
    print("valu：",ret)
    cv.imshow("binary",binary)
    dst = cv.cvtColor(binary,cv.COLOR_GRAY2BGR)
    outImage,contours,hireachy = cv.findContours(binary,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        area = cv.contourArea(contour)
        x,y,w,h = cv.boundingRect(contour)
        rate = min(w,h)/max(w,h)
        print("rate",rate)
        mm = cv.moments(contour)
        # print(type(mm))class 'dict'
        cx = mm['m10']/mm['m00']
        cy = mm['m01']/mm['m00']
        cv.circle(image,(np.int(cx),np.int(cy)),2,(0,0,255),-1)
        cv.rectangle(dst,(x,y),(x+w,y+h),(0,0,255),2)
        print("area",area)
        approxCurve = cv.approxPolyDP(contour,4,True)
        print(approxCurve.shape)
        if approxCurve.shape[0]==6:
            cv.drawContours(dst,contours,1,(0,255,0),2)
    cv.imshow("measure",image)
img = cv.imread("1.jpg")
# contours(img)
measure_object(img)
cv.waitKey()