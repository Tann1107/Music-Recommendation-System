from tkinter import *
from pygame import mixer
from Beatbox6 import getsonglist
import os


songlist=list()
songlist=getsonglist()
index=(0,)
def play(event):
    global paused
    global index
    if(l1.curselection()):
        index=l1.curselection()
        songname=l1.get(index[0])
        if not mixer.music.get_busy()or paused:
            try:
                mixer.music.load(f"sMusic/{songname}")
                mixer.music.play()
                p1.configure(image=simage)
                paused = False
            except Exception as e:
                print(f"Error loading or playing the song: {e}")
        else:
            mixer.music.pause()
            p1.configure(image=pimage if paused else pimage)
            paused=not paused

def stop():
    mixer.music.stop()
    p1.configure(image=pimage)
    global paused
    paused=False


def previous():
    global index
    if index[0]==0:
        mixer.music.play()
    else:
        mixer.music.load("sMusic/"+l1.get(index[0]))
        mixer.music.play()

def next():
    global index
    if index[0]==0:
        mixer.music.play()
    if cur_song_index < len(songlist) - 1:
        cur_song_index += 1
        play_selected_song()

def play_selected_song():
    global paused
    songname = songlist[cur_song_index]
    mixer.music.load("sMusic/"+songname)
    
    if not paused:
        mixer.music.play()
        p1.configure(image=simage)
    else:
        mixer.music.pause()
        p1.configure(image=simage)
        paused = not paused


win=Tk()
win.title("BeatBox")
win.geometry("1920x1080+0+0")

bg_img=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","back.png"))
canvas=Canvas(win,width=1600,height=1100)
canvas.place(x=0,y=0)
canvas.create_image(600,350,anchor=CENTER,image=bg_img)


l1=Listbox(win,height=25,width=140)
for song in songlist:
    l1.insert(1,song)
l1.place(x=170,y=190)
l1.bind('<Button>',play)

mixer.init()
paused=False
cur_song_index=0

pimage=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fplay.png"))
p1=Button(win,image=pimage,height=50,width=50)
p1.bind('<Button>',play)
p1.place(x=600,y=550)

nimage=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fnext.png"))
p2=Button(win,image=nimage,height=50,width=50,command=stop)
p2.place(x=692,y=550)

fimage=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fprevious.png"))
p3=Button(win,image=fimage,height=50,width=50,command=previous)
p3.place(x=508,y=550)

simage=PhotoImage(file=os.path.join(os.path.dirname(__file__), "images","fpause.png"))

