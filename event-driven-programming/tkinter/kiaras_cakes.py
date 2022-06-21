# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

from tkinter import *
from tkinter import messagebox
import os

USERID = "Kiara01"
PASSWORD = "doughnut"


def display_order_form():
    """Displays order entry form"""

    def clear_form():
        """Clears order entry form"""
        var_customer.set("")
        var_item_code.set("")
        var_item_qty.set("")            
        var_message.set("Enter the details of the order and press save")
        txt_customer.focus()
            
    
    def save_order():
        """Validates order details and saves to file"""
        # Get values from variables
        customer = var_customer.get()
        item_code = var_item_code.get()
        item_qty = var_item_qty.get()
        
        # Validation needs to be added here
        
        # Write order details to file
        with open("orders.txt", mode = "a") as file_object:        
            file_object.write(customer + "," + item_code + "," + item_qty + "\n")
            # Clear entry boxes and confirm success
            clear_form()
            var_message.set("Confirmation - Order saved")
        
    
    # main window
    order_form = Tk()
    order_form.title("Kiara's Cakes - Orders")
    order_form.geometry("300x300")
    
    # main window frames    
    body = Frame(order_form)
    body.pack()
    
    footer = Frame(order_form)
    footer.pack()
    
    # body
    lbl_customer = Label(body, text="Customer")
    lbl_customer.grid(row=0, column=0, sticky=W, padx=5, pady=5)
    
    var_customer = StringVar()
    txt_customer = Entry(body, textvariable=var_customer)
    txt_customer.grid(row=0,column=1, sticky=W, padx=5, pady=5)

    
    lbl_item_code = Label(body, text="Item code")
    lbl_item_code.grid(row=1, column=0, sticky=W, padx=5, pady=5)
    
    var_item_code = StringVar()
    txt_item_code = Entry(body, textvariable=var_item_code)
    txt_item_code.grid(row=1,column=1, sticky=W, padx=5, pady=5)
    
    lbl_item_qty = Label(body, text="Item quantity")
    lbl_item_qty.grid(row=2, column=0, sticky=W, padx=5, pady=5)
    
    var_item_qty = StringVar()
    txt_item_qty = Entry(body, textvariable=var_item_qty)
    txt_item_qty.grid(row=2,column=1,sticky=W, padx=5, pady=5)

    # frames for buttons
    left = Frame(body)
    left.grid(row=3, column=0)
    
    right = Frame (body)       
    right.grid(row=3, column=1)
    
    btn_save = Button(right, text="Save", command = save_order)
    btn_save.pack(side=LEFT, padx=5, pady=5)
    
    btn_clear = Button(right, text="Clear", command = clear_form)
    btn_clear.pack(side=LEFT, padx=5, pady=5)

    btn_exit = Button(right, text="Exit", command = order_form.destroy)       
    btn_exit.pack(side=LEFT, padx=5, pady=5)

    # footer
    var_message = StringVar()
    var_message.set("Enter the details of the order and press save")
    lbl_message = Label(footer, textvariable=var_message)
    lbl_message.pack(side=LEFT, padx=10)


    
def display_login_form():
    """displays login form"""
    
    def login():
        """Callback function - login button"""
        userid = txt_userid.get()
        password = txt_password.get()        
        if userid != USERID:
            messagebox.showinfo("Error", "Incorrect or blank userid")
            txt_userid.focus()
        elif password != PASSWORD:
            messagebox.showinfo("Error", "Incorrect or blank password")
            txt_password.focus()
        else: # userid and password match
            sign_in_form.destroy()
            display_order_form()


    #main window
    sign_in_form = Tk()
    sign_in_form.title("Kiara's Cakes - sign in")
    sign_in_form.geometry("300x300")
    
    #widgets
    lbl_userid = Label(sign_in_form, text="User id")
    lbl_userid.pack()
    
    txt_userid = Entry(sign_in_form)
    txt_userid.pack()
    
    lbl_password = Label(sign_in_form, text="Password")
    lbl_password.pack()
    
    txt_password = Entry(sign_in_form)
    txt_password.pack()
    
    btn_login = Button(sign_in_form, text="Sign in", command=login)  
    btn_login.pack(pady=10)
    

if __name__ == "__main__":
    display_login_form()

