from flask import Flask, render_template, Response
app = Flask(__name__)
import cv2
import time

def p(i):
    return "Hello World "+str(i)



@app.route("/")
def hello():
    app.send_static_file('index.html')
if __name__ == '__main__':  
  app.run()        