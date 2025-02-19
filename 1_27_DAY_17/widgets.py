from tkinter import *

# creating window
window = Tk()
window.title("all widget window")
window.minsize(width=500, height=500)

# label
l = Label(text="hello world1")
l.config(text="hello world ")
l.pack()


# button
def action():
    print("do something")


button = Button(text="click", command=action)
button.pack()

# entry
entry = Entry(width=50)
entry.insert(END, string="insert somthing")
print(entry.get())
entry.pack()

# text
text = Text(width=30, height=5)
text.insert(END, "insert some text")
text.focus()
print(text.get("1.0", END))
text.pack()


# spinbox
def spin():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spin)
spinbox.pack()


# scale
def scale1(value):
    print(value)


scale = Scale(from_=0, to=50, command=scale1)
scale.pack()


# check-button
def check():
    print(check_state.get())


check_state = IntVar()
checkbutton = Checkbutton(text="is on?", variable=check_state, command=check)
check_state.get()
checkbutton.pack()


# radiobutton
def radio_on():
    print(radio_state.get())


radio_state = IntVar()
radio1 = Radiobutton(text="option1", value=1, variable=radio_state, command=radio_on)
radio1.pack()
radio2 = Radiobutton(text="option2", value=2, variable=radio_state, command=radio_on)
radio_state.get()
radio2.pack()


# listbox

def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruit = ["mango", "orange", "guava", "grapes"]
for i in fruit:
    listbox.insert(fruit.index(i), i)
listbox.bind("<<ListboxSelect>>", listbox_used)

listbox.pack()
window.mainloop()
