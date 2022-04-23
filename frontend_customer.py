from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql as pm
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import ImageTk,Image
import matplotlib.pyplot as plt

master = Tk()
master.geometry("1280x860")
master.config(background="#FFDCE7")
heading_1 = Label(master, text="CSE-202 | DataBase Management Systems, Winter-2022", height=2, bg="#B7E9F7",
                font=("Ink Free", 32), borderwidth=5, relief="raised")
heading_1.pack(side="top", fill="x")

heading_2 = Label(master, text = "To view the full application,click the button below!", height = 2, bg="#FFDCE7", font = ("Helvetica Bold 16",28))
heading_2.place(x = 250, y = 350)
counter = 0

label_2 = Label(master, bg="yellow", height=6, width=30, relief="raised")
label_2.place(x=1000, y=150)

def get_frame(master):
    frame3 = Frame(master,bg = "#FFDCE7")
    heading2 = Label(frame3, bg="deep sky blue", height=30, width=100, relief="raised", borderwidth=3)
    heading2.config(highlightbackground="purple", highlightthickness=2)
    heading2.pack(padx=250, pady=150)
    heading3 = Label(frame3, text="Email Address", bg="IndianRed1", height=3, width=12, font=("Arial", 18))
    heading3.place(x=380, y=200)

    heading5 = Label(frame3, bg="IndianRed1", height=5, width=30, relief="groove")
    heading5.place(x=600, y=200)

    heading8 = Label(frame3, text="Password", bg="IndianRed1", height=3, width=12, font=("Arial", 18))
    heading8.place(x=380, y=350)

    heading5 = Label(frame3, bg="IndianRed1", height=5, width=30, relief="groove")
    heading5.place(x=600, y=350)

    heading4 = Entry(frame3, textvariable=2, width=30)
    heading4.place(x=620, y=230)

    heading6 = Entry(frame3, textvariable=1, width=30, show="*")
    heading6.place(x=620, y=380)
    return frame3

# get_frame(master)
master.mainloop()