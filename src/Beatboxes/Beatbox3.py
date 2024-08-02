from tkinter import *
import mysql.connector as ms
from tkinter import messagebox as mb
from shared import shareddata as sd
import os

con=ms.connect(host="localhost",user="root",password="tanuja",database="beatbox")
def valid(event):
    nm=name.get()
    em=email.get()
    pn=phoneno.get()
    ps=password.get()
    cur=con.cursor()
    q1="select * from info where username=%s"
    cur.execute(q1,(nm,))
    data=cur.fetchone()
    if data == None:        
        if "@gmail.com" in em:
            if pn.isdigit() and len(pn)==10:
                q2="insert into info values(%s,%s,%s,%s)"
                cur.execute(q2,(nm,em,pn,ps))
                sd.shared_username=nm
                mb.showinfo(title="Beatbox",message="Register Successfull")
                con.commit()
                s1.set("")
                s2.set("")
                s3.set("")
                s4.set("")
                win.destroy()
                import Beatbox4
            else:
                mb.showerror(title="Error",message="Enter Valid Phone Number")
        else:
                mb.showerror(title="Error",message="Enter Valid Email Id")
    else:
        mb.showerror(title="Error",message="Username is Taken")
    



win=Tk()
win.title("Beatbox")
win.geometry("1800x1200+0+0")

bg_img=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","logoblur.png"))
canvas=Canvas(win,width=1800,height=1200)
canvas.place(x=0,y=0)
canvas.create_image(600,350,anchor=CENTER,image=bg_img)

lbname=Label(win,text="Username",font=("Century",11),bg="white").place(x=450,y=250)
s1=StringVar()
name=Entry(win,textvariable=s1)
name.place(x=580,y=250)

lbemail=Label(win,text="Email",font=("Century",11),bg="white").place(x=450,y=280)
s2=StringVar()
email=Entry(win,textvariable=s2)
email.place(x=580,y=280)

lbphone=Label(win,text="Phone no",font=("Century",11),bg="white").place(x=450,y=310)
s3=StringVar()
phoneno=Entry(win,textvariable=s3)
phoneno.place(x=580,y=310)


lbpass=Label(win,text="Password",font=("Century",11),bg="white").place(x=450,y=340)
s4=StringVar()
password=Entry(win,textvariable=s4)
password.place(x=580,y=340)

reg=Button(win,text="Register",font=("Century",12,"bold"),bg="black",fg="white")
reg.place(x=540,y=400)
reg.bind('<Button>',valid)
