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
root = Tk()

def compressQuit(root, quit):
    return lambda *args, **kw: root.destroy(quit.destroy(*args, **kw))

class displayMenu(Frame):
    
    def __init__(self, parent):
        #Setting up the frame for GUI
        self.generateFrame = Frame(parent)
        self.generateFrame.grid()

        # **GUI**
        #Start
        button1 = Button(text="Start", font="Arial 24 bold", bg=btn1clr, relief="solid", activebackground=btn2clr, fg="White", width="8")
        button1.place (x="19.5", y="320")
        
        #Help
        button2 = Button(text="Help", font="Arial 24 bold", bg=btn1clr, relief="solid", activebackground=btn2clr, fg="White", width="8")
        button2.place (x="190", y="320")

        #Quit
        button3 = Button(text="Quit", font="Arial 24 bold", bg=btn1clr, relief="solid", activebackground=btn2clr, fg="White", width="8", command=openButton3())
        button3.place (x="358.5 ", y="320")

        #Title
        title = Label(text="Lucky Unicorns", font="Arial 24 bold", bg=bgclr, fg=fnt1clr)
        title.place(x="150", y="150")
        
    def openButton3():
        # **Generate Window**
        quit = Tk()
        quit.title("Lucky Unicorn - Quit")
        quit.configure(bg=bgclr)
        quit.geometry("350x155")
        quit.resizable(width=False, height=False)
        

        # **GUI**        
        quit.label1 = Label(quit, text="Are you sure you want to quit?", font="Arial 16 bold", bg=bgclr, fg=fnt1clr)
        quit.label1.place(x="20", y="10")

        quit.quitButton1 = Button(quit, text="Yes", font="Arial 24 bold", bg=btn1clr, relief="solid", activebackground=btn2clr, width="5", fg="White", command=root.destroy)
        quit.quitButton1.place(x="50", y="60")
        
        quit.quitButton2 = Button(quit, text="No", font="Arial 24 bold", bg=btn1clr, relief="solid", activebackground=btn2clr, width="5", fg="White", command=quit.destroy)
        quit.quitButton2.place(x="200", y="60")
class displayHelp:
    def __init__(self, parent, controller):
        #Setting up the frame for GUI
        tk.Frame.__init__(self, parent)
        
        # **GUI**
        #Title
        root.title = Label(text="Lucky Unicorns", font="Arial 24 bold", bg=bgclr, fg=fnt1clr)
        root.title.place(x="150", y="150")
        
        #Quit
        root.button1 = Button(root, text="Back", font="Arial 24 bold", bg=btn1clr, relief="solid", activebackground=btn2clr, fg="White", width="8", command=back)
        root.button1.place (x="358.5 ", y="320")

class displayInput:
    def __init__(self, parent, controller):
        #Setting up the frame for GUI
        tk.Frame.__init__(self, parent)
        
        # **GUI**
        #Title
        root.title = Label(text="Lucky Unicorns", font="Arial 24 bold", bg=bgclr, fg=fnt1clr)
        root.title.place(x="150", y="150")
        
        #Quit
        root.button1 = Button(root, text="Back", font="Arial 24 bold", bg=btn1clr, relief="solid", activebackground=btn2clr, fg="White", width="8", command=back)
        root.button1.place (x="358.5 ", y="320")

class displayGame:
    def __init__(self, parent, controller):
        #Setting up the frame for GUI
        tk.Frame.__init__(self, parent)
        
        # **GUI**
        #Title
        root.title = Label(text="Lucky Unicorns", font="Arial 24 bold", bg=bgclr, fg=fnt1clr)
        root.title.place(x="150", y="150")
        
        #Quit
        root.button1 = Button(root, text="Back", font="Arial 24 bold", bg=btn1clr, relief="solid", activebackground=btn2clr, fg="White", width="8", command=back)
        root.button1.place (x="358.5 ", y="320")

# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Lucky Unicorn")
    Generate = displayMenu(root)
    root.configure(bg=bgclr)
    root.geometry("540x400")
    root.resizable(width=False, height=False)
    root.mainloop()
