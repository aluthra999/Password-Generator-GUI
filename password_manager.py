import random
import tkinter
from tkinter import *

# -------- PASSWORD GENERATOR ------------ #


def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&'\()*+/<>;:[]?,._-=|"

    v = tkinter.StringVar()
    password = ""
    for x in range(0, 12):
        password_char = random.choice(chars)
        password = password + password_char

    v.set(password)
    password_entry.config(textvariable=v)


# -------------- SAVE PASSWORDS -----------------------#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open('data.txt', 'a') as f:
        f.write(f"{website} | {email} | {password}\n")

    website_entry.delete(0, END)
    password_entry.delete(0, END)


# ------------------- UI SETUP ------------------------ #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=36)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=36)
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=31, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
