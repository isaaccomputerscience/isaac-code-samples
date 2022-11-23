# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

from tkinter import *
from tkinter import messagebox
from order_form import display_order_form

def display_login_form():
    """Login form for Kiara's cakes"""

    def login():
        """Login script"""
        userid = txt_userid.get()
        password = txt_password.get()        
        if userid != "Kiara":
            messagebox.showinfo("Error", "Incorrect user id")
            txt_userid.focus()
        elif password != "doughnut":
            messagebox.showinfo("Error", "Incorrect password")
            txt_password.focus()
        else: # user id and password match
            login_form.destroy()
            display_order_form()
            
    
    # Application window
    login_form = Tk()
    login_form.title("Kiara's Cakes")
    login_form.geometry("400x300") # Width x Height
    login_form.config(bg="#f5fffa")
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

    btn_login = Button(login_form)
    btn_login.config(text="Sign in", command=login)   
    btn_login.pack()
    
    # Mainloop
    login_form.mainloop()    
    

if __name__ == "__main__":
    display_login_form()
