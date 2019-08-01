# -*- coding: utf-8 -*-
"""
FaceAndroid is called by AddMemberGUIForm.py

it will call -----> .py -----> () Method
Created on Mon Apr 22 23:02:58 2019

@author: Spunky
"""

#from LoginGUIForm import login
#from RegisterUserGUIForm import register
#from LoginGUIForm import login
from tkinter import *

import cv2
import os


def ChangeToLoginSucess():
    root.destroy()           # Destroy win panel
    from SucessLogin import login_sucess
    login_sucess() 
    
    
def capture_face(idn):   
    print("start")   
    '''
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480) 
    '''
    address = "http://192.168.43.1:8080/video" # Your address might be different

    
    cam = cv2.VideoCapture(0)
    cam.open(address)
    #cam.set(3, 640) # set video width
    #cam.set(4, 480)
    
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    face_id = idn
    #face_id = input('\n enter user id end press <return> ==>  ')
    
    

    if (cam.isOpened()== False): 
        print("Error opening video stream or file")
        
    else:
        print("sucess")
        # Read and display video frames until video is completed or 
        # user quits by pressing ESC
        #cv2.startWindowThread()
        print("\n [INFO] Initializing face capture. Look the camera and wait ...")
            
        count = 0
            
        while(cam.isOpened()):
            
            
           
            
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, 1.3, 5)
        
            for (x,y,w,h) in faces:
        
                cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
                count += 1
        
               
                cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        
                cv2.imshow('image', img)
        
            k = cv2.waitKey(100) & 0xff # Press 'ESC' 
            if k == 27:
                break
            elif count >= 30: 
                 break
            
        print("\n [INFO] Exiting Program and cleanup stuff")
        
    
    cam.release()
    cv2.destroyAllWindows()
    msg="Member Added Sucessfully"
    messagebox.showinfo('Message title',msg)
    ChangeToLoginSucess()
    #login_sucess()
   
    
def faceGUI(idP):
    global id
    id = idP
    print("face session Started")
    
    global root
    root = Tk()
    root.geometry("300x250")
    root.title("Face Dataset Creation")
    
    Label(root, text ="Please Enter To Start Dataset Creation").pack()
    Label(root, text ="").pack()
    
   
    Label(root, text ="LOOK AT THE CAMERA").pack()
    btn= Button(root, text = " Start ", height = "1", width = "10", command=lambda: capture_face(id))
    btn.pack()  
    #root.mainloop()
#faceGUI(80)