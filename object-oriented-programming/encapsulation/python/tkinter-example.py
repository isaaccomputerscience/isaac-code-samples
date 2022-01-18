# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

from tkinter import Tk, StringVar, Entry

def tkinter_example():
    master = Tk()
    master.geometry("500x500")  # Make the window big enough to see

    var_user_name = StringVar() # Creates instance of tkinter variable
    txt_user_name = Entry(master, textvariable=var_user_name) # Creates instance of entry widget
    txt_user_name.pack() # Positions entry widget on the form
    user_name = var_user_name.get() # Gets the value from the tkinter variable

    master.mainloop()


if __name__ == '__main__':
    tkinter_example()