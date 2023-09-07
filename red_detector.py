import cv2
import numpy as np
import imutils
cap=cv2.VideoCapture(0)
cap.set(6,340)
cap.set(4,480)
center_points=[]
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    cnts=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    cx=0
    cy=0
    red = np.uint8([[[0, 0,255]]])
    hsvRed = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
    #print(hsvRed)
    for c in cnts:
        area=cv2.contourArea(c)
        #cv2.drawContours(frame,c,-1,(0,0,255),3)
        #M=cv2.moments(c)
        if area >1000:
            x,y,w,h =cv2.boundingRect(c)
        
            #print(x,y,h,w)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1)
            cx=int(x+w/2)
            cy=int(y+h/2)
            center_points.append((cx,cy))
            cv2.circle(frame,(cx,cy),5,(255,255,255),-1)
            cv2.putText(frame,"X: "+str(cx)+"  Y: "+str(cy),(cx-20,cy-20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
            if (cx,cy) not in center_points:
                center_points.append()
                start_pt=(cx,cy)
                end_pt=(cx,cy)
                cv2.line(frame,start_pt,end_pt,(255,255,255),2)
            else:
                l=len(center_points)
                for pt in range (l):
                    if not pt+1==l:
                        start_pt=(center_points[pt][0],center_points[pt][1])
                        end_pt=(center_points[pt+1][0],center_points[pt+1][1])
                        cv2.line(frame,start_pt,end_pt,(255,255,255),2)
        
    cv2.imshow("frame",frame)
    k = cv2.waitKey(5) & 0xFF
    if k == ord('q'):
        print(center_points)
        break
cap.release()
cv2.destroyAllWindows()
