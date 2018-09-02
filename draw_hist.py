import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
def plot(image):
    plt.hist(image.ravel(),256,[0,256])
    plt.show("直方图")
def image_hist(image):
    color = ('blue','green','red')
    for i,color in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])
        plt.plot(hist,color = color)
        plt.xlim([0,256])
    plt.show()
def equalHist(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    dest = cv.equalizeHist(gray)
    cv.imshow("equalHist",dest)
def clahe(image):
    gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    dst = clahe.apply(gray)
    cv.imshow("clash",dst)
def create_rgb(image):
    h,w,c = image.shape
    rgbHist = np.zeros([16*16*16,1],np.float32)
    bsize = 256/16
    for row in range(h):
        for col in range(w):
            b = image[row,col,0]
            g = image[row,col,1]
            r = image[row,col,2]
            index = np.int(b/bsize)*16*16+np.int(g/bsize)*16+np.int(r/bsize)
            rgbHist[np.int(index),0] = rgbHist[np.int(index),0] + 1
    return rgbHist
def hist_compare(image1,image2):
    hist1 = create_rgb(image1)
    hist2 = create_rgb(image2)
    match1 = cv.compareHist(hist1,hist2,cv.HISTCMP_BHATTACHARYYA)
    match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
    match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
    print("巴士距离：%s,相关性：%s,卡方：%s"%(match1,match2,match3))
def hist2d(image):
    hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    hist = cv.calcHist([image],[0,1],None,[180,256],[0,180,0,256])#[180,256]
    # cv.imshow("histd",hist)
    plt.imshow(hist,interpolation='nearest')
    plt.title("2D Histogram")
    plt.show()
def back_projection():
    sample = cv.imread("1.jpg")
    target = cv.imread("in000001.jpg")
    roi_hsv = cv.cvtColor(sample,cv.COLOR_BGR2HSV)
    target_hsv = cv.cvtColor(target,cv.COLOR_BGR2HSV)
    cv.imshow("smple",sample)
    cv.imshow("target",target)
    roiHist = cv.calcHist([roi_hsv],[0,1],None,[180,256],[0,180,0,256])
    cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)
    dst = cv.calcBackProject([target_hsv],[0,1],roiHist,[0,180,0,256],1)
    cv.imshow("back",dst)
img = cv.imread("in000001.jpg")
img1 = cv.imread("1.jpg")
# cv.imshow("1",img)
# cv.imshow("2",img1)
# image_hist(img)
# equalHist(img)
# clahe(img)
# create_rgb(img)
# hist_compare(img,img1)
# hist2d(img)
back_projection()
cv.imshow("src",img)
cv.waitKey()