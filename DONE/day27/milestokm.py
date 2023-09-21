from tkinter import *

screen = Tk()
screen.title("Mile To Km Converter")


input=Entry()
input.insert(END,string="0")
input.grid(column=2,row=1)

miles=Label(text="Miles")
miles.grid(column=3,row=1)

is_equal_to=Label(text="is equal to")
is_equal_to.grid(column=1,row=2)

output=Label(text="0")
output.grid(column=2,row=2)

km=Label(text="Km")
km.grid(column=3,row=2)

def calculate():
    result = round((float(input.get()) * 1.609344) , 3)
    op=output.config(text=result)
    return op
button= Button(text="Calculate",command=calculate)
button.grid(column=2,row=3)













































screen.mainloop()