from tkinter import *


def mile_to_kilo():
    miles = float(mile_input.get())
    km = miles * float(1.609)
    km_result_label.config(f"{km}")


window = Tk()
window.title("mile to kilo converter")
window.config(padx=20, pady=20)

mile_input = Entry()
mile_input.grid(column=1, row=0)

mile_label = Label(text="Mile")
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

is_equal_to_label = Label(text="is equal to:")
is_equal_to_label.grid(column=0, row=1)

km_result_label = Label(text=0)
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=mile_to_kilo)
calculate_button.grid(column=1, row=2)
window.mainloop()
