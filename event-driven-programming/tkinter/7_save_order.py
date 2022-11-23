# Raspberry Pi Foundation
# Developed to be used alongside Isaac Computer Science,
# part of the National Centre for Computing Education
# Usage licensed under CC BY-SA 4

from tkinter import *

def display_order_form():
    """Order form for Kiara's cakes"""

    def save_order():
        """Validates and saves order"""
        # Get values from variables
        customer = var_customer.get()
        item = var_item.get()
        qty = var_qty.get()
        
        # Validation should be added here
        
        # Write order details to file
        with open("orders.csv", mode = "a") as file_object:        
            file_object.write(customer + "," + item + "," + qty + "\n")
            # Confirm success
            var_msg.set("Confirmation - Order saved")
            clear_form()

    def clear_form():
        """Clears order form"""
        var_customer.set("")
        var_item.set("")
        var_qty.set("")            
        txt_customer.focus()
    
    # main window
    order_form = Tk()
    order_form.title("Kiara's Cakes")
    order_form.geometry("400x300") # Width x Height
    order_form.config(bg="#f5fffa")
    order_form.option_add("*font", "Verdana 10")

    # variables
    var_customer = StringVar()
    var_item = StringVar()
    var_qty = StringVar()
    var_msg = StringVar()
    
    # widgets
    lbl_customer = Label(order_form)
    lbl_customer.config(text="Customer", bg="#f5fffa")
    lbl_customer.pack()
        
    txt_customer = Entry(order_form)
    txt_customer.config(textvariable=var_customer)
    txt_customer.pack()
    
    lbl_item = Label(order_form)
    lbl_item.config(text="Item code", bg="#f5fffa")
    lbl_item.pack()
        
    txt_item = Entry(order_form)
    txt_item.config(textvariable=var_item)
    txt_item.pack()
    
    lbl_qty = Label(order_form)
    lbl_qty.config(text="Item quantity", bg="#f5fffa")
    lbl_qty.pack()    
    
    txt_qty = Entry(order_form)
    txt_qty.config(textvariable=var_qty)
    txt_qty.pack()

    btn_save = Button(order_form)
    btn_save.config(text="Save", command = save_order)
    btn_save.pack()

    var_msg.set("Type the order details and press Save")
    lbl_msg = Label(order_form)
    lbl_msg.config(textvariable=var_msg, bg="#f5fffa")
    lbl_msg.pack() 

    # main loop
    order_form.mainloop()
    

if __name__ == "__main__":
    display_order_form()

