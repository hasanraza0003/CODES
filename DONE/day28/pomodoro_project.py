from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_button():
    window.after_cancel(timer)
    timer_but.config(text="Timer")
    tick.config(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"normal"))
    canvas.itemconfig(timer_text,text="00:00")
    global reps
    reps+=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        timer_but.config(text="Break",fg=RED,bg=YELLOW,font=("courier",50,"bold"))
        count_down(long_break_sec)
    elif reps%2==0:
        timer_but.config(text="Break",fg=PINK,bg=YELLOW,font=("courier",50,"bold"))
        count_down(short_break_sec)
    else:
        timer_but.config(text="Work",fg=GREEN,bg=YELLOW,font=("courier",50,"bold"))
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min= math.floor(count/60)
    count_sec= count%60
    if count_sec < 10 :
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")   #canvas.itemconfig  used for change the value at the runtime in canvas
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)                  #.after used for screen update after some sort of time
    else:
        start_timer()
        marks=" "
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✓"
        tick.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW , highlightthickness=0)
image_tomato = PhotoImage(file=r"day28\tomato.png")
canvas.create_image(100,112,image= image_tomato)
timer_text = canvas.create_text(102,130,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(column=2,row=2)

timer_but=Label(text="Timer",fg=GREEN,bg=YELLOW,font=("courier",50,"bold"))
timer_but.grid(column=2,row=1)

start=Button(text="Start",bg=YELLOW,command=start_timer)
start.grid(column=1,row=3)

reset=Button(text="Reset",bg=YELLOW,command=reset_button)
reset.grid(column=3,row=3)

tick=Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,20,"normal"))
tick.grid(column=2,row=4)

window.mainloop()