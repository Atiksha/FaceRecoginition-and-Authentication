# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 12:52:37 2019

@author: Spunky
"""

import cv2


address = "http://192.168.43.1:8080/video" # Your address might be different


cam = cv2.VideoCapture(0)
cam.open(address)
#cam.set(3, 640) # set video width
#cam.set(4, 480)

#make sure 'haarcascade_frontalface_default.xml' is in the same folder as this code
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id (must enter number start from 1, this is the lable of person 1)
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0


if (cam.isOpened()== False): 
    print("Error opening video stream or file")

else:
    print("sucess")
    # Read and display video frames until video is completed or 
    # user quits by pressing ESC
    #cv2.startWindowThread()
    while(cam.isOpened()):
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)
    
        for (x,y,w,h) in faces:
    
            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1
    
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
    
            cv2.imshow('image', img)
    
        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 30 face sample and stop video
             break
   
    cam.release()
    cv2.destroyAllWindows()
