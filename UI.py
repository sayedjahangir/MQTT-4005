import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import bcrypt

from users_DB import db

# database connection
def get_db_connection():
    conn = sqlite3.connect('users.db')
    return conn

# hash password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# insert new user into the database
def insert_user(username, password_hash):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists.")
        return False
    finally:
        conn.close()

def register():
    username = register_username_entry.get()
    password = register_password_entry.get()
    if username and password:  # simple validation
        password_hash = hash_password(password)
        if insert_user(username, password_hash):
            messagebox.showinfo("Success", "Registration is successful.")
    else:
        messagebox.showerror("Error", "Username and password cannot be empty.")

def show_login_frame():

    register_frame.pack_forget()
    login_frame.pack()
    login_frame.pack(padx=100, pady=100)

def show_register_frame():
    login_frame.pack_forget()
    register_frame.pack()
    register_frame.pack(padx=100, pady=100)

def login():
    # dummy login function
    username = login_username_entry.get()
    password = login_password_entry.get()
    messagebox.showinfo("Login System", f"Username: {username}\nPassword: {password}")

# main window setup
root = tk.Tk()
root.title("Login System")
root.geometry("600x500")

transparent_color = 'systemTransparent'
background_image = tk.PhotoImage(file="sewy.pnj.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# styling format
style = ttk.Style()
style.configure("TLabel", font=("arial", 30))
style.configure("TButton", font=("arial", 30))

# login frame
login_frame = ttk.Frame(root)
login_frame.pack(padx=100, pady=100)

login_username_label = ttk.Label(login_frame, text="Username:", background="")
login_username_label.grid(row=0, column=0, sticky="w")
login_username_entry = ttk.Entry(login_frame)
login_username_entry.grid(row=0, column=1, pady=10)

login_password_label = ttk.Label(login_frame, text="Password:", background="")
login_password_label.grid(row=1, column=0, sticky="w")
login_password_entry = ttk.Entry(login_frame, show="*")
login_password_entry.grid(row=1, column=1, pady=10)

login_button = ttk.Button(login_frame, text="Login", command=login)
login_button.grid(row=2, column=0, columnspan=2, pady=10)

to_register_button = ttk.Button(login_frame, text="Register", command=show_register_frame)
to_register_button.grid(row=3, column=0, columnspan=2)

# registration frame
register_frame = ttk.Frame(root)
register_frame.pack(padx=100, pady=100)
register_username_label = ttk.Label(register_frame, text="Username:")
register_username_label.grid(row=0, column=0, sticky="w")
register_username_entry = ttk.Entry(register_frame)
register_username_entry.grid(row=0, column=1, pady=10)

register_password_label = ttk.Label(register_frame, text="Password:")
register_password_label.grid(row=1, column=0, sticky="w")
register_password_entry = ttk.Entry(register_frame, show="*")
register_password_entry.grid(row=1, column=1, pady=10)

register_button = ttk.Button(register_frame, text="Register", command=register)
register_button.grid(row=2, column=0, columnspan=2, pady=10)

to_login_button = ttk.Button(register_frame, text="Back to Login", command=show_login_frame)
to_login_button.grid(row=3, column=0, columnspan=2)

# this makes it start with the login frame
show_login_frame()
root.mainloop()
