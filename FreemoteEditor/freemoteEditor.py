import tkinter
from moviepy.editor import *
import os
from tkinter import *
from tkinter import ttk

n = os.listdir()

def generate():
    for x in n:
        try:
            if x.split(".")[1] == "gif":
                emote = VideoFileClip(x)
                e_width = emote.w
                e_height = emote.h
                print(emote.size)
                if e_width == 49 and e_height == 49:
                    print("Already a Freemote")
                    pass
                else:
                    n1 = 49
                    n2 = 49
                    emote_resize = emote.resize((n1, n2))
                    emote_resize.write_gif(f"{x}_freemote.gif")
                    print(f"Successfully Converted: {x}")
                print(e_width, e_height)
        except:
            pass

##### Optional #####
root = Tk()
root.title("FreemoteEditor")

c1 = Canvas(root, width=300, height=200, background='gray75')
c1.pack()


b = Button(c1, text = 'Generate all emotes', command=generate)
b.pack(side = TOP, padx=300, pady=200)

myico = PhotoImage(file = 'lolw.png')
root.iconphoto(True, myico)

root.mainloop()
