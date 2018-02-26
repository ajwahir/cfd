from flask import Flask
app = Flask(__name__)
import cv2



@app.route("/")
def hello():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False
    i=0
    while rval:
        i=i+1
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break
        if i%50==0:
            cv2.imwrite("image.jpg", frame)
    cv2.destroyWindow("preview")
    return "Hello World!"s