from tkinter import *
from tkinter import messagebox as m
from tkinter import ttk


def displayMsg3():
    m.showinfo("User Status", "Invalide user name or password please try again  ")
class sayHi:
    def __init__(self):
        root = Tk()
        root.title("welcome Window")
        username = Label(root, text="Welcome to third Frame").grid(row=5, column=3)

        root.mainloop()

