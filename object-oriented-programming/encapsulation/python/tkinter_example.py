# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

from tkinter import *

class tkinter_example():
    
    def __init__(self, master):

        self.lbl_prompt = Label(master, text = "Enter your name") # Creates instance of label wigdet
        self.lbl_prompt.pack() # Positions entry widget on the form
        
        self.txt_user_name = Entry(master) # Creates instance of entry widget
        self.txt_user_name.pack() # Positions entry widget on the form
        
        self.btn_play = Button(master, text="Play Game!", command=self.welcome) # Creates instance of button widget
        self.btn_play.pack() # Positions button on the form

        self.lbl_user_name = Label(master) # Creates instance of label wigdet
        self.lbl_user_name.pack() # Positions entry widget on the form

    def welcome(self):
        user_name = self.txt_user_name.get() # Gets the value from the text entry box
        msg = "Welcome to Blackjack " + user_name
        self.lbl_user_name.config(text=msg)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':
    master = Tk() # Create an instance of a tkinter window
    master.title("BlackJack")
    master.geometry("500x500") # Make the window big enough to see
    gui = tkinter_example(master)
    master.mainloop() # Run the application
