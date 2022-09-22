#By This Program you can use Your Phone Camera to Create Computer Vision Application

import cv2
import numpy as np

url = "Your IP Address/video" #Enter Your IP Address Which is Given by IP WebCam App
cp = cv2.VideoCapture(url)
while(True):
    camera, frame = cap.read()
    if frame is not None:
        cv2.imshow("Frame", frame)
    q = cv2.waitKey(1)
    if q==ord("q"):
        break
cv2.destroyAllWindows()  #Closes All Windows For you