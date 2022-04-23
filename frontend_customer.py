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


if __name__ == '__main__':
    master_new = Tk()
    master = Tk()
    master.geometry("1280x860")
    master.config(background="#FFDCE7")
    heading_1 = Label(master, text="CSE-202 | DataBase Management Systems, Winter-2022", height=2, bg="#B7E9F7",
                    font=("Ink Free", 32), borderwidth=5, relief="raised")
    heading_1.pack(side="top", fill="x")

    heading_2 = Label(master, text = "Customer", height = 2, bg="#FFDCE7", font = ("Helvetica Bold 16",28))
    heading_2.place(x=0,y=100)
    button = Button(master, text="logout", bg="deep sky blue", fg="white", font=("Arial", 16), command=master.destroy)
    #
    # label_2 = Label(master, bg="yellow", height=6, width=30, relief="raised")
    # label_2.place(x=1000, y=150)
    get_frame_customer(master).pack(side = "top", fill = "x",pady=100)
    master.mainloop()

# def start_gui():
#     main_window = MainWindow()
#
#     main_window.set_grid(20,3)
#     main_window.root.mainloop()
#
# class MainWindow:
#     def __init__(self, root = tk.Tk()):
#         self.root = root
#         self.root.title('Some Table')
#
#         self.frame = tk.Frame(root, width=100, height=100)
#         self.frame.grid(row = 0, column = 0)
#
#         self.canvas = tk.Canvas(self.frame, width = 100, height = 100)
#         self.canvas.configure(scrollregion=(0, 0, 100, 1000))
#         self.canvas.grid(row = 0, column = 0)
#
#         self.vbar = tk.Scrollbar(self.frame, orient = 'vertical', command= self.canvas.yview)
#         self.vbar.grid(row = 0, column = 1, sticky = 'ns')
#
#         self.canvas.config(yscrollcommand = self.vbar.set)
#         labelheading = tk.Label(self.canvas, text = 'Products', bg = 'yellow', height = 6, width = 30, relief = 'raised')
#         labelheading.grid(row = 0, column = 0)
#
#         labelcart = tk.Label(self.canvas, text='cart', bg='yellow', height=6, width=30, relief='raised')
#         labelcart.grid(row=0, column=1)
#
#         labelprofile = tk.Label(self.canvas, text='cart', bg='yellow', height=6, width=30, relief='raised')
#         labelprofile.grid(row=0, column=1)
#
#
#     def set_grid(self, rows, columns):
#         for i in range(rows):
#             for j in range(columns):
#                 label = tk.Label(self.canvas, text = 'some label', relief = 'solid', width = 20)
#                 label.grid(row = i+1, column = j)
