# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

from tkinter import *

class tkinter_example():
    def __init__(self, master):
        self.txt_user_name = Entry(master) # Creates instance of entry widget
        self.txt_user_name.pack() # Positions entry widget on the form

        self.btn_push_me = Button(master, text="Push me!", command=self.display_name) # Creates instance of button widget
        self.btn_push_me.pack() # Positions button on the form

    def display_name(self):
        user_name = self.txt_user_name.get() # Gets the value from the text entry box
        print(user_name) # will display the name entered in the console window (just for testing)
    

# This code will run if this file is executed directly
# (i.e. not called by another program)

if __name__ == '__main__':
    master = Tk() # Create an instance of a tkinter window
    master.geometry("500x500") # Make the window big enough to see
    gui = tkinter_example(master)
    master.mainloop() # Run the application
