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
                                    font="Arial 24 bold", bg="Black", 
                                    fg="White", padx="50", pady="20", command=self.btn_clr)
        self.button1.place (x="-180.5", y="142")
        
        #Help

        self.button2 = Button(text="Help", 
                                    font="Arial 24 bold", bg="Black", 
                                    fg="White", padx="50", pady="20", command=self.btn_clr)
        self.button2.place (x="14.5", y="142")

        #Quit

        self.button3 = Button(text="Quit", 
                                    font="Arial 24 bold", bg="Black", 
                                    fg="White", padx="50", pady="20", command=self.btn_clr)
        self.button3.place (x="208.5", y="142")

        #Title
        
        self.title = Label(text="Lucky Unicorns", font="Arial 24 bold", bg="White")
        self.title.grid(row=0)

    def btn_clr(self):
        self.button.configure(bg="#999999")

    def window_quit(self):
        self.newWindow = karl2()

class karl2(Frame):     
    def __init__(self):
        new =tk.Frame.__init__(self)
        new = Toplevel(self)
        new.title("karlos More Window")
        new.button = tk.Button(  text = "PRESS TO CLOSE", width = 25,
                                 command = self.close_window )
        new.button.pack()
    def close_window(self):
        self.destroy()

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Lucky Unicorn")
    Generate = DisplayMenu(root)
    root.configure(bg=bgclr, padx="300", pady="240")
    root.mainloop()