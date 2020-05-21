import cv2
import numpy as np

wang = cv2.VideoCapture('wang.flv')
print(wang)
flag, frame = wang.read()
print(flag, frame.shape)
fps= wang.get(propId= cv2.CAP_PROP_FPS)
print(fps, 1000/fps)
print(wang.get(propId=cv2.CAP_PROP_FRAME_COUNT))

# cv2.imshow('frame',frame)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
while wang.isOpened():      # Draw the circle while the video is open
    flag, frame = wang.read()
    face = detector.detectMultiScale(frame, scaleFactor= 1.2 , minNeighbors=5)   # The object which contained the facial_zone. 
    for x,y,w,h in face:
        cv2.circle(frame , center=(x+w//2,y+h//2), radius= w//2, color=[0,0,255], thickness=2)  # Draw a circle in people's faces
    cv2.imshow('wang', frame)
    if flag == False:
        break;
    if ord('q') == cv2.waitKey(15):     # Enter q to quit the video
        break;

cv2.destroyAllWindows()
