from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

#-----Password generator day 5 project ------#
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pas.insert(0, password)
    pyperclip.copy(password)

#--------Save password---------#

def save_data():
    site=web.get()
    mail=eml.get()
    code=pas.get()

    if len(site) == 0 or len(code) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {mail} "
                                                      f"\nPassword: {code} \nIs it ok to save?")
        if is_ok:
            with open(r"day29\data.txt" ,"a") as file:
                file.write(f"{site} | {mail} | {code} \n")
                web.delete(0,END)
                pas.delete(0,END)

# ------ FRONTEND SETUP------#
# screen
screen=Tk()
screen.title("Password Manager")
screen.config(padx=50,pady=20)

# image
canvas=Canvas(width=200,height=200)
logo_image=PhotoImage(file=r"day29/logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

# lABELS
website=Label(text="Website")
website.grid(column=0,row=1)

email=Label(text="Email / Username")
email.grid(column=0,row=2)

password=Label(text="Password")
password.grid(column=0,row=3)

# Entries 
web=Entry(width=52)
web.grid(row=1 , column=1,columnspan=2)

eml=Entry(width=52)
eml.grid(row=2,column=1,columnspan=2)
eml.insert(0, "www.hasanrazadell143@gmail.com")

pas=Entry(width=33)
pas.grid(row=3,column=1)

# Buttons
gen = Button(text="Generate Password",command=generate_password)
gen.grid(row=3,column=2)

add=Button(text="Add",width=45,command=save_data)
add.grid(column=1,row=4,columnspan=2)

screen.mainloop()