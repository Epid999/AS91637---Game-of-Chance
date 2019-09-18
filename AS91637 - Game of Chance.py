from tkinter import *
import random

# Game of Chance
# Lucky Unicorn

# Colours
bgclr = "#3399FF" #Light Blue
obj1clr = "#" #Yellow
obj2clr = "#" #Orange
btn1clr = "#999999" #Grey
btn2clr = "#666666" #Dark Grey
fnt1clr = "White"
fnt2clr = "Black"

class DisplayMenu:
    def __init__(self, parent):
        
        #Setting up the frame for GUI
        self.generateFrame = Frame(parent)
        self.generateFrame.grid()
        
        # **GUI**
        #Start

        self.button1 = Button(text="Start", 
                                    font="Arial 24 bold", bg=btn1clr, activebackground=btn2clr, 
                                    fg="White", padx="25", pady="10", command=self.btn_clr)
        self.button1.place (x="-145.5", y="142")
        
        #Help

        self.button2 = Button(text="Help", 
                                    font="Arial 24 bold", bg=btn1clr, activebackground=btn2clr, 
                                    fg="White", padx="25", pady="10", command=self.btn_clr)
        self.button2.place (x="49.5", y="142")

        #Quit

        self.button3 = Button(text="Quit", 
                                    font="Arial 24 bold", bg=btn1clr, activebackground=btn2clr, 
                                    fg="White", padx="25", pady="10", command=self.openButton3)
        self.button3.place (x="242.5", y="142")

        #Title
        
        self.title = Label(text="Lucky Unicorns", font="Arial 24 bold", bg=bgclr, fg=fnt1clr)
        self.title.grid(row=0)

    def btn_clr(self):
        self.button.configure(bg="#999999")

    def openButton3(self):
            # **Generate Window**
            quit =Tk()
            quit.title("Lucky Unicorn - Quit")
            quit.configure(bg=bgclr)
            quit.geometry("400x200")
            Generate = DisplayMenu(root)
       
           # **GUI**        
            self.quitButton1 = Button(self, text="Yes", font="Arial 24 bold", bg=btn1clr, activebackground=btn2clr, fg="White", padx="25", pady="10", command=self.btn_clr).__init__()

            quitButton2 = Button(self, text="No", 
                                        font="Arial 24 bold", bg=btn1clr, activebackground=btn2clr, 
                                        fg="White", padx="25", pady="10", command=self.btn_clr).__init__()
            quitButton2.grid (row=0)

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Lucky Unicorn")
    Generate = DisplayMenu(root)
    root.configure(bg=bgclr, padx="300", pady="240")
    root.resizable(width=False, height=False)
    root.mainloop()