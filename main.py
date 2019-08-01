# -*- coding: utf-8 -*-
"""
Main file of the Project
it will call -----> LoginGUIForm.py -----> login() Method

Created on Wed Apr 24 14:25:36 2019

@author: Spunky
"""



from tkinter import *
import os
import mysql.connector


from LoginGUIForm import login
#from RegisterUserGUIForm import register

from PIL import Image, ImageTk

def ChangeToLoginGUIForm():
    root.destroy()           # Destroy win panel
    login()  


def main_root():
    global root
    root = Tk()
    #root.attributes("-alpha", 0.3)
    root.geometry("300x250")
    root.title("Recogination and Information Retrival")
    Label(text ="WELCOME", bg = "grey", height = "2", width = "300",font = ("Calibri", 13)).pack()
    Label(text ="").pack()
    Button(text = "Login", height = "2", width = "30",command = ChangeToLoginGUIForm).pack()
    root.mainloop()
    
main_root()