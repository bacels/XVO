import urllib.request
import cv2
import numpy as np


video_ip_on = True
url='http://192.168.0.11:8080/shot.jpg'

cv2.namedWindow('Sz_Laboratorio_XVO', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Sz_Laboratorio_XVO', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while video_ip_on:
        try:            
            imgResp=urllib.request.urlopen(url)
            imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
            img=cv2.imdecode(imgNp,-1)
            cv2.imshow('Sz_Laboratorio_XVO',img)
            if ord('x')==cv2.waitKey(1):
                video_ip_on = False
        except:
            video_ip_on = False
            
cv2.destroyAllWindows()