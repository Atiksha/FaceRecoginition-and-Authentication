

from tkinter import *

from PIL import Image, ImageTk

import os
import mysql.connector
#from tkcalendar import Calendar, DateEntry

#from tkinter import messagebox


from tkinter import scrolledtext



def ChangeToLoginSucess():
    root.destroy()           # Destroy win panel
    from SucessLogin import login_sucess
    login_sucess() 





def search(idNo): 
    
    
    global root 
    root = Tk()
    
    #root = Toplevel(screen)
    root.state('zoomed')
    root.geometry('{}x{}'.format(1920,1080))
    root.title("Admin Portal")
    #root.attributes("-alpha", 0.3)
    
    top_frame = Frame(root, bg='black', width=450, height=100, pady=3)
    center = Frame(root, bg='navy', width=50, height=40, padx=0, pady=3)
    btm_frame = Frame(root, bg='gray60', width=450, height=45, pady=3)
    
    # layout all of the main containers
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    #position of frames
    top_frame.grid(row=0, sticky="ew")
    center.grid(row=1, sticky="nsew")
    btm_frame.grid(row=2, sticky="ew")
    
    def showImg():
        load = Image.open("q10.jpg")
        
        #load = Image.open("giphy.gif")
        #opacity of image
        load.putalpha(250)
        render = ImageTk.PhotoImage(load)
    
        # labels can be text or images
        img = Label(center,image=render)
        img.image = render
        img.place(x=0, y=0)
        
    #showImg()
    
  
    model_label = Label(top_frame, text='Identification Process ',height = "1", width = "20",font = ("Calibri", 30), padx=3, pady=20).pack()
    #model_label.grid(row=1, columnspan=3)
    
    
    # create the center widgets
    center.grid_rowconfigure(0, weight=1)
    center.grid_columnconfigure(1, weight=1)
    
    
    
    ctr_mid1 = Frame(center, bg='Yellow', width=250, height=190, padx=3, pady=3)
    
    
    
    Label(center, text="Details", height = "1", width = "20",font = ("Calibri", 30)).pack(pady=(30, 30))
   
    global st
    st = scrolledtext.ScrolledText(center,font = ("Calibri",25),height = "12", width = "65")
    st.pack()
   
    # layout the widgets Bottom frame
    btn_Next = Button(btm_frame,text = "Back",  height = "2", width = "30",bg="gray50",command=ChangeToLoginSucess).pack()
 
    
    mydb = mysql.connector.connect(host="localhost", user="root",passwd="root", database="testdb")
    mycursor = mydb.cursor()
       
    
    #sql = "SELECT * FROM studentData WHERE fName = %s"
    #mycursor.execute(sql, ("xyz", ))
    
    sql = "SELECT * FROM studentData WHERE regNO = %s"
    mycursor.execute(sql, (idNo, ))
    print(idNo)
    
    myresult = mycursor.fetchall()
    
    
    #mycursor.execute("SELECT * FROM studentData WHERE regNO="idNo)
    #myresult = mycursor.fetchall()
    
    color = ['ID NO', 'FIRST NAME', 'LAST NAME','DOB', 'GENDER', 'EMAIL ID','PHONE NO', 'COURSE','BATCH', 'BLOOD GROUP','ADDRESS', 'FATHER NAME', 'MOTHER NAME','ANY OTHER INFO'] 
    for row in myresult:
        for (colname,col) in zip(color, row): 
            cols= "    "+colname+ "\t\t-\t" +str(col)
            st.insert (INSERT, cols )
            print(colname,col)
            st.insert(END,"\n")
            
    
    
    root.mainloop()
#search(28)