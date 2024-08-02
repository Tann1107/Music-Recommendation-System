from tkinter import *
import os

win=Tk()
win.geometry("1800x1200")
win.title("Welcome")
win.iconbitmap(os.path.join(os.path.dirname(__file__), "images", "Beaticon.ico"))

bg_img=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","logoblur.png"))
canvas=Canvas(win,width=1800,height=1200)
canvas.place(x=0,y=0)
canvas.create_image(600,350,anchor=CENTER,image=bg_img)

def reg():
    win.destroy()
    import Beatbox3

def log():
    win.destroy()
    import Beatbox5

register=Button(win,text="Register",width=10,font=("Century",14,"bold"),bg="white",fg="black",command=reg).place(x=550,y=300)
login=Button(win,text="Login",width=10,font=("Century",14,"bold"),bg="white",fg="black",command=log).place(x=550,y=350)
