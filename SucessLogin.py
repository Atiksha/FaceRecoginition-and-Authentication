# -*- coding: utf-8 -*-
"""


LoginGUIForm is called by main.py

it will call -----> AddMemberGUIForm.py -----> add_member() Method
or

it will call -----> Recognise.py -----> detect() Method
or

it will call -----> TrainData.py -----> train() Method


Created on Wed May  1 06:09:31 2019

@author: Spunky
"""


from tkinter import *
import os



from AddMemberGUIForm import add_member
from TrainData import train
#from Recognise import detect

from RecogniseAndroid import detect




def delete():
    screen4.destroy()
    
def ChangeToAddMemberGUIForm():
    root.destroy()           # Destroy win panel
    add_member()
    
def ChangeToTrainData():
    root.destroy()           # Destroy win panel
    train()
    
def ChangeToRecognise():
    root.destroy()           # Destroy win panel
    detect()
 
    
def ChangeToLoginGUIForm():
    root.destroy()           # Destroy win panel
    from LoginGUIForm import login
    login()  


global login_sucess
def login_sucess():
    
    global root
    root = Tk()
    #root.attributes("-alpha", 0.3)
    #root = Toplevel(root)
    root.geometry("400x450")
    root.title("Admin Portal")
    Label(root,text =" Welcome ", bg = "grey", height = "2", width = "300",font = ("Calibri", 15)).pack()
    Label(root,text ="").pack()
    Label(root,text ="").pack()
    Button(root,text = "Add new Member", height = "3", width = "30",font = ("Calibri", 11),command = ChangeToAddMemberGUIForm).pack()
    Label(root,text ="").pack()
    
    Button(root,text = " Search ", height = "3", width = "30",font = ("Calibri", 11), command = ChangeToRecognise).pack()
    Label(root,text ="").pack()
    
    Button(root,text = " Train ", height = "3", width = "30",font = ("Calibri", 11), command = train).pack()
    Label(root,text ="").pack()
    Label(root,text ="").pack()
    
    Button(root,text = " logout ", height = "1", width = "10",font = ("Calibri", 11), command = ChangeToLoginGUIForm).pack()