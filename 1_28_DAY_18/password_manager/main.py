# day29
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import string
import pyperclip
import json


def save():
    web = website_Entry.get()
    email = e_entry.get()
    password = pass_entry.get()
    new_data = {
        web: {"email": email, "password": password}
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any field empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        # FileNotFoundError or JSONDecodeError
        except:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_Entry.delete(0, END)
            pass_entry.delete(0, END)


# find password

def find_password():
    website = website_Entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="Error", message=" there no data  file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email} \nPassword:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No detail exist for {website}. ")


# password generator
def press_generate():
    letters = []
    s1 = string.ascii_letters
    for char in s1:
        letters.append(char)

    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    symbols = ['@', '#', '$', '%', '*', '!']

    n_letters = random.randint(1, 5)
    n_numbers = random.randint(2, 5)
    n_symbol = random.randint(3, 5)

    letter_list = [random.choice(s1) for _ in range(n_letters)]
    n_list = [random.choice(numbers) for _ in range(n_numbers)]
    sym_list = [random.choice(symbols) for _ in range(n_symbol)]

    pass_list = letter_list + n_list + sym_list

    random.shuffle(pass_list)

    password_1 = ""
    for i in pass_list:
        password_1 += str(i)
    # password_1 ="".join(pass_list)
    pass_entry.insert(0, password_1)
    pyperclip.copy(password_1)


# UI
window = Tk()
window.title("password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

e_label = Label(text="Email/Username:")
e_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

website_Entry = Entry(width=33)
website_Entry.grid(column=1, row=1)

e_entry = Entry(width=52)
e_entry.grid(column=1, row=2, columnspan=2)
e_entry.insert(0, "sneha1@aliansoftware.com")

pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password", command=press_generate)
generate_pass_button.grid(column=2, row=3)

button = Button(text="Add", width=45, command=save)
button.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=14, command=find_password)
search.grid(column=2, row=1)

window.mainloop()
