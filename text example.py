from tkinter import *
import random

# Colours
bgclr = "#3399FF" #Light Blue
obj1clr = "#" #Yellow
obj2clr = "#" #Orange
btn1clr = "#999999" #Grey
btn2clr = "#666666" #Dark Grey
fnt1clr = "White"
fnt2clr = "Black"

def btn_clr(root):
    root.button.configure(bg="#999999")

def openButton3(root):
        # **Generate Window**
        quit =Tk()
        quit.title("Lucky Unicorn - Quit")
        quit.configure(bg=bgclr)
        quit.geometry("350x155")
       
        # **GUI**        
        root.quitButton1 = Button(root, text="Yes", font="Arial 24 bold", bg=btn1clr, activebackground=btn2clr, fg="White", padx="25", pady="10")
        root.quitButton1.place(x="-0.5", y="0.2"),
        quitButton2 = Button(root, text="No", 
                                    font="Arial 24 bold", bg=btn1clr, activebackground=btn2clr, 
                                    fg="White", padx="25", pady="10")
        quitButton2.grid (row=0)

root = Tk()
root.title("Lucky Unicorn")
root.configure(bg=bgclr)
root.geometry("540x400")
root.resizable(width=False, height=False)
   
# **GUI**
#Start
root.button1 = Button(root, text="Start", 
                            font="Arial 24 bold", bg=btn1clr, activebackground=btn2clr, 
                            fg="White", padx="25", pady="10")
root.button1.place (x="-145.5", y="142")
        
#Help

root.button2 = Button(root, text="Help", 
                            font="Arial 24 bold", bg=btn1clr, activebackground=btn2clr, 
                            fg="White", padx="25", pady="10")
root.button2.place (x="49.5", y="142")

#Quit

root.button3 = Button(root, text="Quit", 
                            font="Arial 24 bold", bg=btn1clr, activebackground=btn2clr, 
                            fg="White", padx="25", pady="10", command=root.openButton3)
root.button3.place (x="242.5", y="142")

#Title
        
root.title = Label(root, text="Lucky Unicorns", font="Arial 24 bold", bg=bgclr, fg=fnt1clr)
root.title.grid(row=0)

button1=Button(root, text="Demo", fg='white', bg='brown', relief="solid", font=("arial", 12,"bold"))
button1.place(x=110, y=110)

root.mainloop()
