import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql as pm
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import frontend

# ye pracitce ka h kuch kam ka nhi h
def get_frame_customer(master):
    frame = Frame(master,bg = "#FFDCE7")
    heading2 = Label(frame, bg="deep sky blue", height=30, width=100, relief="raised", borderwidth=3)
    heading2.config(highlightbackground="purple", highlightthickness=2)
    # heading2.pack(padx=250, pady=150)
    heading3 = Label(frame, text="Email Address", bg="IndianRed1", height=3, width=12, font=("Arial", 18))
    heading3.place(x=380, y=200)
    canvas = tk.Canvas(frame, width=1200, height=700)
    canvas.configure(scrollregion=(0, 0, 0, 1000))
    canvas.pack(side="left", fill="both", expand=True)

    vbar = tk.Scrollbar(frame, orient='vertical', command=canvas.yview)
    vbar.pack(side='right', fill='y')

    canvas.config(yscrollcommand=vbar.set)
    return frame
