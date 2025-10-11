from tkinter import *
from tkinter import messagebox
 
root = Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Virus found in your system")

button = Button(root, text="Click Me", command=msg)

def deletevirus():
   messagebox.showerror("Want to delete virus")
button2 = Button(root, text="Delete Virus", command=deletevirus)
def showvirus():
    messagebox.showinfo("Virus .exe found")

BUTTON3 = Button(root, text="Show Virus", command=showvirus)
button.pack()
button2.pack()
BUTTON3.pack()


root.mainloop()