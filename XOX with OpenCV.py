import numpy as np
import cv2 as cv

def printScreen(event,x,y,flags,param):

    if event==cv.EVENT_LBUTTONDOWN:
        if x<300 and x>=0 and y<300 and y>=0:
            cv.circle(bos,(150,150),100,(0,0,255),-1)
            return

        if x<600 and x>=300 and y<300 and y>=0:
            cv.circle(bos,(450,150),100,(0,0,255),-1)
            return

        if x<900 and x>=600 and y<300 and y>=0:
            cv.circle(bos,(750,150),100,(0,0,255),-1)
            return



        if x<300 and x>=0 and y<600 and y>=300:
            cv.circle(bos,(150,450),100,(0,0,255),-1)
            return

        if x<600 and x>=300 and y<600 and y>=300:
            cv.circle(bos,(450,450),100,(0,0,255),-1)
            return

        if x<900 and x>=600 and y<600 and y>=300:
            cv.circle(bos,(750,450),100,(0,0,255),-1)
            return




        if x<300 and x>=0 and y<900 and y>=600:
            cv.circle(bos,(150,750),100,(0,0,255),-1)
            return

        if x<600 and x>=300 and y<900 and y>=600:
            cv.circle(bos,(450,750),100,(0,0,255),-1)
            return

        if x<900 and x>=600 and y<900 and y>=600:
            cv.circle(bos,(750,750),100,(0,0,255),-1)
            return

    elif event==cv.EVENT_RBUTTONDOWN:        
        if x<300 and x>=0 and y<300 and y>=0:
            cv.circle(bos,(150,150),100,(0,255,0),-1)
            return

        if x<600 and x>=300 and y<300 and y>=0:
            cv.circle(bos,(450,150),100,(0,255,0),-1)
            return

        if x<900 and x>=600 and y<300 and y>=0:
            cv.circle(bos,(750,150),100,(0,255,0),-1)
            return



        if x<300 and x>=0 and y<600 and y>=300:
            cv.circle(bos,(150,450),100,(0,255,0),-1)
            return

        if x<600 and x>=300 and y<600 and y>=300:
            cv.circle(bos,(450,450),100,(0,255,0),-1)
            return

        if x<900 and x>=600 and y<600 and y>=300:
            cv.circle(bos,(750,450),100,(0,255,0),-1)
            return



        if x<300 and x>=0 and y<900 and y>=600:
            cv.circle(bos,(150,750),100,(0,255,0),-1)
            return

        if x<600 and x>=300 and y<900 and y>=600:
            cv.circle(bos,(450,750),100,(0,255,0),-1)
            return

        if x<900 and x>=600 and y<900 and y>=600:
            cv.circle(bos,(750,750),100,(0,255,0),-1)
            return

cv.namedWindow(winname="siyah")
bos = np.ones(shape=(900,900,3))
cv.setMouseCallback("siyah",printScreen)


while True:
    cv.imshow("siyah",bos)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()