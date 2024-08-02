from tkinter import *
import mysql.connector as ms
from tkinter import messagebox as mb
from shared import shareddata as sd
import os

con=ms.connect(host="localhost",user="root",password="tanuja",database="beatbox")

artists=[]
def getinfo(event):
    global artists
    nm=event.widget.cget("text")
    artists.append(nm)
    mb.showinfo(title="beatbox",message=nm)

def nxt():
    cur=con.cursor()
    username=sd.shared_username
    q1="insert into fav_artist(Username,Artist_name) values(%s,%s)"
    val=[(username,artist) for artist in artists]
    cur.executemany(q1,val)
    con.commit()
    win.destroy()
    import Beatbox5

win=Tk()
win.title("BeatBox")
win.geometry("1920x1080+0+0")

bg_img=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","logoblur.png"))
canvas=Canvas(win,width=1800,height=1200)
canvas.place(x=0,y=0)
canvas.create_image(600,350,anchor=CENTER,image=bg_img)

select=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fav.png"))
Label(win,image=select,height=1080,width=200).pack(anchor="w")

nm=Label(win,text=sd.shared_username,width=10,height=5).place(x=1100,y=250)
nt=Button(win,text="Next",command=nxt,width=10,height=5).place(x=1100,y=330)

#1
x=StringVar()
arijit=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","f1arijit.png"))
b1=Button(win,image=arijit,height=200,width=200,text="Arijit Singh")
b1.bind('<Button>',getinfo)
b1.place(x=210,y=20)

shankar=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fshankar.png"))
b2=Button(win,image=shankar,height=200,width=200,text="Shankar Mahadevan")
b2.bind('<Button>',getinfo)
b2.place(x=210,y=230)

lata=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","f1lata.png"))
b3=Button(win,image=lata,height=200,width=200,text="Lata Mangeshkar")
b3.bind('<Button>',getinfo)
b3.place(x=210,y=440)


#2
shreya=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fshreya.png"))
b4=Button(win,image=shreya,height=200,width=200,text="Shreya Ghoshal")
b4.bind('<Button>',getinfo)
b4.place(x=420,y=20)

badshah=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fbadshah.png"))
b5=Button(win,image=badshah,height=200,width=200,text="Badshah")
b5.bind('<Button>',getinfo)
b5.place(x=420,y=230)

neha=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fneha.png"))
b6=Button(win,image=neha,height=200,width=200,text="Neha Kakkar")
b6.bind('<Button>',getinfo)
b6.place(x=420,y=440)

#3
armaan=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","farmaan.png"))
b7=Button(win,image=armaan,height=200,width=200,text="Armaan Malik")
b7.bind('<Button>',getinfo)
b7.place(x=650,y=20)

sonu=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fsonu.png"))
b8=Button(win,image=sonu,height=200,width=200,text="Sonu Nigam")
b8.bind('<Button>',getinfo)
b8.place(x=650,y=230)

kk=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fkk.png"))
b9=Button(win,image=kk,height=200,width=200,text="KK")
b9.bind('<Button>',getinfo)
b9.place(x=650,y=440)

#4
sana=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fsana.png"))
b10=Button(win,image=sana,height=200,width=200,text="Shehnaaz Gill")
b10.bind('<Button>',getinfo)
b10.place(x=860,y=20)

yoyo=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fyoyo.png"))
b11=Button(win,image=yoyo,height=200,width=200,text="Yo Yo Honey Singh")
b11.bind('<Button>',getinfo)
b11.place(x=860,y=230)

jubin=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fjubin.png"))
b12=Button(win,image=jubin,height=200,width=200,text="Jubin Nautiyal")
b12.bind('<Button>',getinfo)
b12.place(x=860,y=440)


