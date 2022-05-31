# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

from tkinter import *


def display_login_form():
    """Login form for Kiara's cakes"""
    login_form = Tk()
    login_form.title("Kiara's Cakes")
    login_form.geometry("400x300") # Width x Height
    login_form.configure(bg="#f5fffa")
    login_form.option_add("*font", "Verdana 10")
    login_form.mainloop()

if __name__ == "__main__":
    display_login_form()
