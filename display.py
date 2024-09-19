import tkinter as tk
import sqlite3
import subprocess
from u import *
from tkinter import messagebox
# Establish a connection to the database
conn = sqlite3.connect('users.db')
cur = conn.cursor()

# Retrieve user information from the database
cur.execute('SELECT name FROM users WHERE username = ?', (username,))
name = cur.fetchone()

cur.execute('SELECT dob FROM users WHERE username = ?', (username,))
dob = cur.fetchone()

cur.execute('SELECT address FROM users WHERE username = ?', (username,))
addr = cur.fetchone()

cur.execute('SELECT phone FROM users WHERE username = ?', (username,))
phon = cur.fetchone()

cur.execute('SELECT email FROM users WHERE username = ?', (username,))
email = cur.fetchone()

cur.execute('SELECT accno FROM users WHERE username = ?', (username,))
accno = cur.fetchone()

cur.execute('SELECT amount FROM users WHERE username = ?', (username,))
amou = cur.fetchone()

def dep():
    amt=int(deposit_entry.get())
    my_tuple = (amou) 
    amoun = int(my_tuple[0])
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    update_query = "UPDATE users SET amount = ? WHERE username = ?"
    new_value1 = amt+amoun
    condition_value = username
    cursor.execute(update_query, (new_value1, condition_value))
    messagebox.showinfo("Success", "Deposited Successfully!")
    conn.commit()
    conn.close()

def witd():
    amt=int(withd_entry.get())
    my_tuple = (amou) 
    amoun = int(my_tuple[0])
    if amt < amoun:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        update_query = "UPDATE users SET amount = ? WHERE username = ?"
        new_value1 = amoun-amt
        condition_value = username
        cursor.execute(update_query, (new_value1, condition_value))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Withdrawal Successfully!")
    else:
        messagebox.showerror("OOps", "insufficient amount")

def register():
    root.destroy()
    subprocess.run(['python', 'reg.py'])

def login():
    root.destroy()
    subprocess.run(['python', 'login.py'])

def home():
    root.destroy()
    subprocess.run(['python', 'home.py'])

def refresh():
    root.destroy()
    subprocess.run(['python', 'display.py'])

def trans():
    root.destroy()
    subprocess.run(['python', 'trans.py'])

# Create the main window
root = tk.Tk()
window_width = 600
window_height = 300
root.minsize(window_width, window_height)
root.maxsize(window_width, window_height)
root.title("User data")
root.configure(bg="skyblue")
menubar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Home", command=home)
file_menu.add_command(label="Login", command=login)
file_menu.add_command(label="Registration", command=register)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Transaction Menu
transaction_menu = tk.Menu(menubar, tearoff=0)
transaction_menu.add_command(label=name)
transaction_menu.add_command(label=dob)
transaction_menu.add_command(label=addr)
transaction_menu.add_command(label=email)
transaction_menu.add_command(label=phon)
transaction_menu.add_command(label=username)

# Add both menus to the menubar
menubar.add_cascade(label="Menu", menu=file_menu)
menubar.add_cascade(label="Profile", menu=transaction_menu)

# Set the menubar
root.config(menu=menubar)

name_label = tk.Label(root, text="SBI", bg="skyblue", font=("Helvetica", 24, "bold"))
name_label.grid(row=0, column=0, padx=0, pady=5, sticky=tk.W)
# Name label and entry
ACC_num = tk.Label(root, text="Acc. Number:", bg="skyblue")
ACC_num.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

ACC_number = tk.Label(root,text=accno, width=20, font=("Helvetica", 9, "bold"))
ACC_number.grid(row=1, column=1, padx=10, pady=5)

# Date of Birth label and entry
Branch_label = tk.Label(root, text="Branch:", bg="skyblue")
Branch_label.grid(row=1, column=2, padx=40, pady=5, sticky=tk.W)

dob_entry = tk.Label(root, text="Ujire", width=20, font=("Helvetica", 9, "bold"))
dob_entry.grid(row=1, column=3, padx=0, pady=5)

# Address label and entry
name_label = tk.Label(root, text="Name", bg="skyblue")
name_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

name_entry =tk.Label(root,text=name, width=20, font=("Helvetica", 9, "bold"))
name_entry.grid(row=2, column=1, padx=10, pady=5)

# Phone Number label and entry
phone_label = tk.Label(root, text="@username", bg="skyblue")
phone_label.grid(row=2, column=2, padx=40, pady=5, sticky=tk.W)

phone_entry = tk.Label(root,text=username, width=20, font=("Helvetica", 9, "bold"))
phone_entry.grid(row=2, column=3, padx=10, pady=5)

# Email label and entry
email_label =  tk.Button(root, text="Check Balance", width=15,command=refresh )
email_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

email_entry = tk.Label(root,text=amou, width=20)
email_entry.grid(row=3, column=1, padx=10, pady=5)

password_label = tk.Button(root, text="Deposit", width=15, command=dep)
password_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

deposit_entry =  tk.Entry(root,width=24)
deposit_entry.grid(row=4, column=1, padx=10, pady=5)

password_label = tk.Button(root, text="Withdrawal", width=15, command=witd)
password_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)

withd_entry =  tk.Entry(root,width=24)
withd_entry.grid(row=5, column=1, padx=10, pady=5)

password_label = tk.Button(root, text="transfer", width=15, command=trans)
password_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)

root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

root.mainloop()
