import sqlite3
import random
import tkinter as tk
from tkinter import messagebox
import subprocess
from tkcalendar import DateEntry

def create_database():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 name TEXT, dob TEXT, address TEXT, phone TEXT, 
                 email TEXT, username TEXT, password TEXT, accno TEXT, amount FLOAT)''')
    conn.commit()
    conn.close()

def ACC():
    return ''.join(random.choices('0123456789', k=3))

def Accno():

    last_name = ACC()
    acnumber = f"SBI00{last_name}"
    return acnumber

def register_user():
    # Get values from entry fields
    name = name_entry.get()
    dob = dob_entry.get()
    address = address_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    accno = Accno()
    amount = 0
    # Check if passwords match
    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match.")
        return
        # Check if any field is empty
    if not username or not password or not email or not phone:
        messagebox.showerror("Error", "All fields are required")
        return

    # Check username length
    if len(username) < 3 or len(username) > 16:
        messagebox.showerror("Error", "Username must be between 3 and 16 characters")
        return

    # Check password length and complexity
    if len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long")
        return
    if not any(char.isupper() for char in password):
        messagebox.showerror("Error", "Password must contain at least one uppercase letter")
        return
    if not any(char.islower() for char in password):
        messagebox.showerror("Error", "Password must contain at least one lowercase letter")
        return
    if not any(char.isdigit() for char in password):
        messagebox.showerror("Error", "Password must contain at least one digit")
        return

    # Check email format
    if "@" not in email or "." not in email:
        messagebox.showerror("Error", "Invalid email format")
        return

    # Check phone number format
    if not phone.isdigit() or len(phone) != 10:
        messagebox.showerror("Error", "Phone number must be 10 digits long")
        return

    messagebox.showinfo("Success", "Registration successful for user: {}".format(username))
    
    # Save registration details to the database
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''INSERT INTO users (name, dob, address, phone, email, username, password,accno,amount) 
                 VALUES (?, ?, ?, ?, ?, ?, ?,?,?)''', (name, dob, address, phone, email, username, password,accno,amount))
    conn.commit()
    conn.close()
    save_username_to_file(username)
    succ()

def save_username_to_file(data):
    with open('u.py', 'w') as f:
        f.write('username='+"'" + data + "'")
# Function to navigate back to the previous page
def back():
    root.destroy()
    subprocess.run(['python', 'home.py'])

def succ():
    root.destroy()
    subprocess.run(['python', 'home.py'])

def next():
    root.destroy()
    subprocess.run(['python', 'login.py'])

def register():
    root.destroy()
    subprocess.run(['python', 'reg.py'])

def login():
    root.destroy()
    subprocess.run(['python', 'login.py'])

def home():
    root.destroy()
    subprocess.run(['python', 'home.py'])

root = tk.Tk()
window_width = 600
window_height = 300

root.minsize(window_width, window_height)
root.maxsize(window_width, window_height)
root.title("Registration Page")
root.configure(bg="skyblue")

# Create SQLite database
create_database()

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Home", command=home)
file_menu.add_command(label="Login", command=login)
file_menu.add_command(label="Registration", command=register)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Menu", menu=file_menu)

root.config(menu=menubar)

# Rest of your GUI code...
name_label = tk.Label(root, text="Name:", bg="skyblue")
name_label.grid(row=0, column=0, padx=100, pady=5, sticky=tk.W)

name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=0, pady=5)

# Date of Birth label and entry
def get_date():
    selected_date = dob_entry.get_date()
    print(selected_date)

# Date of Birth entry using tkcalendar DateEntry widget
dob_entry = DateEntry(root, width=12, background='darkblue',foreground='white', borderwidth=2)
dob_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

dob_label = tk.Label(root, text="Date of Birth (DD/MM/YYYY):", bg="skyblue")
dob_label.grid(row=1, column=0, padx=100, pady=5, sticky=tk.W)

'''dob_entry = tk.Entry(root, width=30)
dob_entry.grid(row=1, column=1, padx=0, pady=5)'''

# Address label and entry
address_label = tk.Label(root, text="Address:", bg="skyblue")
address_label.grid(row=2, column=0, padx=100, pady=5, sticky=tk.W)

address_entry = tk.Entry(root, width=30)
address_entry.grid(row=2, column=1, padx=0, pady=5)

# Phone Number label and entry
phone_label = tk.Label(root, text="Phone Number:", bg="skyblue")
phone_label.grid(row=3, column=0, padx=100, pady=5, sticky=tk.W)

phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=3, column=1, padx=0, pady=5)

# Email label and entry
email_label = tk.Label(root, text="Email:", bg="skyblue")
email_label.grid(row=4, column=0, padx=100, pady=5, sticky=tk.W)

email_entry = tk.Entry(root, width=30)
email_entry.grid(row=4, column=1, padx=0, pady=5)

# Username label and entry
username_label = tk.Label(root, text="Username:", bg="skyblue")
username_label.grid(row=5, column=0, padx=100, pady=5, sticky=tk.W)

username_entry = tk.Entry(root, width=30)
username_entry.grid(row=5, column=1, padx=0, pady=5)

# Password label and entry
password_label = tk.Label(root, text="Password:", bg="skyblue")
password_label.grid(row=6, column=0, padx=100, pady=5, sticky=tk.W)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=6, column=1, padx=0, pady=5)

# Confirm password label and entry
confirm_password_label = tk.Label(root, text="Confirm Password:", bg="skyblue")
confirm_password_label.grid(row=7, column=0, padx=100, pady=5, sticky=tk.W)

confirm_password_entry = tk.Entry(root, show="*", width=30)
confirm_password_entry.grid(row=7, column=1, padx=0, pady=5)

# Register button
register_button = tk.Button(root, text="Register", command=register_user)
register_button.grid(row=8, column=1, padx=10, pady=5)


# Run the main event loop


root.mainloop()
