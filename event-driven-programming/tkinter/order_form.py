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
    order_form.config(bg="#f5fffa")
    order_form.option_add("*font", "Verdana 10")

    # frames
    main_frame = Frame(order_form, bg="#f5fffa")
    btn_frame = Frame(order_form, bg="#f5fffa")
    msg_frame = Frame(order_form, bg="#f5fffa")
    main_frame.pack()
    btn_frame.pack()
    msg_frame.pack()

    # variables
    var_customer = StringVar()
    var_item = StringVar()
    var_qty = StringVar()
    var_msg = StringVar()    
    
    # widgets for main_frame
    lbl_customer = Label(main_frame)  # container is main_frame
    lbl_customer.config(text="Customer", bg="#f5fffa")
    lbl_customer.grid(row=0, column=0, padx=5, pady=15)
        
    txt_customer = Entry(main_frame)
    txt_customer.config(textvariable=var_customer)
    txt_customer.grid(row=0, column=1, padx=5, pady=5)
    
    lbl_item = Label(main_frame)
    lbl_item.config(text="Item", bg="#f5fffa")
    lbl_item.grid(row=1, column=0, padx=5, pady=15)
        
    txt_item = Entry(main_frame)
    txt_item.config(textvariable=var_item)
    txt_item.grid(row=1, column=1, padx=5, pady=5)
    
    lbl_qty = Label(main_frame)
    lbl_qty.config(text="Quantity", bg="#f5fffa")
    lbl_qty.grid(row=2, column=0, padx=5, pady=15)   
    
    txt_qty = Entry(main_frame)
    txt_qty.config(textvariable=var_qty)
    txt_qty.grid(row=2, column=1, padx=5, pady=5)

    # widgets for btn_frame

    btn_save = Button(btn_frame)  # container is btn_frame
    btn_save.config(text="Save", command = save_order)
    btn_save.grid(row=0, column=0, padx=5, pady=5)

    btn_clear = Button(btn_frame)
    btn_clear.config(text="Clear", command = clear_form)
    btn_clear.grid(row=0, column=1, padx=5, pady=5)


    # widgets for msg_frame

    var_msg.set("Type the order details and press Save")
    lbl_msg = Label(msg_frame)  # container is msg_frame
    lbl_msg.config(textvariable=var_msg, bg="#f5fffa", width=40)
    lbl_msg.grid(row=0, column=0, padx=10) 

    # main loop
    order_form.mainloop()
    

if __name__ == "__main__":
    display_order_form()
