import cv2 as cv
import numpy as np
def template():
    img = cv.imread('pic.jpg')
    template = cv.imread('template.jpg')
    method = [cv.TM_SQDIFF_NORMED,cv.TM_CCORR_NORMED,cv.TM_CCOEFF_NORMED]
    th,tw = template.shape[:2]
    for md in method:
        print(md)
        result = cv.matchTemplate(img,template,md)
        min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
        if md == cv.TM_SQDIFF_NORMED:
            tl = min_loc
        else:
            tl = max_loc
        br = (tl[0]+tw,tl[1]+th)
        cv.rectangle(img,tl,br,(0,0,255),2)
        # cv.imshow("match"+np.str(md),img)
        cv.imshow("match" + np.str(md), result)
        cv.waitKey()
template()