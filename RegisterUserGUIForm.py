from tkinter import *
import os
import mysql.connector




def register_user():
    username_info = username.get()
    password_info = password.get()
    
    #file=open(username_info+".txt", "w")
    file=open(username_info, "w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    username_entery.delete(0, END)
    password_entery.delete(0, END)
    
    Label(screen1, text ="Registration Successful", fg = "green", font = ("Calibri", 13)).pack()

def register(scr):
    global screen
    screen = scr
    global screen1 
    screen1 = Toplevel(screen)
    screen1.geometry("300x250")
    screen1.title("Register")
    
    
    global username 
    global password
    global username_entery
    global password_entery
    
    username = StringVar()
    password = StringVar()
    
    Label(screen1, text ="Please Enter Details Below").pack()
    Label(screen1, text ="").pack()
    
    Label(screen1, text ="Username").pack()
    username_entery = Entry(screen1, textvariable = username)
    username_entery.pack()
    Label(screen1, text ="Password").pack()
    password_entery =  Entry(screen1, textvariable = password)
    password_entery.pack()
    Button(screen1, text = " Register ", height = "1", width = "10", command = register_user).pack()

    