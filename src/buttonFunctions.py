import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from src.store_pass import storepass

def storeButton(app, current_frame):
    current_frame.destroy()
    app.title("Store a Password")


    store_frame = tk.Frame(app, bg="#f0f0f0", padx=20, pady=20)
    store_frame.pack(expand=True, fill="both")

 
    tk.Label(store_frame, text="Website:", font=("Arial", 14)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
    website_entry = tk.Entry(store_frame, font=("Arial", 14))
    website_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

    tk.Label(store_frame, text="Password:", font=("Arial", 14)).grid(row=1, column=0, sticky="w", padx=5, pady=5)
    password_entry = tk.Entry(store_frame, font=("Arial", 14))
    password_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)


    store_frame.columnconfigure(1, weight=1)

    tk.Button(store_frame, text="Save Password", font=("Arial", 12),
              command=lambda: storePass(website_entry.get(), password_entry.get())).grid(row=2, column=0, columnspan=2, pady=15)


    tk.Button(store_frame, text="Back", font=("Arial", 12),
              command=lambda: startScreen(app, store_frame)).grid(row=3, column=0, columnspan=2, pady=10)


def storePass(website, password):
    if storepass(website, password):
        messagebox.showinfo("Success", "Successfully stored password!")
    else:
        messagebox.showwarning("Error", "Please enter both website and password.")

def allPassButton(app):
    pass

def genPass(app):
    pass

def deletePass(app):
    pass


def startScreen(app, current_frame):
    current_frame.destroy()
    app.title("Password Manager")
    app.state('zoomed')
    app.iconphoto(False, ttk.PhotoImage(file=r'C:\Users\riley\Desktop\Python project\images\icon.png'))


    frame = ttk.Frame(app, padding=30)
    frame.pack(expand=True)


    storeBtn = ttk.Button(frame, text="Store a New Password", bootstyle=SUCCESS, command=lambda:storeButton(app, frame))
    allPassBtn = ttk.Button(frame, text="Display All Passwords", bootstyle=INFO, command=lambda:allPassButton(app))
    genPassBtn = ttk.Button(frame, text="Generate New Password", bootstyle=WARNING, command=lambda:genPass(app))
    deletePassBtn = ttk.Button(frame, text="Delete Saved Password", bootstyle=DANGER, command=lambda:deletePass(app))
    exitBtn = ttk.Button(frame, text="Exit", bootstyle=SECONDARY, command=app.destroy)


    for btn in [storeBtn, allPassBtn, genPassBtn, deletePassBtn, exitBtn]:
        btn.pack(fill='x', pady=10, ipady=10)
