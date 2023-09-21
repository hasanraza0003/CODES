from tkinter import *
import random
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

# Read Data
try:
    data=pd.read_csv(r"day31\data\words_to_learn")
except FileNotFoundError:
    original_data=pd.read_csv(r"day31\data\french_words.csv")
    to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

new_dict={}

# timer
def flip_card():
    canvas.itemconfig(img,image=newimg)
    canvas.itemconfig(f,text="English",fill="white")
    canvas.itemconfig(tran_f,text=new_dict["English"],fill="white")

# Choice Random word
def rand_choice():
    global new_dict,flip_timer
    screen.after_cancel(flip_timer)
    new_dict = random.choice(to_learn)
    canvas.itemconfig(f,text="French",fill="black")
    canvas.itemconfig(tran_f,text=new_dict["French"],fill="black")
    canvas.itemconfig(img,image=oldimg)
    flip_timer=screen.after(3000,func=flip_card)

# New WORD list
def is_known():
    to_learn.remove(new_dict)
    data = pd.DataFrame(to_learn)
    data.to_csv("day31/data/words_to_learn",index=False)
    rand_choice()

#  UI
screen = Tk()
screen.title("FLashy")
screen.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer=screen.after(3000,func=flip_card)

# Canvas
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
oldimg=PhotoImage(file=r"day31\images\card_front.png")
newimg=PhotoImage(file=r"day31/images/card_back.png")
img=canvas.create_image(400,263,image=oldimg)
f=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
tran_f=canvas.create_text(400,263,text="",font=("Ariel",40,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

# Buttons
imgw=PhotoImage(file=r"day31\images\wrong.png")
wrong=Button(image=imgw,bg=BACKGROUND_COLOR,highlightthickness=0,command=rand_choice)
wrong.grid(column=0,row=1)

imgr=PhotoImage(file=r"day31\images\right.png")
right=Button(image=imgr,bg=BACKGROUND_COLOR,highlightthickness=0,command=is_known)
right.grid(column=1,row=1)

rand_choice()
screen.mainloop()

