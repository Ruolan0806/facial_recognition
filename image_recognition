import cv2
import numpy as np
# gray = cv2.cvtColor(picture,code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # cv2.imwrite('gray.JPG',gray)
# # another = cv2.cvtColor(picture, code=cv2.COLOR_BGR2BGRA)
# # cv2.imshow('other',another)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# print(picture.shape)
# p2 = cv2.resize(picture, dsize=(188*2,420))
# cv2.imshow('other',p2)
# if cv2.waitKey() == ord('q'):
#     cv2.destroyAllWindows()
b= cv2.imread('14.jpg')
print(b.shape)
bb= cv2.resize(b,dsize=(400,460))
# cv2.imshow('family', bb)
# cv2.waitKey(5000)
# cv2.destroyAllWindows()
detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml') #returns a detector for classfier
face = detector.detectMultiScale(b, scaleFactor=1.3, minNeighbors= 5 , minSize=(20,20))
print(face)   #find out what kind of information is contained in the returned value
for x,y,h,w in face:
    cv2.rectangle(b, (x, y), (x+w, y+h), color=(0, 255, 0), thickness= 2 )   #draw a rectangle in people's face
cv2.namedWindow('family',cv2.WINDOW_NORMAL)
cv2.imshow('family', b)
cv2.waitKey(0)
cv2.destroyAllWindows()
