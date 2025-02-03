from tkinter import *
import pandas as pd
import random

BG = "#add9c1"
current_card = {}
to_learn ={}
# data
try:
    data = pd.read_csv("data/learn_words.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def next_card():
    global current_card, flipper_timer
    window.after_cancel(flipper_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(image_front, image=front_image)
    flipper_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data=pd.DataFrame(to_learn)
    data.to_csv("data/learn_words.csv",index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(image_front, image=back_image)


# UI
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BG)
flipper_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
image_front = canvas.create_image(400, 263, image=front_image)

# back_image = PhotoImage("images/card_back.png")
# image_back=canvas.create_image(400, 263, image=back_image)

card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "bold"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BG, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross = Button(image=cross_image, highlightthickness=0, command=next_card)
cross.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=is_known)
right.grid(row=1, column=1)

next_card()
window.mainloop()
