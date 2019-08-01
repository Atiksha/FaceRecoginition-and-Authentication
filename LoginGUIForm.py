# -*- coding: utf-8 -*-
"""
LoginGUIForm is called by main.py

it will call -----> AddMemberGUIForm.py -----> add_member() Method
or

it will call -----> Recognise.py -----> detect() Method
or

it will call -----> TrainData.py -----> train() Method

Created on Fri Apr 19 11:31:27 2019


@author: Spunky
"""


from tkinter import *
import os
import mysql.connector


from SucessLogin import login_sucess

'''
from AddMemberGUIForm import add_member
from TrainData import train
from Recognise import detect


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
 
    

def login_sucess():
    
    global screen3 
    screen3 = Toplevel(root)
    screen3.geometry("400x450")
    screen3.title("Admin Portal")
    Label(screen3,text =" Welcome ", bg = "grey", height = "2", width = "300",font = ("Calibri", 15)).pack()
    Label(screen3,text ="").pack()
    Label(screen3,text ="").pack()
    Button(screen3,text = "Add new Member", height = "3", width = "30",font = ("Calibri", 11),command = ChangeToAddMemberGUIForm).pack()
    Label(screen3,text ="").pack()
    
    Button(screen3,text = " Search ", height = "3", width = "30",font = ("Calibri", 11), command = ChangeToRecognise).pack()
    Label(screen3,text ="").pack()
    
    Button(screen3,text = " Train ", height = "3", width = "30",font = ("Calibri", 11), command = train).pack()
    Label(screen3,text ="").pack()
    Label(screen3,text ="").pack()
    
    Button(screen3,text = " logout ", height = "1", width = "10",font = ("Calibri", 11), command = delete).pack()
    
'''   

def ChangeToLoginSucess():
    root.destroy()           # Destroy win panel
    login_sucess()  
    
def password_not_recognised():
    global screen4 
    screen4 = Toplevel(root)
    screen4.geometry("150x100")
    screen4.title("Fail")
    
    Label(screen4,text ="password Error").pack()
    Button(screen4,text = " OK ", command = delete).pack()
    
    
    
def user_not_found():
    global screen5 
    screen5 = Toplevel(root)
    screen5.geometry("150x100")
    screen5.title("Fail")
    
    Label(screen5,text ="user not found").pack()
    Button(screen5,text = " OK ", command = delete4).pack()
    
   
    
def login_verify():
    
    
    username = username_verify.get()
    password = password_entery.get()
    print(username)
    print(password)
    
    username_entery.delete(0, END)
    password_entery.delete(0, END)
    print("Login Sucess")
    #login_sucess()
    
 
    mydb = mysql.connector.connect(host="localhost", user="root",passwd="root", database="testdb")
    mycursor = mydb.cursor()
    #mycursor.execute("SELECT * FROM stud WHERE name='Atiksha' and pass='hello'")
    mycursor.execute("SELECT * FROM stud WHERE name= '"+username+"' and pass='"+password+"' ")
 
    #myresult = mycursor.fetchall()
    myresult = mycursor.fetchone()
    
    if(myresult):
        for row in myresult:
            print(row)
        ChangeToLoginSucess()
    else:
         print("Invalid Details")
         password_not_recognised()
       
    
'''
    list_of_files = os.listdir()
    if username in list_of_files:
        file1 = open(username, "r")
        verify = file1.read().splitlines()
        if password in verify:
            #print("Login Sucess")
            login_sucess()
        else:
            #print("Password is not matching")
            password_not_recognised()
    else:
        #print("User not Found")
        user_not_found()
'''
    
    
def login():
    global root
    root = Tk()
    #root.attributes("-alpha", 0.3)
    root.geometry("300x250")
    root.title("Login")
    
    Label(root, text ="Please Enter Details Below to LOGIN").pack()
    Label(root, text ="").pack()
    
    global username_verify
    global password_verify 
    
    username_verify = StringVar()
    password_verify = StringVar()
    
    global username_entery
    global password_entery
    
    Label(root, text ="Username").pack()   
    username_entery = Entry(root, textvariable = username_verify)
    username_entery.pack()
    
   
    Label(root, text ="Password").pack()
    password_entery =  Entry(root, textvariable = password_verify)
    password_entery.pack()
    
    Button(root, text = " Login ", height = "1", width = "10", command = login_verify).pack()
    
    