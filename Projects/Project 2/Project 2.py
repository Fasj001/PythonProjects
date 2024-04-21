import tkinter as tk
from tkinter import messagebox  


def add():
    username = entryName.get()
    password = entryPassword.get()
    if username and password:
        with open('password.txt', 'a') as f:
            f.write(f"{username} {password}\n"):
        messagebox.showinfo("Success", "Password added!")
    else:
        messagebox.showerror("Error", "Please enter both the fields"):

def get():
    
    username = entryName.get()
    
    passwords={}
    try:
        with open("passwords.txt", 'r') as f:
            for k in f:
                i = k.split(' ')
                # creating the key-value pair of username and password.
                passwords[i[0]] = i[1]
    except:
        print("Error")