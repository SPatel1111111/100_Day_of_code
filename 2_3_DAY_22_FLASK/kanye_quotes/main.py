from tkinter import *
import requests


#API call
def get_quotes():
    response=requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data=response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text,text=quote)


#ui
window =Tk()
window.title("kanye say...")
window.config(padx=50,pady=50)

canvas = Canvas(width=300,height=414)
background_image =PhotoImage(file="background.png")
canvas.create_image(150,207, image=background_image)
quote_text=canvas.create_text(150,207,text="kanye quotes goes here",width=270,font=("Arial",17,"bold"),fill="white")
canvas.grid(row=0,column=0)

kanye_image =PhotoImage(file="kanye.png")
kanye_button=Button(image=kanye_image,highlightthickness=0,command=get_quotes)
kanye_button.grid(row=1,column=0)
window.mainloop()


