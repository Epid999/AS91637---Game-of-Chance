from tkinter import *
import random

# Colours
bgclr = "#3399FF" #Light Blue
btn1clr = "#999999" #Grey
btn2clr = "#666666" #Dark Grey
fnt1clr = "#FFFFFF" #White
fnt2clr = "#000000" #Black
class displayMenu:
    def __init__(self, parent):
        # Main Panel GUI,
        self.generateFrame = Frame(parent, bg=bgclr)
        self.generateFrame.grid()
        
        self.gameheading_label = Label(self.generateFrame, text="Lucky Unicorn", font="Arial 24 bold", padx=10, pady=10,  bg=bgclr, fg=fnt1clr)
        self.gameheading_label.grid(row=0, column=1)
        
        self.gameheading_label = Label(self.generateFrame, text="Enter name: ", font="Arial 16", padx=10, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_label.grid(row=1, column=0)

        isString = StringVar()
        self.nameinput = Entry(self.generateFrame, width="15", highlightbackground=bgclr, textvariable=isString)
        self.nameinput.grid(row=1, column=1)

        self.gameheading_label = Label(self.generateFrame, text="Enter cash: ", font="Arial 16", padx=10, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_label.grid(row=2, column=0)

        isFloat = float()
        self.cashinput = Entry(self.generateFrame, width="15", highlightbackground=bgclr, textvariable=isFloat)
        self.cashinput.grid(row=2, column=1)

        self.button1 = Button(self.generateFrame, text="Start", font="Arial 16 bold", bg=fnt2clr, highlightbackground=bgclr, fg=fnt2clr, relief="solid", width="15", command=self.game)
        self.button1.grid(row=3, column=0)

        self.button2 = Button(self.generateFrame, text="Help", font="Arial 16 bold", bg=fnt2clr, highlightbackground=bgclr, fg=fnt2clr, relief="solid", width="15", command=self.help)
        self.button2.grid(row=3, column=1)

        self.button3 = Button(self.generateFrame, text="Quit", font="Arial 16 bold", bg=fnt2clr, highlightbackground=bgclr, fg=fnt2clr, relief="solid", width="15", command=self.quit)
        self.button3.grid(row=3, column=2)       

    def help(self):
        get_help = Help()

    def quit(self):
        root.destroy()

    def game(self):
        get_game = Game(self.nameinput.get(), self.cashinput.get())
        

class Help:
    def __init__(self):
        
        self.help_box = Toplevel()
        self.help_box.configure(bg=bgclr)
        self.help_frame = Frame(self.help_box, bg=bgclr)
        self.help_frame.grid()

        self.gameheading_label = Label(self.help_box, text="Lucky Unicorn", font="Arial 24 bold", padx=10, pady=10,  bg=bgclr, fg=fnt1clr)
        self.gameheading_label.grid(row=0, column=1)
        
        self.gameheading_text = Label(self.help_box, text='''
        In this game you have a chance to earn a lot of money. 
        You do this by dealing yourself cards and you get a 
        certain amount of money each time you deal yourself a
        new hand. There are four different cards you can be 
        dealt. Unicorns, give you the most amount of money, 
        followed by hearts, stars, then lastly, jacks. Each 
        time you deal a hand a it costs $1 to deal yourself a
        new hand. Good luck and most importantly, have fun!''', font="Arial 12", padx=10, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text.grid(row=1, column=1)
        
        self.filler1 = Label(self.help_box, width="15", bg=bgclr)
        self.filler1.grid(row=2, column=0)

        self.filler2 = Label(self.help_box, width="15", bg=bgclr)
        self.filler2.grid(row=2, column=1)

        self.button3 = Button(self.help_box, text="Close", font="Arial 16 bold", bg=fnt2clr, highlightbackground=bgclr, fg=fnt2clr,  relief="solid", width="15", command=self.help_box.destroy)
        self.button3.grid(row=2, column=2)

class Game:
    global cards
    cards = ['Jack in the Box','Star', 'Unicorn', 'Heart'] 

    def __init__(self, name, balance):
        global displayCash
        displayCash = balance
        displayName = ("Welcome {}!".format(name))
        self.game_box = Toplevel()
        self.game_box.configure(bg=bgclr)
        self.game_frame = Frame(self.game_box, bg=bgclr)
        self.game_frame.grid()

        self.gameheading_label = Label(self.game_box, text=displayName, font="Arial 16 bold", padx=10, pady=10,  bg=bgclr, fg=fnt1clr)
        self.gameheading_label.grid(row=0, column=1)

        self.gameheading_label = Label(self.game_box, text="Lucky Unicorn", font="Arial 24 bold", padx=10, pady=10,  bg=bgclr, fg=fnt1clr)
        self.gameheading_label.grid(row=1, column=1)
        
        self.gameheading_text = Label(self.game_box, text="Result", font="Arial 16", padx=10, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text.grid(row=3, column=1)        
        
        self.gameheading_text = Label(self.game_box, text=("${}".format(displayCash)), font="Arial 16", padx=10, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text.grid(row=4, column=1)      

        roll1 = ['Unknown'] 
        roll2 = ['Unknown']
        roll3 = ['Unknown']

        self.gameheading_text1 = Label(self.game_box, text=random.choice(roll1), font="Arial 12", padx=10, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text1.grid(row=2, column=0)

        self.gameheading_text2 = Label(self.game_box, text=random.choice(roll2), font="Arial 12", padx=10, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text2.grid(row=2, column=1)

        self.gameheading_text3 = Label(self.game_box, text=random.choice(roll3), font="Arial 12", padx=10, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text3.grid(row=2, column=2)

        self.button1 = Button(self.game_box, text="Roll", font="Arial 16 bold", highlightbackground=bgclr, relief="solid", width="15", command=self.roll)
        self.button1.grid(row=5, column=0)

        self.button2 = Button(self.game_box, text="Cash Out", font="Arial 16 bold", highlightbackground=bgclr, relief="solid", width="15")
        self.button2.grid(row=5, column=1)

        self.button3 = Button(self.game_box, text="Quit", font="Arial 16 bold", bg=fnt2clr, highlightbackground=bgclr, fg=fnt2clr, relief="solid", width="15", command=self.game_box.destroy)
        self.button3.grid(row=5, column=2)
    
    def matching(self, card1, card2, card3):
        if (card1 == card2 == card3):
            return 3
        elif (card1 == card2):
            return 2
        elif (card1 == card3):
            return 2
        elif (card2 == card3):
            return 2
        else:
            return 1
    
    def matchingCard(self, card1, card2, card3):
        if self.matching(card1, card2, card3) == 3:
            return card1
        elif self.matching(card1, card2, card3) == 2:
            if card2 == card3:
                return card2
        else:
            return card1

    def roll(self):
        displayCash = 20
        displayCash -= 1.0
        roll1 = random.choice(cards.copy())
        roll2 = random.choice(cards.copy())
        roll3 = random.choice(cards.copy())
        result = "You lost"
        winnings = 0.0

        if self.matching(roll1, roll2, roll3) == 3:
            if roll1 == cards[0]: #Jack in the Box x3
                winnings == 1.0
            elif roll1 == cards[1]: #Star x3
                winnings == 2.5
            elif roll1 == cards[2]: #Unicorn x3
                winnings == 5.0
            else: #Hear x3
                winnings == 2.5
        elif self.matching(roll1, roll2, roll3) == 2:
            if self.matchingCard(roll1, roll2, roll3) == cards[0]:
                #If there are two of the same and one unicorn, give player
                #$1.50
                if roll1 == cards[2]:
                    winnings == 1.5
                elif roll2 == cards[2]:
                    winnings == 1.5
                elif roll3 == cards[2]:
                    winnings == 1.5
                else: #Jack in the Box x2
                    winnings == 0.0
            elif self.matchingCard(roll1, roll2, roll3) == cards[1]:
                #If there are two of the same and one unicorn, give player
                #$1.50
                if roll1 == cards[2]:
                    winnings == 1.5
                elif roll2 == cards[2]:
                    winnings == 1.5
                elif roll3 == cards[2]:
                    winnings == 1.5
                else:
                    winnings == 1.0 #Star x2
            elif self.matchingCard(roll1, roll2, roll3) == cards[2]:
                winning == 2.0 #Unicorn x2 (Don't need to check for third unicorn, as they would get a prize
                               #from another if statement)
            else:
                #If there are two of the same and one unicorn, give player
                #$1.50
                if roll1 == cards[2]:
                    winnings == 1.5
                elif roll2 == cards[2]:
                    winnings == 1.5
                elif roll3 == cards[2]:
                    winnings == 1.5
                else:
                    winnings == 1.0 #Heart x2
        else:
            winnings == 0.0
        
        if winnings >= 1.0:
            results == "You won!"
        else:
            results == results

        displayCash += winnings

        self.gameheading_text1 = Label(self.game_box, text=roll1, font="Arial 12", padx=35, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text1.grid(row=1, column=0)

        self.gameheading_text2 = Label(self.game_box, text=roll2, font="Arial 12", padx=35, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text2.grid(row=1, column=1)

        self.gameheading_text3 = Label(self.game_box, text=roll3, font="Arial 12", padx=35, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text3.grid(row=1, column=2)
        
        self.gameheading_text = Label(self.game_box, text=result, font="Arial 16", padx=10, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text.grid(row=2, column=1)

        self.gameheading_text = Label(self.game_box, text=displayCash, font="Arial 16", padx=10, pady=10,  bg=bgclr, fg=fnt2clr)
        self.gameheading_text.grid(row=3, column=1)
       

#Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Lucky Unicorn")
    Generate = displayMenu(root)
    root.configure(bg=bgclr)
    root.resizable(width=False, height=False)    
    root.mainloop()