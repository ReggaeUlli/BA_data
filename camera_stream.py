import cv2
import socket
import time
import requests
import io
import base64
#connect webcam
cap = cv2.VideoCapture(-1)

#connect TCP
host = socket.gethostname()
port = 2000                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while(True):
        ret, frame = cap.read()
        success, jpg = cv2.imencode(".jpg", frame)
        im_bytes = jpg.tobytes()
        im_b64 = base64.b64encode(im_bytes)
        s.send(im_b64)
        s.send(";;;")
        time.sleep(5)
s.close()
print('Received', repr(data))
