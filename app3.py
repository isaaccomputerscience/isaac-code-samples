# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

from tkinter import *


def display_login_form():
    """Login form for Kiara's cakes"""
    # Application window
    login_form = Tk()
    login_form.title("Kiara's Cakes")
    login_form.geometry("400x300") # Width x Height
    login_form.configure(bg="#f5fffa")
    login_form.option_add("*font", "Verdana 10")
    
    # Widgets
    lbl_userid = Label(login_form)
    lbl_userid.config(bg="#f5fffa", text="User id")
    lbl_userid.pack()

    txt_userid = Entry(login_form)
    txt_userid.pack()   
  
    lbl_password = Label(login_form)
    lbl_password.config(bg="#f5fffa", text="Password")
    lbl_password.pack()

    txt_password = Entry(login_form)
    txt_password.pack() 
    
    # Mainloop
    login_form.mainloop()    
    

if __name__ == "__main__":
    display_login_form()
