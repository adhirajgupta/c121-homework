import cv2
import numpy as np


# Starting video
cap = cv2.VideoCapture(0)

while True:
    # Reading camera value
    ret,frame = cap.read()
    # Resizing frame
    frame = cv2.resize(frame,(640,480))

    # Reading image
    img = cv2.imread("download.jpg")
    # Resizing image
    img2 = cv2.resize(img,(640,480))

    # Range of colours that have to be hidden and image has to be shown instead 
    l_black = np.array([30,30,0])
    u_black = np.array([104,153,70])


    # Finding the pixels that are in the range of above
    mask = cv2.inRange(frame,l_black,u_black)
    # Blacks out al the pixels that are to be shown
    res = cv2.bitwise_and(frame,frame,mask=mask)    

    # The minus removes all the black pixels OF THE RES FROM THE FRAME 
    f = frame - res

    # All the black pixels being replaced by the pixels of the image
    d = np.where(f == 0,img2,f)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",d)
    # cv2.imshow("img",f)

    if cv2.waitKey(1) == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
    