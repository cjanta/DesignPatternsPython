import tkinter as tk
from ttkbootstrap import Style
from tkinter import messagebox
from ttkbootstrap import ttk

# Function to handle button click event
def on_button_click():
    name = name_entry.get()
    if name:
        messagebox.showinfo("Greetings", f"Hello, {name}!")
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")

# Initialize the main window
root = tk.Tk()
root.title("Simple Tkinter App with Bootstrap")
root.geometry("400x300")

# Apply Bootstrap styling
style = Style(theme='superhero')  # You can choose other themes like 'darkly', 'flatly', etc.

# Create and place the widgets using ttkbootstrap widgets (ttk)
title_label = ttk.Label(root, text="Welcome to the App!", font=("Helvetica", 16))
title_label.pack(pady=20)

name_label = ttk.Label(root, text="Enter your name:")
name_label.pack(pady=5)

name_entry = ttk.Entry(root)
name_entry.pack(pady=5)

greet_button = ttk.Button(root, text="Greet Me", command=on_button_click)
greet_button.pack(pady=20)

# Start the application
root.mainloop()
