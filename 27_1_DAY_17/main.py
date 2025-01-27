import tkinter

window = tkinter.Tk()
window.title("FIRST TKINTER")
window.minsize(500, 300)
window.config(padx=100, pady=50)

# label widget
tk_lable = tkinter.Label(text="hello world", font="arial")
# tk_lable.pack()
# tk_lable.place(x=100,y=200)
tk_lable.grid(column=0,row=0)
# tk_lable["text"]="new hello"
# tk_lable.config(text="new hii")


# entry widget
entry = tkinter.Entry(width=50)
# entry.pack()
entry.grid(column =1,row=1)
# print(entry.get())


# button widget
def button_click():
    print("i got clicked")
    new_text = entry.get()
    tk_lable.config(text=new_text)
    # button.config(text="button got clicked")


button = tkinter.Button(text="click here", command=button_click ,justify= tkinter.CENTER)
# button.pack()
button.grid(column =3,row=2)

button2=tkinter.Button(text="click here.")
button2.grid(column=2,row=0)

window.mainloop()

# other widget like below.
# text widget
# spinbox
# scale
# check button
# radio box
# listbox



# from tkinter import *
#
# # creating window
# window = Tk()
# window.title("My first Gui program")
# window.minsize(width=500, height=500)
#
# # label
# l = Label(text="hello world1")
# l.config(text="hello world ")
# l.pack()
#
#
# # button
# def action():
#     print("do something")
#
#
# button = Button(text="click", command=action)
# button.pack()
#