from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
import pymysql as pm
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from PIL import ImageTk,Image
import matplotlib.pyplot as plt

if __name__ == '__main__':
    mydb = pm.connect(host="localhost",  # setting up connection
                      user="root",
                      passwd="root",
                      database="practice")
    print("Connection is successful")
    cur = mydb.cursor()
    try:
        def createTables():
            sql1 = '''CREATE TABLE CUSTOMER(
                    CUST_ID CHAR(4) PRIMARY KEY,
                    EMAIL_ID VARCHAR(50) NOT NULL ,
                    FIRST_NAME VARCHAR(20) NOT NULL,
                    LAST_NAME VARCHAR(20) NOT NULL,
                    C_PASSWORD VARCHAR(30) NOT NULL,
                    CHECK (EMAIL_ID LIKE '%@%.%'),
                    CHECK (LENGTH(C_PASSWORD)>1 ),
                    CHECK (CUST_ID LIKE 'C%'));'''
            cur.execute(sql1)

            sql2 = ''' CREATE TABLE SUPPLIER(
                    SUPP_ID CHAR(4) PRIMARY KEY,
                    EMAIL_ID VARCHAR(50) NOT NULL,
                    COMPANY_NAME VARCHAR(50) NOT NULL,
                    CHECK (SUPP_ID LIKE 'S%'),
                    CHECK (EMAIL_ID LIKE '%@%.%'));'''
            cur.execute(sql2)

            sql3 = ''' '''
            mydb.commit()
        createTables()
    except:
        print("TABLES ALREADY EXIST!")
    finally:
        print("Hello World!")
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


        def raise_frame(frame):
            frame.tkraise()

        def counter_label(label):  # for counter on the main page
            counter = 0

            def count():
                global counter
                counter += 1
                label.config(text=str(counter))
                label.after(1000, count)
                if counter == 20:
                    master.destroy()

            count()


        label = Label(master, fg="dark green", bg="white", width=20)
        label.place(x=1040, y=190)
        counter_label(label)
        def f1():
            master_new = Tk()

            frames = {}
            frame3 = Frame(master_new,bg = "#FFDCE7")
            def f3():
                frame3.pack(side = "top", fill = "both")
                frame1.forget()

            frame4 = Frame(master_new,bg = "#FFDCE7")
            def f4():
                frame4.pack(side = "top", fill = "both")
                frame1.forget()

            frame5 = Frame(master_new,bg = "#FFDCE7")
            def f5():
                frame5.pack(side = "top", fill = "both")
                frame1.forget()

            master_new.geometry("1280x860")
            master_new.config(background="#FFDCE7")
            frame1 = Frame(master_new,bg = "#FFDCE7")
            frame1.place(x = 0, y = 118)
            heading_1 = Label(master_new, text="Welcome to Amazon :)", height=2, bg="#B7E9F7",
                              font=("Ink Free", 32), borderwidth=5, relief="raised")
            heading_1.pack(side="top", fill="x")
            frame1.pack(side = "top", fill = "both")
            img = ImageTk.PhotoImage(Image.open('download.png'), master = frame1)
            canvas = Canvas(frame1, width=300, height=300)
            canvas.create_image(150, 150, image=img)
            canvas.pack(side = "left", pady=200)
            heading3 = Button(frame1, text="CUSTOMER LOGIN", bg="IndianRed1", height=3, width=20, font=("Arial", 18),
                              command=f3)
            heading3.place(x=490, y=200)
            heading8 = Button(frame1, text="EMPLOYEE LOGIN", bg="IndianRed1", height=3, width=20, font=("Arial", 18),
                              command=f4)
            heading8.place(x=490, y=350)
            img1 = ImageTk.PhotoImage(Image.open('cust.png'), master = frame1)
            canvas1 = Canvas(frame1, width=200, height=200)
            canvas1.create_image(100, 100, image=img1)
            canvas1.place(x = 850, y = 100)

            img2 = ImageTk.PhotoImage(Image.open('emp.png'), master = frame1)
            canvas2 = Canvas(frame1, width=200, height=200)
            canvas2.create_image(100, 100, image=img2)
            canvas2.place(x = 850, y = 350)
            heading_2 = Label(frame1, text="For new customers, sign up below!", height=2,
                              bg="#FFDCE7", font=("Arial", 14))
            heading_2.place(x=750, y=550)
            button_5 = Button(frame1, text="SIGN UP!", height=2, width=10, bg="light blue", command=f5)
            button_5.place(x=800, y= 600)

            def f2():
                frame2.pack(side = "top", fill = "both")
                frame1.forget()
            button_1 = Button(frame1, text="Click Me! f1", height=2, width=10, bg="light blue", command=f2)
            button_1.place(x=600, y=450)
            button_1.pack()

            frames["intro"] = frame1
            frame2 = Frame(master_new,bg = "#FFDCE7")
            heading_2 = Label(frame2, text="CSE-202 | DataBase Management Systems, Winter-2022", height=2, bg="#B7E9F7",
                              font=("Ink Free", 32), borderwidth=5, relief="raised")
            def f3():
                frame1.pack(side = "top", fill = "both")
                frame2.forget()
            heading_2.pack(side="top", fill="x")
            frame2.place(x = 0, y = 118)
            button_2 = Button(frame2, text="Click Me! f2", height=2, width=10, bg="light blue", command=f3)
            button_2.place(x=600, y=450)
            button_2.pack()
            frame2.pack(side="top", fill="both")
            frame2.forget()
            frames["next"] = frame2
            master_new.mainloop()
        button_1 = Button(master, text="Click Me!", height = 2,width = 10,bg="light blue", command=f1)
        button_1.place(x=600, y=450)
        # heading_3 = Label(master, text = "click the button below!", height = 2,bg="#FFDCE7", font = ("Helvetica Bold 16",28))
        # heading_3.place(x = 500, y = 420)
        master.mainloop()


