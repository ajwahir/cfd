import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('/home/ajwahir/imagine_cup/cfd/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

vidcap = cv2.VideoCapture(0)
# vidcap = cv2.VideoCapture('/home/ajwahir/acads/pd3/face2.mp4')
vidcap.set(4,1280)
vidcap.set(5,720)
# vidcap.set(4,520)
# vidcap.set(5,718)
success,img = vidcap.read()

while success:
	success,img = vidcap.read()

	# img = cv2.imread('ammma.jpg')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
	    # cv2.Rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	    roi_gray = gray[y:y+h, x:x+w]
	    roi_color = img[y:y+h, x:x+w]
	    eyes = eye_cascade.detectMultiScale(roi_gray)
	    # print eyes
	    for(ex,ey,ew,eh) in eyes:
	        # cv2.Rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	        print 'eyes here'
	# cv2.imshow('img',img)
	

