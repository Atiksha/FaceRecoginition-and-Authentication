# -*- coding: utf-8 -*-
"""

AddMemberGUIForm is called by LoginGUIForm.py

it will call -----> FaceAndroid.py -----> faceGUI() Method
or
it will call -----> Face.py -----> faceGUI() Method

Created on Fri Apr 19 10:18:32 2019

@author: Spunky
"""


from tkinter import *

from PIL import Image, ImageTk

import os
import mysql.connector
from tkcalendar import Calendar, DateEntry

from tkinter import messagebox


from tkinter import scrolledtext


'''
#for webcam(laptop Camera)
from face import faceGU
'''

from FaceAndroid import faceGUI
#from face import faceGUI


def ChangeToLoginSucess():
    root.destroy()           # Destroy win panel
    from SucessLogin import login_sucess
    login_sucess()  

def ChangeToFaceAndroid():
    root.destroy()           # Destroy win panel
    faceGUI(msg)

def getResistrationNumber():
    ''' 
    TO ACCESS THE REGESTRATION NUMBER OF CURRENT STUDENT ,
    WHICH WILL BE THE ID NUMBER FOR THE DATASET OF SAME PERSON IN NEXT PHASE
    
    '''
    
    mydb = mysql.connector.connect(host="localhost", user="root",passwd="root", database="testdb")
    mycursor = mydb.cursor()
       
    mycursor.execute("SELECT MAX(regNO) FROM studentData")
    myresult = mycursor.fetchone()
    global msg
    for row in myresult:
        msg=row
    #messagebox.showinfo('Message title',msg)
    print(msg)
    ChangeToFaceAndroid()
    #faceGUI(msg,root)
    
 
def submit_data():
        
    FName = e0.get()
    LName = e1.get()
    DOB = e2.get()
    Gender = e3
    Email = e4.get()
    Phone = e5.get()
    Course = e6.get()
    Batch = e7.get()
    BGroup = e8.get()
    Address = e9.get(1.0,END)
    FtName = e10.get()        
    MtName = e11.get()
    OInfo = e12.get(1.0,END)
    
    mydb = mysql.connector.connect(host="localhost", user="root",passwd="root", database="testdb")
    mycursor = mydb.cursor()
            
    sqlFormula = "insert into studentData(fName, lName, dob, gender , email , pNo , course , batch , bGroup , addess , ftName, mtName , oInfo) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    #student = [('xyz','Pundir', '13-11-1998', 'F','atikshapundir1311@gmali.com', '9874563210' ,'Btech (CSE)', '2016-2020', 'A','dehradoon', 'S.S.P', 'S.P', '6sem')]
    student = [(FName,LName,DOB,Gender,Email,Phone,Course,Batch,BGroup,Address,FtName,MtName,OInfo)]
    mycursor.executemany(sqlFormula, student)
    
    mydb.commit() 
    
    
    '''
    print(FName)
    print(LName)
    print(DOB)
    print(Gender)
    print(Email)
    print(Phone)
    print(Course)
    print(Batch)
    print(BGroup)
    print(Address)
    print(FtName)
    print(MtName)
    print(OInfo)
    '''
    
    getResistrationNumber()
    
   






def add_member(): 
    global root
    root = Tk()
    root.state('zoomed')
    root.resizable(False,False)
    #app=FullrootApp(root)
    #root.geometry("1200x750")
    root.geometry('{}x{}'.format(1920,1080))
    root.title("Admin Portal")
    #root.attributes("-alpha", 0.3)
    
    top_frame = Frame(root, bg='black', width=450, height=100, pady=3)
    center = Frame(root, bg='navy', width=50, height=40, padx=3, pady=3)
    btm_frame = Frame(root, bg='gray60', width=450, height=45, pady=3)
    #btm_frame2 = Frame(root, bg='pink', width=450, height=60, pady=3)
    
    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    #position of frames
    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=2, sticky="ew")
    #btm_frame2.grid(row=4, sticky="ew")
    
    
    # create the widgets for the top frame
    #Label(top_frame, text='',height = "1", width = "20",font = ("Calibri", 30)).grid(row=0, columnspan=3)
   
    model_label = Label(top_frame, text='Registration Process 1',height = "1", width = "20",font = ("Calibri", 30), padx=3, pady=20).pack()
    #model_label.grid(row=1, columnspan=3)
    
    
    # create the center widgets
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)
    
    
    
    ctr_left = Frame(center, bg='midnight blue', width=250, height=190)
    ctr_mid1 = Frame(center, bg='Yellow', width=250, height=190, padx=3, pady=3)
    ctr_right = Frame(center, bg='#808080', width=250, height=190, padx=3, pady=3)
    
    def showImg():
        load = Image.open("q10.jpg")
        
        #load = Image.open("giphy.gif")
        #opacity of image
        load.putalpha(150)
        render = ImageTk.PhotoImage(load)
    
        # labels can be text or images
        img = Label(ctr_mid1,image=render)
        img.image = render
        img.place(x=0, y=0)
        
    showImg()
    '''
    
    ctr_left = Frame(center,  width=250, height=190)
    ctr_mid1 = Frame(center, width=250, height=190, padx=3, pady=3)
    ctr_right = Frame(center,  width=250, height=190, padx=3, pady=3)
    '''
    
    #ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid1.grid(row=0, column=1, sticky="nsew")
    #ctr_right.grid(row=0, column=2, sticky="ns")
    
    
    
    # create the center YELLOW widgets
    
    
        
        
        
    def myfunction(event):
        #canvas.configure(scrollregion=canvas.bbox("all"),width=1000,height=580)
        canvas.configure(scrollregion=canvas.bbox("all"),width=900,height=1000)
    
   
    
    canvas=Canvas(ctr_mid1)
    ctr_mid=Frame(canvas)
    myscrollbar=Scrollbar(ctr_mid1,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)
    
    
    
    myscrollbar.pack(side="right",fill="y")
    canvas.pack()
    canvas.create_window((0,0),window=ctr_mid,anchor='nw')
    ctr_mid.bind("<Configure>",myfunction)
    
    global e0
    Label(ctr_mid, text="First Name", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(50, 10),row=0, sticky=W)
    e0 = Entry(ctr_mid, width = "40",font = ("Calibri", 15))
    e0.grid(padx=(20, 10),pady=(50, 10),row=0, column=1)
   
    
    global e1
    Label(ctr_mid, text="Last Name", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=1, sticky=W)
    e1 = Entry(ctr_mid, width = "40",font = ("Calibri", 15))
    e1.grid(padx=(20, 10),row=1, column=1)
    
    
    
    #Calander will Open to Select a Date
    def example1():
        def print_sel():
            #print(cal.selection_get())
            DOB=cal.selection_get()
            e2.config(state=NORMAL)
            e2.delete(0, END)
            e2.insert ( 0, DOB )
            e2.config(state=DISABLED)
        #top = tk.Toplevel(root)
        top = Toplevel(root)
        cal = Calendar(top, font="Arial 14", selectmode='day', cursor="hand1", year=2018, month=2, day=5)
        cal.pack(fill="both", expand=True)
        ttk.Button(top, text="ok", command=print_sel).pack()
    
    global e2
    Label(ctr_mid, text="Date Of Birth", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=2, sticky=W)
    e2 = Entry(ctr_mid, width = "40",font = ("Calibri", 15))
    e2.grid(padx=(20, 10),row=2, column=1)
    e2.insert(0, 'Choose Date From Calander')
    e2.config(state=DISABLED)
    bt1=Button(ctr_mid, text='Calendar', command=example1)
    bt1.grid(padx=(20, 10),row=2, column=2)
    
    
    
    
    def sel():
       global e3
       selection = "You selected the option " + str(var.get())
       e3 = str(var.get())
       print(e3)
         
    Label(ctr_mid, text="Gender", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=3, sticky=W)
    #var = IntVar()
    var = StringVar()
    var.set("Female")
    R1 = Radiobutton(ctr_mid, text=" Male ", variable=var, value="M",font = ("Calibri", 15),command=sel)
    R1.grid(padx=(20, 10),pady=(10, 10),row=3, column=1,sticky=W)
    
    R2 = Radiobutton(ctr_mid, text=" Female", variable=var, value="F",font = ("Calibri", 15), command=sel)
    R2.grid(padx=(20, 10),pady=(10, 10),row=3, column=1,sticky=E)
    
    
    global e4
    Label(ctr_mid, text="E-mail", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=4, sticky=W)
    e4 = Entry(ctr_mid, width = "40",font = ("Calibri", 15))
    e4.grid(padx=(20, 10),row=4, column=1)
    
    
    global e5
    Label(ctr_mid, text="Phone No.", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=5, sticky=W)
    e5 = Entry(ctr_mid, width = "40",font = ("Calibri", 15))
    e5.grid(padx=(20, 10),row=5, column=1)
    
    
    global e6
    Label(ctr_mid, text=" Course ", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=6, sticky=W)
    e6 = Entry(ctr_mid, width = "40",font = ("Calibri", 15))
    e6.grid(padx=(20, 10),row=6, column=1)
    e6.insert(0, 'Choose course from the droplist')
    e6.config(state=DISABLED)
    # Create a Tkinter variable
    tkvar = StringVar(ctr_mid)
     
    # Dictionary with options
    choices = { 'Btech CS','Btech IT','Btech MC','Btech EC','MCA','BCA','BSC'}
    tkvar.set('Btech CS') # set the default option
     
    popupMenu = OptionMenu(ctr_mid, tkvar, *choices)
    popupMenu.grid(padx=(20, 10),row = 6, column =2)
     
    # on change dropdown value
    def change_dropdown(*args):
        #print( tkvar.get() )
        Cou=tkvar.get()
        e6.config(state=NORMAL)
        e6.delete(0, END)
        e6.insert ( 0, Cou )
        e6.config(state=DISABLED)
     
    # link function to change dropdown
    tkvar.trace('w', change_dropdown)
    
    
    global start,end,e7
    Label(ctr_mid, text=" Batch ", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=7, sticky=W)
    e7 = Entry(ctr_mid, width = "25",font = ("Calibri", 15))
    e7.grid(padx=(20, 10),row=7, column=1,sticky=W)
    e7.insert(0, 'Choose Batch Duration')
    e7.config(state=DISABLED)
    var2 = IntVar(ctr_mid)
    def ok():
        start1=start.get()
        end1=end.get()
        e7.config(state=NORMAL)
        e7.delete(0, END)
        e7.insert ( 0, start1 )
        e7.insert ( 4, "-" )
        
        e7.insert ( 5, end1 )
        e7.config(state=DISABLED)
        
    start = Spinbox(ctr_mid,from_=2018, to=2030 ,command=ok)
    start.grid(padx=(20, 10),row=7, column=1,sticky=E)
    
    end = Spinbox(ctr_mid,from_=2020, to=2030 ,command=ok)
    end.grid(padx=(20, 10),row=7, column=2,sticky=E)
    
    
    global e8
    Label(ctr_mid, text="Blood Group", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=8, sticky=W)
    e8 = Entry(ctr_mid, width = "40",font = ("Calibri", 15))
    e8.grid(padx=(20, 10),row=8, column=1)
    
    
    global e9
    Label(ctr_mid, text="Address", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=9, sticky=W)
    e9 = scrolledtext.ScrolledText(ctr_mid,height=3,width = "38",font = ("Calibri", 15))
    e9.grid(padx=(20, 10),row=9, column=1)
   
    
    global e10
    Label(ctr_mid, text="Father's Name", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=10, sticky=W)
    e10 = Entry(ctr_mid, width = "40",font = ("Calibri", 15))
    e10.grid(padx=(20, 10),row=10, column=1)
    
   
    global e11
    Label(ctr_mid, text="Mother's Name", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(10, 10),row=11, sticky=W)
    e11 = Entry(ctr_mid, width = "40",font = ("Calibri", 15))
    e11.grid(padx=(20, 10),row=11, column=1)
    
    
    global e12
    Label(ctr_mid, text="Any Other Info", height = "1", width = "20",font = ("Calibri", 15)).grid(padx=(30, 30),pady=(12, 10),row=12, sticky=W)
    e12 = scrolledtext.ScrolledText(ctr_mid,height=3,width = "38",font = ("Calibri", 15))
    e12.grid(padx=(20, 10),pady=(0, 50),row=12, column=1)

    
    
    
    # layout the widgets 2nd Bottom frame
    #Label(btm_frame, text="").grid(row=0, column=1, sticky=W)
    
    #btn_back = Button(btm_frame,text = "Back",  height = "2", width = "30",bg="gray50",  command = submit_data).pack()
    btn_Next = Button(btm_frame,text = "Next",  height = "2", width = "30",bg="gray50",  command = submit_data)
    btn_Back = Button(btm_frame,text = "Back",  height = "2", width = "30",bg="gray50",  command = ChangeToLoginSucess)
    btn_Back.grid(padx=(400, 100),row=0, column=0, sticky=E)
    btn_Next.grid(padx=(100, 100),row=0, column=5, sticky=W)

    #root.mainloop()
  
#add_member()