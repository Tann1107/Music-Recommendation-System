from tkinter import *
from PIL import Image, ImageTk
import cv2
import os

def play_video(video_path):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    canvas = Canvas(win, width=width, height=height)
    canvas.pack()

    def update_frame():
        ret, frame = cap.read()
        if ret:
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            photo = ImageTk.PhotoImage(Image.fromarray(rgb_frame))
            canvas.create_image(0, 0, anchor=NW, image=photo)
            canvas.photo = photo
            win.after(50, update_frame)
        else:
            cap.release()
            win.destroy()
            import Beatbox2

    update_frame()

if __name__ == "__main__":
    win = Tk()
    win.title("BeatBox")
    win.geometry("1800x1200")

    video_path = os.path.join(os.path.dirname(__file__), "images", "Beatgif.gif")
    play_video(video_path)
    win.mainloop()
