import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
from datetime import datetime


# Function to calculate GST amount and total amount
def calculate_gst(amount, gst_rate, qty):
    gst_amount = (amount + (amount * gst_rate / 100))*qty
    total_amount = gst_amount
    return total_amount

# Function to generate the bill
def generate_bill():
    if customer_name_entry.get()=="" or customer_name_entry.get()=="":
        messagebox.showerror("Error","Customer details are must")
    elif not(phone_number_entry.get().isnumeric()) or len(phone_number_entry.get())!=10:
        messagebox.showerror("Invalid Details","Enter a Valid Phone Number")
    else:
        customer_name = customer_name_entry.get() # Get customer name from the entry field
        phone_number = phone_number_entry.get() # Get phone number from the entry field

        items = [] # List to store item details
        total_amount = 0 # Variable to keep track of the total amount

        # Loop through all item entry fields
        for i in range(len(item_entries)):
            item = item_entries[i].get() # Get the item name from the entry field
            price = float(price_entries[i].get()) # Get the item price from the entry field

            gst_rate = float(gst_entries[i].get()) # Get the item GST rate from the entry field
            qty = int(qty_entries[i].get()) #Get the item Qty from the entry field

            items.append((item, price, gst_rate, qty)) # Append item details to the list

        # Generate unique bill number using current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        bill_number = f"{timestamp}"

        # Create bill directory if it doesn't exist
        if not os.path.exists("savbills"):
            os.makedirs("savbills")

        # Create bill file path
        bill_file_path = f"savbills/{bill_number}.txt"

        # Create bill content
        bill_content = f"""                           Welcome to ThakurJi Shop 

Customer Name: {customer_name}
Phone Number: {phone_number}
Bill Number: {bill_number}

==============================================================================
Item	        Price	        Qty	        GST	                 Total
=============================================================================="""

        # Loop to calculate total amount for each item and add to the bill content
        i=0
        for item, price, gst_rate, qty in items:
            i+=1
            item_total = calculate_gst(price, gst_rate, qty) # Calculate the total amount for the item
            total_amount += item_total # Update the total amount
            
            bill_content += f"{i}. {item}         {price}            {qty}            {gst_rate}%            {item_total}\n\n" # Add item details and total amount to the bill content
            temp_i_detail=f"{i}. {item}         {price}            {qty}            {gst_rate}%            {item_total}\n\n"
            
                              
        bill_content += "------------------------------------------------------------------------------\n"
        bill_content += f"TOTAL AMOUNT:\t\t\t\t{total_amount}\n" # Add the final total amount of the bill to the bill content
        bill_content += "------------------------------------------------------------------------------\n"

        # Save the bill to a file
        with open(bill_file_path, "w") as file:
            file.write(bill_content)

        # Clear the output text widget
        output_text.delete(1.0, tk.END)

        # Display the bill content in the output text widget
        output_text.insert(tk.END, bill_content)

        # Display success message
        output_text.insert(tk.END, f"\nBill saved successfully as {bill_number}.txt")

def welcome_bill():
    output_text.delete('1.0',END)
    output_text.insert(END,"""                           Welcome to ThakurJi Shop 

Customer Name: 
Phone Number:
Bill Number: 

==============================================================================
Item	        Price	        Qty	        GST	                 Total
==============================================================================""")

# Function to search for a bill
def search_bill():
    search_bill_number = search_entry.get() # Get the bill number to search

    # Clear the output text widget
    output_text.delete(1.0, tk.END)

    # Search for the bill file

    file_path = f"savbills\{search_bill_number}.txt"  # Create the full file path

    if os.path.exists(file_path):
         # Read and display the bill content
        with open(file_path, "r") as bill_file:
            bill_content = bill_file.read()
            output_text.insert(tk.END, bill_content)
        return
    else:
        print(f"The file {search_bill_number} does not exist in the folder.")


    # Display error message if bill is not found
    messagebox.showinfo("TryAgain", "Bill Not Found!!")
    output_text.insert(tk.END, "Bill not found.")


# Create the main window
window = tk.Tk()
window.geometry("1920x1080+0+0")
window.title("Prashant Biling Software")
window.iconbitmap("favicon.ico")
title = tk.Label(window,text = "Biling System", bd=5,relief=GROOVE,bg="#EDEADE",fg="black",font = ("Baloo Bhai",30,"bold"),pady=0).pack(fill=X)

# Create a frame for customer details
customer_frame = LabelFrame(window,text="Customer details:",bd=5,fg="green",font=("Times New Roman",12,"bold"))
customer_frame.pack()

# Create labels and entry fields for customer details
customer_name_label = tk.Label(customer_frame, text="Customer Name:", bd=5,relief=GROOVE,bg="#1A8A70",fg="white",pady=10,font=("Times New Roman",15,"bold"))
customer_name_label.pack(side= "left")
customer_name_entry = tk.Entry(customer_frame,width=25,bd=5,relief=SUNKEN)
customer_name_entry.pack(side="left")

phone_number_label = tk.Label(customer_frame, text="Phone Number:", bd=5,relief=GROOVE,bg="#1A8A70",fg="white",pady=10,font=("Times New Roman",15,"bold"))
phone_number_label.pack(side="left")
phone_number_entry = tk.Entry(customer_frame,width=25,bd=5,relief=SUNKEN)
phone_number_entry.pack(side="right")


##
###Scroll Ybarr
##
##scrol_y=Scrollbar(item_frame,orient=VERTICAL)
##output_text=Text(item_frame,yscrollcommand=scrol_y.set)
##scrol_y.pack(side=RIGHT,fill=Y)
##scrol_y.config(command=output_text.yview)
##output_text.pack(fill=BOTH,expand=1)

item_entries = []
price_entries = []
gst_entries = []
qty_entries = []

i=0
def add_item():
    global i
    #To Check if Item Entries     
##    if i!=0:
##        if item_entry.get()=="" or price_entry.get()=="" or qty_entry.get()=="" or gst_entry.get()=="":
##            messagebox.showerror("Error","Customer details are must")
    i=i+1
    
    # Create a frame for item details
    item_frame = LabelFrame(window,bd=8,text=F"   ITEM DETAILS:{i}   ",relief=GROOVE,font=("baloo bhai",15,"bold"),fg="red",)
    item_frame.place(x=780,y=135+25)
    # Create labels and entry fields for item details
    item_label = tk.Label(item_frame,fg="black", text=f"ITEM NAME:",font = ("Baloo bhai",12,"bold"))
    item_label.pack()

    item_entry = tk.Entry(item_frame)
    item_entry.pack()
    item_entries.append(item_entry)

    price_label = tk.Label(item_frame, fg="black",text="Item Price:",font = ("Baloo bhai",12,"bold"))
    price_label.pack()

    price_entry = tk.Entry(item_frame)
    price_entry.pack()
    price_entries.append(price_entry)

    item_label = tk.Label(item_frame,fg="black", text="Quantity:",font = ("Baloo bhai",12,"bold"))
    item_label.pack()

    qty_entry = tk.Entry(item_frame)
    qty_entry.pack()
    qty_entries.append(qty_entry)

    gst_label = tk.Label(item_frame,fg="black", text="Item GST Rate (%):",font = ("Baloo bhai",12,"bold"))
    gst_label.pack()

    gst_entry = tk.Entry(item_frame)
    gst_entry.pack()
    gst_entries.append(gst_entry)
    
    if i!=1:
        if (customer_name_entry.get()=="" or phone_number_entry.get()==""):
            messagebox.showerror("Don't Forget","Customer details are must")
        elif not(phone_number_entry.get().isnumeric()) or len(phone_number_entry.get())!=10:
            messagebox.showerror("Invalid Details","Enter a Valid Phone Number")
        

# Create an initial set of entry fields
add_item()






# Create a button to add more items
add_item_button = tk.Button(window, text="Add Item",bd=5,fg="green",command=add_item)
add_item_button.place(x=865-20,y=385+25)


# Create a button to generate the bill
generate_button = tk.Button(window, text="GenerateBill", bg="cadetblue",fg="white",bd=4,pady=0,width=12,font=("baloo bhai",10,"bold"),command=generate_bill)
generate_button.place(x=845-20,y=425+25)

# Create a label and entry field for searching bill
search_label = tk.Label(window, text="Search Bill",fg="black",font=("baloo bhai",13,"bold"))
search_label.place(x=1136,y=200)

search_entry = tk.Entry(window,width=25,bd=5,relief=SUNKEN)
search_entry.place(x=1110,y=225)

# Create a button to search for a bill
search_button = tk.Button(window, text="Search", command=search_bill,width=5,bd=3,font=("arial 15 bold"))
search_button.place(x=1115+36,y=255)

### Create an output text widget to display the bill
##output_text = tk.Text(window, height=20, width=70)
##output_text.pack()


#====Bill Area======
F5 = Frame(window,bd=10,relief=GROOVE)
F5.place(x=648,y=500,width=665,height=420)
bill_title=Label(F5,text="Bill Area",font=("baloo bhai",16,"bold"),bd=7,relief=GROOVE).pack(fill=X)
scrol_y=Scrollbar(F5,orient=VERTICAL)
output_text=Text(F5,yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=output_text.yview)
output_text.pack(fill=BOTH,expand=1)
welcome_bill()







# Start the main loop
window.mainloop()
