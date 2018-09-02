import cv2 as cv
import numpy as np

def sobel(image):
    # grad_x = cv.Sobel(image,cv.CV_32F,1,0)
    grad_x = cv.Scharr(image, cv.CV_32F, 1, 0)#Sensitivity to noise
    grad_y = cv.Sobel(image, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x)#Negative number for absolute value. Go to the 8 bit
    grady = cv.convertScaleAbs(grad_y)
    cv.imshow("x",gradx)
    cv.imshow("y",grady)
    gradxy = cv.addWeighted(grad_x,0.5,grad_y,0.5,0)
    cv.imshow("xy", gradxy)
    cv.waitKey()
def lapalian(image):
    # dst = cv.Laplacian(image,cv.CV_32F)
    # lpls = cv.convertScaleAbs(dst)
    kernel = np.array([[0,1,0],[1,-4,1],[0,1,1]])
    dst = cv.filter2D(image,cv.CV_32F,kernel=kernel)
    lpls = cv.convertScaleAbs(dst)
    cv.imshow("lpls", lpls)
    cv.waitKey()

def edge(image):
    blurred = cv.GaussianBlur(image,(3,3),0)
    gray = cv.cvtColor(blurred,cv.COLOR_BGR2GRAY)
    gradx = cv.Sobel(gray,cv.CV_16SC1,1,0)
    grady = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    edge_output = cv.Canny(gradx,grady,50,150)
    cv.imshow("canny_edage", edge_output)

    dst = cv.bitwise_and(image,image,mask=edge_output)
    cv.imshow("color", dst)
def line_detection(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize=3)
    lines = cv.HoughLines(edges,1,np.pi/180,200)
    for line in lines:
        rho,theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0+1000*(-b))
        y1 = int(y0+1000*(-a))
        x2 = int(x0-1000*(-b))
        y2 = int(y0-1000*(-a))
        cv.line(image,(x1,y1),(x2,y2),(0,0,255),1)
    cv.imshow("image",image)
def line_detect_possible(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=50,maxLineGap=10)
    for line in lines:
        print(type(line))
        x1,y1,x2,y2 = line[0]
        cv.line(image, (x1, y1), (x2, y2), (0, 0, 255), 1)
    cv.imshow("image", image)
def detection_circle(image):
    dst = cv.pyrMeanShiftFiltering(image,10,100)
    gray = cv.cvtColor(dst,cv.COLOR_BGR2GRAY)
    circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.round(circles))
    for i in circles[0,:]:
        cv.circle(image,(i[0],i[1]),i[2],(0,0,255),2)
        cv.circle(image, (i[0], i[1]), 2, (255, 0, 0), 2)
    cv.imshow("image", image)
img = cv.imread("in000001.jpg")
# img = cv.imread("1.jpg")
# sobel(img)
# lapalian(img)
# edge(img)
# line_detection(img)
# line_detect_possible(img)
detection_circle(img)
cv.waitKey()