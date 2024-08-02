from tkinter import *
import mysql.connector as ms
from tkinter import messagebox as mb

con=ms.connect(host="localhost",user="root",password="tanuja",database="Beatbox")
win=Tk()
win.geometry("600x600")

def getinfo(event):
    cur=con.cursor()
    q1="insert into songlist values(%s,%s,%s,%s)"
    cur.execute("select * from songlist")
    data=cur.fetchall()
    for i in data:
        print(i)
        if song.get() in i[3]:
            print(i[3])
            mb.showinfo(title="Beatbox_Admin",message="Already There")
            break
        else:
            cur.execute(q1,(artist_id.get(),mood_id.get(),lyrics.get(),song.get()))
            con.commit()
            break
        

artist_id=Entry(win)
artist_id.pack()

mood_id=Entry(win)
mood_id.pack()

lyrics=Entry(win)
lyrics.pack()

song=Entry(win)
song.pack()

b1=Button(win,text="store")
b1.pack()
b1.bind('<Button>',getinfo)
