# Isaac Computer Science
# Usage licensed under the Open Government Licence v3.0

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
        """Clears order entry form"""
        var_customer.set("")
        var_item.set("")
        var_qty.set("")            
        txt_customer.focus()
    
    # main window
    order_form = Tk()
    order_form.title("Kiara's Cakes")
    order_form.geometry("400x300") # Width x Height
    order_form.configure(bg="#f5fffa")
    order_form.option_add("*font", "Verdana 10")

    # variables
    var_customer = StringVar()
    var_item = StringVar()
    var_qty = StringVar()
    var_msg = StringVar()    
    
    # widgets
    lbl_customer = Label(order_form)
    lbl_customer.config(text="Customer", bg="#f5fffa")
    lbl_customer.grid(row=0, column=0, padx=5, pady=15)
        
    txt_customer = Entry(order_form)
    txt_customer.config(textvariable=var_customer)
    txt_customer.grid(row=0, column=1, padx=5, pady=5)
    
    lbl_item = Label(order_form)
    lbl_item.config(text="Item", bg="#f5fffa")
    lbl_item.grid(row=1, column=0, padx=5, pady=15)
        
    txt_item = Entry(order_form)
    txt_item.config(textvariable=var_item)
    txt_item.grid(row=1, column=1, padx=5, pady=5)
    
    lbl_qty = Label(order_form)
    lbl_qty.config(text="Quantity", bg="#f5fffa")
    lbl_qty.grid(row=2, column=0, padx=5, pady=15)   
    
    txt_qty = Entry(order_form)
    txt_qty.config(textvariable=var_qty)
    txt_qty.grid(row=2, column=1, padx=5, pady=5)

    btn_save = Button(order_form)
    btn_save.config(text="Save", command = save_order)
    btn_save.grid(row=3, column=1, padx=5, pady=5)

    var_msg.set("Type the order details and press Save")
    lbl_msg = Label(order_form)
    lbl_msg.config(textvariable=var_msg, bg="#f5fffa", width=40)
    lbl_msg.grid(row=4, column=1, padx=10) 

    # main loop
    order_form.mainloop()
    

if __name__ == "__main__":
    display_order_form()
