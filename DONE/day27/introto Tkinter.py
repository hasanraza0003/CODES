from tkinter import *

window =Tk()
window.title("My First Gui Interaction")
window.minsize(width=1000,height=600)

#label
my_label = Label(text="Hello, Hasan",font=("Times Romans Sans" , 25 , "bold"))
my_label.pack()                            # if we want to show o/p in screen after one by one then we use pack function


#* modifying values in labels
my_label["text"] = "Hi ,Mr. Hasan Raza "              #method 1
my_label.config(text="Hi ,Mr.Hasan Raza ")           #METHOD 2


#Button
def button_click():
    my_label.config(text=input.get())            # input.get()   this func is used for to get input from the entry box

button= Button(text="Click me" ,command=button_click)    # when we use any function in command then
                                                         # we dont need to add ( )  parenthesis
button.pack()                                            # if we want to show o/p in screen after one by one then we use pack function

# Entry 
entry = Entry(width=30)
# Addsome text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
#position
input.pack(side="left")                    # if we want to show o/p in screen after one by one then we use pack function
input.place(x=5,y=10)                      # if we want to show o/p in screen with the help of coordinates 
input.grid(column=2,row=5)                 # if we want to show o/p in screen inthe row and column form



#Text Multi line
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()

















window.mainloop() 

