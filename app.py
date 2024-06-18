import tkinter as tk
from tkinter import ttk

# Function to add user to the listbox
def add_user():
    name = name_entry.get()
    email = email_entry.get()
    if name and email:
        user_list.insert(tk.END, f"Name: {name}, Email: {email}")
        name_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
    else:
        status_label.config(text="Please enter both name and email")

# Function to clear the status message
def clear_status(event):
    status_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("User Information")

# Create and place the labels, entries, and buttons
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Email:").grid(row=1, column=0, padx=10, pady=10)

name_entry = tk.Entry(root)
email_entry = tk.Entry(root)

name_entry.grid(row=0, column=1, padx=10, pady=10)
email_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, text="Add User", command=add_user)
add_button.grid(row=2, columnspan=2, pady=10)

# Status label to show messages
status_label = tk.Label(root, text="", fg="red")
status_label.grid(row=3, columnspan=2)

# Listbox to display users
user_list = tk.Listbox(root, width=50)
user_list.grid(row=4, columnspan=2, padx=10, pady=10)

# Bind the entries to clear status message on focus
name_entry.bind("<FocusIn>", clear_status)
email_entry.bind("<FocusIn>", clear_status)

# Run the application
root.mainloop()
