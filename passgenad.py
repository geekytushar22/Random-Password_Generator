import random
import string
import tkinter as tk
from tkinter import messagebox

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be greater than 0!")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid length!")
        return

    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_symbols = symbols_var.get()

    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "No character set selected!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# GUI Setup
root = tk.Tk()
root.title("Password Generator")

# Input Fields
tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Checkboxes for Character Types
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

# Checkboxes
tk.Checkbutton(root, text="Include Uppercase", variable=upper_var).grid(row=1, column=0)
tk.Checkbutton(root, text="Include Lowercase", variable=lower_var).grid(row=2, column=0)
tk.Checkbutton(root, text="Include Numbers", variable=digits_var).grid(row=3, column=0)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=4, column=0)

# Generate Button
generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2)

# Password Display
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=6, column=0, columnspan=2)

# Run the GUI
root.mainloop()