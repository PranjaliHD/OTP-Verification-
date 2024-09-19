import tkinter as tk
from tkinter import messagebox
import smtplib
import random
from passd import *
import time
import subprocess
import sqlite3


def save_username_to_file(data):
    with open('u.py', 'w') as f:
        f.write('username='+"'" + data + "'")

def generate_otp():
    return ''.join(random.choices('0123456789', k=6))

def send_email(email, otp):
    try:
        sender_email = 'hdpranjali@gmail.com'
        sender_password = password
        subject = 'OTP Verification'
        body = f'Your OTP is: {otp}'
        message = f'Subject: {subject}\n\n{body}'
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email, message)
        server.quit()
        return True
    except Exception as e:
        print("Error:", e)
        return False

def verify_otp():
    global otp_request_time
    entered_otp = otp_entry.get()
    if entered_otp == otp and time.time() - otp_request_time < 60:
        messagebox.showinfo("Success", "OTP Verified Successfully!")
        otp_timer == 0
        login_window.destroy()
        save_username_to_file(username)
        subprocess.run(['python', 'display.py',username])
    else:
        messagebox.showerror("Error", "Invalid OTP")

def request_otp():
    global otp, otp_request_time, username

    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    if result:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute('SELECT email FROM users WHERE username = ?', (username,))
        email = cur.fetchone()
        otp = generate_otp()
        otp_request_time = time.time()
        if send_email(email, otp):
                messagebox.showinfo("Success", "OTP Sent Successfully!")
                start_otp_timer()
                otp_timer_label.configure(state="normal")
                login_button.config(state="normal")
    
        else:
             messagebox.showerror("Error", "Failed to send OTP")
    else:
        messagebox.showerror("Error", "Invalid username or password.")
        
def invalidate_otp():
    global otp
    otp = None
    messagebox.showinfo("Info", "OTP has expired. Please request a new OTP.")

def start_otp_timer():
    global otp_timer
    otp_timer = 60
    update_timer()

def update_timer():
    global otp_timer
    if otp_timer > 0:
        otp_timer_label.config(text=f"Resend in {otp_timer} seconds")
        otp_timer -= 1
        login_window.after(1000, update_timer)
    else:
        otp_resend_btn.config(state="normal")
        otp_timer_label.config(text="")

def register():
    login_window.destroy()
    subprocess.run(['python', 'reg.py'])

def login():
    login_window.destroy()
    subprocess.run(['python', 'login.py'])

def home():
    login_window.destroy()
    subprocess.run(['python', 'home.py'])

def forgot():
    username = entry_username.get()
    save_username_to_file(username)
    login_window.destroy()
    subprocess.run(['python', 'reset.py'])

login_window = tk.Tk()
window_width = 600
window_height = 300

login_window.minsize(window_width, window_height)
login_window.maxsize(window_width, window_height)
login_window.title("Login Page")
login_window.configure(bg="skyblue")


menubar = tk.Menu(login_window)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Home", command=home)
file_menu.add_command(label="Login", command=login)
file_menu.add_command(label="Registration", command=register)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=login_window.quit)
menubar.add_cascade(label="Menu", menu=file_menu)

login_window.config(menu=menubar)

label_username = tk.Label(login_window, text="Username:", bg="skyblue")
label_username.grid(row=0, column=0, padx=100, pady=5, sticky=tk.W)

entry_username = tk.Entry(login_window)
entry_username.grid(row=0, column=1, padx=2, pady=5)

label_password = tk.Label(login_window, text="Password:", bg="skyblue")
label_password.grid(row=1, column=0, padx=100, pady=5, sticky=tk.W)

entry_password = tk.Entry(login_window, show="*")
entry_password.grid(row=1, column=1, padx=2, pady=5)

otp_entry = tk.Label(login_window, text="Enter the OTP:", bg="skyblue")
otp_entry.grid(row=2, column=0, padx=100, pady=5, sticky=tk.W)

otp_entry = tk.Entry(login_window)
otp_entry.grid(row=2, column=1, padx=2, pady=5)

request_button = tk.Button(login_window, text="Request OTP", command=request_otp, highlightthickness=0,width=13)
request_button.grid(row=2, column=2, columnspan=3, pady=0, padx=0)

login_button = tk.Button(login_window, text="Login", command=verify_otp, state="disabled")
login_button.grid(row=3, column=1, padx=10, pady=10)

request_button = tk.Button(login_window, text="Forgot password", command=forgot, highlightthickness=0)
request_button.grid(row=3, column=2, columnspan=3, pady=0, padx=0)

otp_resend_btn = tk.Button(login_window, text="Resend Verification Code", command=request_otp, state="disabled", width=30)
otp_resend_btn.grid(row=4, column=1, columnspan=2, pady=10)

otp_timer_label = tk.Label(login_window, text="",width=30, bg="skyblue")
otp_timer_label.grid(row=5, column=1, columnspan=2, pady=10)

login_window.mainloop()