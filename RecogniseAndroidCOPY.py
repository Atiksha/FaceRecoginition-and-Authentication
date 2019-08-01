# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:51:55 2019

@author: Spunky
"""

'''

RecogniseAndroid is called by LoginGUIForm.py

it will call -----> SearchResult.py -----> search() Method

'''
from tkinter import *
from SearchResult import search
import cv2
import numpy as np
import os 

import mysql.connector

def detect():
    
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')   #load trained model
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    '''
    #iniciate id counter, the number of persons you want to include
    id = 6 #two persons (e.g. Jacob, Jack)
    
    
    names = ['','Atiksha','Surbhi','Shivu','Ayushi','Aditya','Sashi']  #key in names, start from the second place, leave first empty
    '''
    # Initialize and start realtime video capture
    address = "http://192.168.43.1:8080/video" # Your address might be different
    
    
    id=0
    mydb = mysql.connector.connect(host="localhost", user="root",passwd="root", database="testdb")
    mycursor = mydb.cursor()
       
    #mycursor.execute("SELECT fName FROM studentData")
    mycursor.execute("SELECT regNO FROM studentData")
    myresult = mycursor.fetchall()
        
    names = ['']    #leave first place empty
    for nam in myresult:
        names.extend(nam)
        id=id+1 
        
    for nam in names:
        print(nam)
    
    print(id)

    cam = cv2.VideoCapture(0)
    cam.open(address)

    #cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video widht
    cam.set(4, 480) # set video height
    
    # Define min window size to be recognized as a face
    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)
    
    if (cam.isOpened()== False): 
        print("Error opening video stream or file")
        
    else:
        print("sucess")
        # Read and display video frames until video is completed or 
        # user quits by pressing ESC
        #cv2.startWindowThread()
        while(cam.isOpened()):
    
        
            ret, img =cam.read()
        
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        
            faces = faceCascade.detectMultiScale( 
                gray,
                scaleFactor = 1.2,
                minNeighbors = 5,
                minSize = (int(minW), int(minH)),
               )
            flag=0
            for(x,y,w,h) in faces:
        
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        
                id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
    
                # Check if confidence is less them 100 ==> "0" is perfect match 
                if (confidence > 40):
                    
                    print("original   "+ str(confidence))
                    print(id)
                    #idd = names[id]
                    idd=id
                    #confidence = "  {0}%".format(round(100 - confidence))
                    print(idd)
                    flag=1
                    
                    '''
                    print("original   "+ str(confidence))
                    idd = names[id]
                    #confidence = "  {0}%".format(round(100 - confidence))
                    print(idd)
                    flag=1
                    '''
                else:
                    idd = "unknown"
                    confidence = "  {0}%".format(round(100 - confidence))
                    print("unknown")
                
                cv2.putText(img, str(idd), (x+5,y-5), font, 1, (255,255,255), 2)
                cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
                
                print(str(idd),str(confidence))
                
            if flag == 1: 
                
                print("Sucesssssssssssss")
                print("\n [INFO] Exiting Program and cleanup stuff")
                cam.release()
                cv2.destroyAllWindows()
                search(idd)
            
                '''
                print("Sucesssssssssssss")
                search()
                break
                '''
            cv2.imshow('camera',img)
            
            k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
            
    
    # Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    cam.release()
    cv2.destroyAllWindows()
    
detect()
'''
def main_screen():
    global screen
    screen = Tk()
    #screen.attributes("-alpha", 0.3)
    screen.geometry("300x250")
    screen.title("NOTES")
    Label(text ="Notes 1.0", bg = "grey", height = "2", width = "300",font = ("Calibri", 13)).pack()
    Label(text ="").pack()
    
    Button(text = "Register",  height = "2", width = "30",command=detect).pack()
    #screen.state('zoomed')
    screen.mainloop()
    
main_screen() 
'''