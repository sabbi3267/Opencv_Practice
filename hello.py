import cv2 as cv2
import numpy as np

cap = cv2.VideoCapture("red_panda_snow.mp4")

fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("flipped_red_panda.avi", fourcc, 25, (640, 360))

while True:
    ret, frame = cap.read()
    frame2 = cv2.flip(frame, 0)
    
    cv2.imshow("frame2", frame2)
    cv2.imshow("frame", frame)
    
    out.write(frame2)
    
    key = cv2.waitKey(25)
    if key == 27:
        break

out.release()
cap.release()
cv2.destroyAllWindows()