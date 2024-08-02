from tkinter import *
import mysql.connector as ms
from tkinter import messagebox as mb
from shared import shareddata
import os
con=ms.connect(host="localhost",user="root",password="tanuja",database="beatbox")

def log(event):
    unm=uname.get()
    ps=password.get()
    cur=con.cursor()
    q1="select Username,Password from info where username=%s"
    cur.execute(q1,(unm,))
    data=cur.fetchone()
    if data == None:
        mb.showerror(title="BeatBox",message="No User Found")
    elif data[0] == unm and data[1] == ps:
        shareddata.shared_username=uname.get()
        mb.showinfo(title="BeatBox",message="Login Succesfull")
        win.destroy()
        import Beatbox6
    elif data[1] != unm:
        mb.showerror(title="BeatBox",message="No User Found")
    elif data[0] == unm and data[1] != ps:
        mb.showwarning(title="BeatBox",message="Wrong Password")
    else:
        pass
    s1.set("")
    s2.set("")

                
    
win=Tk()
win.title("BeatBox")
win.geometry("1920x1080+0+0")

bg_img=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","logoblur.png"))
canvas=Canvas(win,width=1800,height=1200)
canvas.place(x=0,y=0)
canvas.create_image(600,350,anchor=CENTER,image=bg_img)

lbname=Label(win,text="Username",font=("Century",11),bg="white").place(x=450,y=300)
s1=StringVar()
uname=Entry(win,textvariable=s1)
uname.place(x=580,y=300)

lbpass=Label(win,text="Password",font=("Century",11),bg="white").place(x=450,y=350)
s2=StringVar()
password=Entry(win,textvariable=s2)
password.place(x=580,y=350)

Login=Button(win,text="Login",font=("Century",12),bg="black",fg="white")
Login.place(x=540,y=400)
Login.bind('<Button>',log)
