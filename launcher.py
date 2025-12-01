import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# --- CONFIGURATION ---
# Updated Credentials for Group 7
VALID_USERNAME = "Group7"
VALID_PASSWORD = "Elmhurst@123"

def login():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == VALID_USERNAME and pwd == VALID_PASSWORD:
        messagebox.showinfo("Login Success", "Authentication Successful!\nLaunching ASL Detector...")
        root.destroy() # Close the login window
        run_app() # Start the camera
    else:
        messagebox.showerror("Login Failed", "Invalid Username or Password")

def run_app():
    # This runs your existing camera script
    print("Starting Camera...")
    subprocess.run([sys.executable, "realtime_test.py"])

# --- GUI SETUP ---
root = tk.Tk()
root.title("ASL Security System - Login")
root.geometry("400x300")
root.configure(bg="#2C3E50") 

# Title
lbl_title = tk.Label(root, text="Secure ASL System", font=("Arial", 18, "bold"), bg="#2C3E50", fg="white")
lbl_title.pack(pady=20)

# Username
lbl_user = tk.Label(root, text="Username:", font=("Arial", 12), bg="#2C3E50", fg="white")
lbl_user.pack()
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack(pady=5)

# Password
lbl_pwd = tk.Label(root, text="Password:", font=("Arial", 12), bg="#2C3E50", fg="white")
lbl_pwd.pack()
password_entry = tk.Entry(root, font=("Arial", 12), show="*") 
password_entry.pack(pady=5)

# Login Button
btn_login = tk.Button(root, text="LOGIN", font=("Arial", 12, "bold"), bg="#27AE60", fg="white", width=15, command=login)
btn_login.pack(pady=20)

# Footer
lbl_footer = tk.Label(root, text="Authorized Personnel Only", font=("Arial", 8), bg="#2C3E50", fg="#BDC3C7")
lbl_footer.pack(side="bottom", pady=10)

root.mainloop()