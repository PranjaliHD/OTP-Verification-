import tkinter as tk
import sqlite3
import subprocess
from u import *
from tkinter import messagebox
import smtplib
import random
from passd import *                                                                                                                                                                                                         
import time
import sqlite3

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

cur.execute('SELECT password FROM users WHERE username = ?', (username,))
paswd = cur.fetchone()

def transfer():
    cliacc = ACC_number.get()
    seam = float(amount_entry.get())
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('SELECT amount FROM users WHERE accno = ?', (cliacc,))
    camou = cur.fetchone()
    Mtuple = (camou) 
    cliam = float(Mtuple[0])
    update_query = "UPDATE users SET amount = ? WHERE accno = ?"
    new_value1 = cliam+seam
    condition_value = cliacc
    cur.execute(update_query, (new_value1, condition_value))
    conn.commit()
    conn.close()
    

def witd():
    cliacc = ACC_number.get()
    passs = pas_entry.get()
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE accno = ?', (cliacc,))
    result = cur.fetchone()
    amt=float(amount_entry.get())
    my_tuple = (amou) 
    amoun = float(my_tuple[0])
    if result:
        if amt < amoun:
            if passs == paswd[0]:

                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                update_query = "UPDATE users SET amount = ? WHERE username = ?"
                new_value1 = amoun-amt
                condition_value = username
                cursor.execute(update_query, (new_value1, condition_value))
                conn.commit()
                conn.close()
                transfer()
                messagebox.showinfo("Success", "TRANSFER successfully")
            else:
                messagebox.showerror("OOps", "Invalid Password")
                trans()

        else:
            messagebox.showerror("OOps", "insufficient amount")
            trans()
    else:
        messagebox.showerror("OOps", "Invalid Account Number")
        trans()
    refresh()

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

# Create the menu
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Home", command=home)
file_menu.add_command(label="Login", command=login)
file_menu.add_command(label="Registration", command=register)
file_menu.add_command(label="Dashbord", command=refresh)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Menu", menu=file_menu)
root.config(menu=menubar)

name_label = tk.Label(root, text="SBI", bg="skyblue", font=("Helvetica", 24, "bold"))
name_label.grid(row=0, column=0, padx=0, pady=5, sticky=tk.W)
ACC_num = tk.Label(root, text="Acc. Number:", bg="skyblue",font=("Helvetica", 10, "bold"))
ACC_num.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

ACC_number = tk.Entry(root, width=24)
ACC_number.grid(row=1, column=1, padx=10, pady=5)


name_label = tk.Label(root, text="Amount", bg="skyblue",font=("Helvetica", 10, "bold"))
name_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

amount_entry =tk.Entry(root,width=24)
amount_entry.grid(row=2, column=1, padx=10, pady=5)



otp_label = tk.Label(root, text="Password", bg="skyblue",font=("Helvetica", 10, "bold"))
otp_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

pas_entry = tk.Entry(root,show="*",width=24)
pas_entry.grid(row=3, column=1, padx=10, pady=5)


Deposit_label = tk.Button(root, text="Transfer", width=20, command=witd)
Deposit_label.grid(row=4, column=1,  padx=20, pady=5, sticky=tk.W)



root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

root.mainloop()
