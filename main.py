from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="DONT LEAVE A FIELD EMPTY")
    else:
        try:
            with open("data.json", "r") as f:
                #Reading old data
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as f:
                #Saving updated data
                json.dump(data, f, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if entry_website.get() in data:
            print("yes")
            messagebox.showinfo(message=f"{entry_website.get()}\n{data[entry_website.get()]["password"]}")
        else:
            print("no")
            messagebox.showinfo(message=f"No details for {entry_website} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)
label_email = Label(text="Email/Username")
label_email.grid(column=0, row=2)
label_password = Label(text="password")
label_password.grid(column=0, row=3)

#Entry
entry_website = Entry(width=21)
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()
entry_email = Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email.insert(0, "83fake@gmail.com")
entry_password = Entry(width=21)
entry_password.grid(column=1, row=3, columnspan=2, sticky="EW")

#Button
button_generate_password = Button(text="Generate Password", command=generate_password)
button_generate_password.grid(column=2, row=3)
button_add = Button(text="Add", width=35, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")
button_search = Button(text="Search", width=35, command=find_password)
button_search.grid(column=1, row=5,columnspan=2, sticky="EW")


window.mainloop()