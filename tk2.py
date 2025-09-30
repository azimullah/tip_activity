from tkinter import *
from  datetime import  date


root = Tk()

root .title("getting started with widgets")
root .geometry("400x300")

lbl = Label(root, text = "Hello World" , font = ("Arial Bold", 50))
namelbl = Label(root, text = "Enter your name", bg = '#3895D3') 
name_entry = Entry(root) 
def diplay():
 global message 
 message = " hello welcome to the appplication \n today's date is " 
 greet =  "hello" + name_entry .get ()+"\n"
 text_box .insert(END, greet)
 text_box .insert(END, message)
 text_box .insert(END, date .today())

text_box = Text(root, height = 3)  
btn = Button( text = "begin", command = diplay , height = 1, bg = '#1261A0', fg = 'white' )

lbl. pack()
namelbl .pack()
name_entry .pack()
btn .pack()
text_box .pack()

root .mainloop()


