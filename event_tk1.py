from tkinter import *

window = Tk()
window.title("even handler demo")
window.geometry("100x100")

def handle_click(event):
    print("you clicked the button")

def handle_keypress(event):
    print({event.char})

window.bind("<Button-1>", handle_click)
button = Button( text="click me")
button.pack()

button.bind("<Button-1>", handle_click)

window.mainloop()