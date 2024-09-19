import tkinter as tk
import subprocess
from tkinter import PhotoImage

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
root.title("OTP Verification")

bg_image = tk.PhotoImage(file="bg1.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Home", command=home)
file_menu.add_command(label="Login", command=login)
file_menu.add_command(label="Registration", command=register)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Menu", menu=file_menu)

root.config(menu=menubar)

container_frame = tk.Frame(root, bg="white")
container_frame.pack(pady=20, padx=50, side=tk.RIGHT) 

register_frame = tk.Frame(container_frame, bg="white")
register_frame.pack(pady=10, padx=10, side=tk.TOP)  

register_label = tk.Label(register_frame, text="Register Section", bg="white")
register_label.pack()

register_button = tk.Button(register_frame, text="Register", command=register)
register_button.pack(pady=5)

login_frame = tk.Frame(container_frame, bg="white")
login_frame.pack(pady=30, padx=10, side=tk.TOP)  

login_label = tk.Label(login_frame, text="Login Section", bg="white")
login_label.pack()

login_button = tk.Button(login_frame, text="Login", command=login)
login_button.pack(pady=5)

root.mainloop()
