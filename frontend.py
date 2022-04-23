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
                      database="retailstore")
    print("Connection is successful")
    cur = mydb.cursor()
    try:
        def createTables():
            sql3 = '''CREATE TABLE ADMINISTRATOR(
                    ADMIN_ID CHAR(4) PRIMARY KEY,
                    FIRST_NAME VARCHAR(30) NOT NULL,
                    LAST_NAME VARCHAR(30) NOT NULL,
                    EMAIL_ID VARCHAR(50) NOT NULL,
                    A_PASSWORD VARCHAR(30) NOT NULL,
                    CHECK (ADMIN_ID LIKE 'A%'),
                    CHECK (LENGTH(A_PASSWORD)>1 )); '''
            cur.execute(sql3)
            mydb.commit()
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
                if counter == 5:
                    master.iconify()

            count()


        label = Label(master, fg="dark green", bg="white", width=20)
        label.place(x=1040, y=190)
        counter_label(label)
        def f1():
            master_new = Tk()

            frames = {}
            dict_customers = {}
            dict_employee = {}
            sql1 = '''SELECT EMAIL_ID, C_PASSWORD FROM CUSTOMER;'''
            cur.execute(sql1)
            rows = cur.fetchall()
            for i in rows:
                dict_customers[i[0]] = i[1]
            mydb.commit()
            sql1 = '''SELECT EMAIL_ID, A_PASSWORD FROM ADMINISTRATOR;'''
            cur.execute(sql1)
            rows = cur.fetchall()
            for i in rows:
                dict_employee[i[0]] = i[1]
            mydb.commit()
            frame3 = Frame(master_new,bg = "#FFDCE7")
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
            def back():
                frame1.pack(side = "top", fill = "both")
                frame3.forget()

            def callbac():
                passw = heading6.get()
                user = heading4.get()
                if user in dict_customers.keys() and passw in dict_customers.values() and dict_customers[user]==passw:
                    a = messagebox.askquestion("Success", "Would you like to continue?")
                    if a == "yes":
                        messagebox.showinfo("Success", "You will be directed to the page in a short while")

                    else:
                        heading6.delete(first=0, last=100)
                        heading4.delete(first=0, last=100)
                        back()
                        #('blythe_case7564@aol.net', 'NJJ74DHN7XA'),
                        # ('c.erickson6969@outlook.edu', 'IYL06VQE3DK'),
                        # ('hebertcharity5210@yahoo.in', 'BAY99IMX4JE')
                elif user in dict_customers.keys() and passw not in dict_customers.values():
                    messagebox.askokcancel("Error", "Enter the correct details")
                    heading6.delete(first=0, last=100)
                    heading4.delete(first=0, last=100)
                elif user not in dict_customers.keys() and passw in dict_customers.values():
                    messagebox.askokcancel("Error", "Enter the correct details")
                    heading6.delete(first=0, last=100)
                    heading4.delete(first=0, last=100)
                else:
                    messagebox.askokcancel("Error", "Enter the correct details")
                    heading6.delete(first=0, last=100)
                    heading4.delete(first=0, last=100)

            heading7 = Button(frame3, text="Submit", bg="orange", bd=2, relief="groove", height=2, width=9,
                              font=("Arial", 15), command=callbac)
            heading7.place(x=500, y=500)

            button_10 = Button(frame3, text="Back",bg="orange", bd=2, relief="groove", height=2, width=9,
                              font=("Arial", 15), command=back)
            button_10.place(x=650, y=500)
            frame3.place(x=0, y=118)
            frame3.pack(side="top", fill="both")
            frame3.forget()

            def f3():
                frame3.pack(side = "top", fill = "both")
                frame1.forget()

            frame4 = Frame(master_new,bg = "#FFDCE7")
            heading2 = Label(frame4, bg="deep sky blue", height=30, width=100, relief="raised", borderwidth=3)
            heading2.config(highlightbackground="purple", highlightthickness=2)
            heading2.pack(padx=250, pady=150)
            heading3 = Label(frame4, text="Email Address", bg="IndianRed1", height=3, width=12, font=("Arial", 18))
            heading3.place(x=380, y=200)

            heading5 = Label(frame4, bg="IndianRed1", height=5, width=30, relief="groove")
            heading5.place(x=600, y=200)

            heading8 = Label(frame4, text="Password", bg="IndianRed1", height=3, width=12, font=("Arial", 18))
            heading8.place(x=380, y=350)

            heading5 = Label(frame4, bg="IndianRed1", height=5, width=30, relief="groove")
            heading5.place(x=600, y=350)

            heading4 = Entry(frame4, textvariable=2, width=30)
            heading4.place(x=620, y=230)

            heading6 = Entry(frame4, textvariable=1, width=30, show="*")
            heading6.place(x=620, y=380)
            def back1():
                frame1.pack(side = "top", fill = "both")
                frame4.forget()

            def callbac1():
                passw = heading6.get()
                user = heading4.get()
                if user in dict_employee.keys() and passw in dict_employee.values() and dict_employee[user]==passw:
                    a = messagebox.askquestion("Success", "Would you like to continue?")
                    if a == "yes":
                        messagebox.showinfo("Success", "You will be directed to the page in a short while")

                    else:
                        heading6.delete(first=0, last=100)
                        heading4.delete(first=0, last=100)
                        back()
                        #('blythe_case7564@aol.net', 'NJJ74DHN7XA'),
                        # ('c.erickson6969@outlook.edu', 'IYL06VQE3DK'),
                        # ('hebertcharity5210@yahoo.in', 'BAY99IMX4JE')
                elif user in dict_employee.keys() and passw not in dict_employee.values():
                    messagebox.askokcancel("Error", "Enter the correct details")
                    heading6.delete(first=0, last=100)
                    heading4.delete(first=0, last=100)
                elif user not in dict_employee.keys() and passw in dict_employee.values():
                    messagebox.askokcancel("Error", "Enter the correct details")
                    heading6.delete(first=0, last=100)
                    heading4.delete(first=0, last=100)
                else:
                    messagebox.askokcancel("Error", "Enter the correct details")
                    heading6.delete(first=0, last=100)
                    heading4.delete(first=0, last=100)

            heading7 = Button(frame4, text="Submit", bg="orange", bd=2, relief="groove", height=2, width=9,
                              font=("Arial", 15), command=callbac1)
            heading7.place(x=500, y=500)

            button_10 = Button(frame4, text="Back",bg="orange", bd=2, relief="groove", height=2, width=9,
                              font=("Arial", 15), command=back1)
            button_10.place(x=650, y=500)
            frame4.place(x=0, y=118)
            frame4.pack(side="top", fill="both")
            frame4.forget()
            def f4():
                frame4.pack(side = "top", fill = "both")
                frame1.forget()

            frame5 = Frame(master_new,bg = "#FFDCE7")
            heading2 = Label(frame5, bg="deep sky blue", height=40, width=100, relief="raised", borderwidth=3)
            heading2.config(highlightbackground="purple", highlightthickness=2)
            heading2.pack(padx=50, pady=150)
            heading3 = Label(frame5, text="First Name", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
            heading3.place(x=320, y=180)
            lab1 = Label(frame5, bg="IndianRed1", height=5, width=30, relief="groove")
            lab1.place(x=670, y=180)
            ent1 = Entry(frame5, textvariable=1, width=30)
            ent1.place(x=685, y=210)

            def chk_adm():  # validating admission number
                cur = mydb.cursor()
                sql = "SELECT C_ID from CUSTOMER;"
                cur.execute(sql)
                res = cur.fetchall()
                l = []
                for i in res:
                    l.append(i[0])
                c_id = 'C' + str(int(l[-1][1:]) + 1)
                return c_id

            def chk_fname():  # validating name
                name = str(ent1.get())
                if name.isalpha() == True:
                    messagebox.askokcancel("Success", "Data saved successfully!", parent=frame5)
                elif name.isdigit() == True:
                    messagebox.askokcancel("Error", "Enter correctly!", parent=frame5)
                    ent2.delete(first=0, last=100)
                elif name.isalnum() == True:
                    messagebox.askokcancel("Error", "Enter correctly!", parent=frame5)
                    ent2.delete(first=0, last=100)
            def chk_lname():  # validating name
                name = str(ent2.get())
                if name.isalpha() == True:
                    messagebox.askokcancel("Success", "Data saved successfully!", parent=frame5)
                elif name.isdigit() == True:
                    messagebox.askokcancel("Error", "Enter correctly!", parent=frame5)
                    ent2.delete(first=0, last=100)
                elif name.isalnum() == True:
                    messagebox.askokcancel("Error", "Enter correctly!", parent=frame5)
                    ent2.delete(first=0, last=100)
            but = Button(frame5, text="Save", fg="red", command=chk_fname)
            but.place(x=930, y=210)
            heading5 = Label(frame5, text="Last Name", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
            heading5.place(x=320, y=280)
            lab2 = Label(frame5, bg="IndianRed1", height=5, width=30, relief="groove")
            lab2.place(x=670, y=280)
            ent2 = Entry(frame5, textvariable=2, width=30)
            ent2.place(x=685, y=310)

            but1 = Button(frame5, text="Save", fg="red", command=chk_lname)
            but1.place(x=930, y=310)
            heading8 = Label(frame5, text="Email Address", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
            heading8.place(x=320, y=380)
            lab3 = Label(frame5, bg="IndianRed1", height=5, width=30, relief="groove")
            lab3.place(x=670, y=380)
            ent3 = Entry(frame5, textvariable=3, width=30)
            ent3.place(x=685, y=410)

            def chk_email():  # validating grade
                grad = str(ent3.get())
                if grad.isdigit() == True:
                    if int(grad) > 5 or int(grad) < 1:
                        messagebox.askokcancel("Error", "Enter grade between 1-5", parent=frame5)
                        ent3.delete(first=0, last=100)
                    else:
                        messagebox.askokcancel("Success", "Data saved successfully", parent=frame5)
                elif grad.isalpha() == True:
                    messagebox.askokcancel("Error", "Enter correctly!", parent=frame5)
                    ent3.delete(first=0, last=100)
                elif grad.isalnum() == True:
                    messagebox.askokcancel("Error", "Enter correctly", parent=frame5)
                    ent3.delete(first=0, last=100)

            but2 = Button(frame5, text="Save", fg="red", command=chk_email)
            but2.place(x=930, y=410)
            heading6 = Label(frame5, text="Password", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
            heading6.place(x=320, y=480)
            lab4 = Label(frame5, bg="IndianRed1", height=5, width=30, relief="groove")
            lab4.place(x=670, y=480)
            ent4 = Entry(frame5, textvariable=4, width=30)
            ent4.place(x=685, y=510)

            def chk_dob():  # validating date of birth
                dob = str(ent4.get())
                if len(dob) == 8:
                    if int(dob[0:4]) < 2015 and int(dob[0:4]) > 2010:
                        if dob[4:6] in ["01", "03", "05", "07", "08", "10", "12"] and int(dob[6] + dob[7]) <= 31:
                            messagebox.askokcancel("Success", "Data saved successfully", parent=frame5)
                        elif dob[4:6] in ["04", "06", "09", "11"] and int(dob[6] + dob[7]) <= 30:
                            messagebox.askokcancel("Success", "Data saved successfully", parent=frame5)
                        elif dob[4:6] in ["02"] and int(dob[7] + dob[8]) <= 28:
                            messagebox.askokcancel("Success", "Data saved successfully", parent=frame5)
                        elif int(dob[0:4]) % 4 == 0 and dob[4:6] in ["02"] and int(dob[6] + dob[7]) <= 28:
                            messagebox.askokcancel("Success", "Data saved successfully", parent=frame5)
                    else:
                        messagebox.askokcancel("Error", "Enter correctly!", parent=frame5)
                        ent4.delete(first=0, last=100)
                elif len(dob) != 8:
                    messagebox.askokcancel("Error", "Enter correctly!", parent=frame5)
                    ent4.delete(first=0, last=100)

            but3 = Button(frame5, text="Save", fg="red", command=chk_dob)
            but3.place(x=930, y=510)

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


