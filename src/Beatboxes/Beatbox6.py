from tkinter import *
import mysql.connector as ms
from shared import shareddata as sd
import os
con=ms.connect(host="localhost",user="root",password="tanuja",database="beatbox")

def songs():
    cur=con.cursor()
    q1=f"select artist_name from fav_artist where username=%s"
    cur.execute(q1,(sd.shared_username,))
    data=cur.fetchall()
    for i in data:
        listbox.insert(1,i[0])
    listbox.place(x=50,y=70)

    
songnames=list()
def nxt():
    global songnames
    cur=con.cursor()
    if(listbox.curselection()):
        index=listbox.curselection()
    artist=[listbox.get(i) for i in index[::]]
    q1="select songfile from songlist where artistid=%s and moodis=%s"
    for i in artist:
        for j in mood:
            val=(i,j)
            cur.execute("select artistid from artid where artistname=%s",(i,))
            artistid=cur.fetchall()[0][0]
            cur.execute("select id from mood_id where mood_name=%s",(j,))
            moodid=cur.fetchall()[0][0]
            cur.execute(q1,(artistid,moodid))
            song=cur.fetchall()
            songnames.extend([i[0] for i in song])
    con.commit()
    win.destroy()
    import Beatbox7

def getsonglist():
    return songnames

mood=[]
def getmood(event):
    global moods
    if(event.widget.cget("text") not in mood): 
        mood.append(event.widget.cget("text"))

    
win=Tk()
win.title("BeatBox")
win.geometry("1920x1080+0+0")

bg_img=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","logoblur.png"))
canvas=Canvas(win,width=1800,height=1200)
canvas.place(x=0,y=0)
canvas.create_image(600,350,anchor=CENTER,image=bg_img)

wel=Label(win,text="Welcome",font=("Brush Script MT",22),bg="pink",padx=10).place(x=500,y=20)
wel=Label(win,text=sd.shared_username,font=("Brush Script MT",22),bg="pink",padx=10).place(x=600,y=20)

b1=Button(win,text="My Artists",font=("Century",14,"bold"),bg="white",fg="black",command=songs).place(x=50,y=30)
listbox=Listbox(win,selectmode="multiple")

nxt=Button(win,text="Next",font=("Century",14,"bold"),bg="white",fg="black",command=nxt).place(x=1000,y=330)

happy=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fhappy.png"))
bhappy=Button(win,image=happy,text="happy")
bhappy.place(x=250,y=100)
bhappy.bind('<Button>',getmood)

sad=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fsad.png"))
bsad=Button(win,image=sad,text="sad")
bsad.place(x=500,y=100)
bsad.bind('<Button>',getmood)

love=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","flove.png"))
blove=Button(win,image=love,text="love")
blove.place(x=750,y=100)
blove.bind('<Button>',getmood)

angry=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fangry.png"))
bangry=Button(win,image=angry,text="angry")
bangry.place(x=250,y=400)
bangry.bind('<Button>',getmood)

party=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fparty.png"))
bparty=Button(win,image=party,text="party")
bparty.place(x=500,y=400)
bparty.bind('<Button>',getmood)

religious=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","freligious.png"))
breligious=Button(win,image=religious,text="religious")
breligious.place(x=750,y=400)
breligious.bind('<Button>',getmood)
