from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Treeview
import pymysql as pm
import re
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
            print(dict_customers)
            print(dict_employee)


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
            def customer_pages(master1,user,passw):
                frame7 = Frame(master1, bg="#FFDCE7")
                heading2 = Label(frame7, bg="deep sky blue", height=80, width=60, relief="raised", borderwidth=3)
                heading2.config(highlightbackground="purple", highlightthickness=2)
                label_2 = Label(frame7, bg="yellow", height=6, width=30, relief="raised")
                label_2.place(x=1000, y=40)
                label = Label(frame7, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                              font=("Arial", 14))
                label.place(x=1020, y=70)
                heading2.pack(padx=150, pady=170)
                def view_products():
                    frame10 = Frame(master_new, bg="#FFDCE7")
                    heading2 = Label(frame10, bg="deep sky blue", height=60, width=60, relief="raised",
                                     borderwidth=3)
                    heading2.config(highlightbackground="purple", highlightthickness=2)
                    label_2 = Label(frame10, bg="yellow", height=6, width=30, relief="raised")
                    label_2.place(x=1000, y=40)
                    label = Label(frame10, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                  font=("Arial", 14))
                    label.place(x=1020, y=70)
                    heading2.pack(padx=150, pady=170)
                    heading4 = Label(frame10, text="Enter Category ID", bg="IndianRed1", height=3, width=20,
                                     font=("Arial", 18))
                    heading4.place(x=490, y=250)
                    lab1 = Label(frame10, bg="IndianRed1", height=5, width=40, relief="groove")
                    lab1.place(x=490, y=380)
                    ent2 = Entry(frame10, textvariable=2, width=40)
                    ent2.place(x=510, y=410)
                    frame10.pack(side="top", fill="both")
                    frame7.forget()

                    def check_id():
                        id = str(ent2.get())
                        if id[0] != 'C' or id[1] != 'T':
                            messagebox.askokcancel("Error", "Category ID is not Valid!", parent=frame10)
                            ent2.delete(first=0, last=100)
                            ent3.delete(first=0, last=100)
                            return False
                        else:
                            sql1 = '''SELECT * FROM CATEGORY WHERE CATEGORY_ID = (%s)'''
                            cur.execute(sql1, id)
                            rows = cur.fetchall()
                            if len(rows) == 0:
                                ent2.delete(first=0, last=100)
                                messagebox.askokcancel("Error", "Category ID is not valid.")
                            else:
                                ent2.delete(first=0, last=100)
                                try:
                                    sql1 = '''
                                            SELECT PRODUCT_ID,PRODUCT_NAME,PRODUCT_QUANTITY,UNIT_PRICE,DISCOUNT,UNIT_WEIGHT,IN_STOCK, CATEGORY_NAME
                                            FROM CATEGORY C, PRODUCT P WHERE P.CATEGORY_ID = (%s) AND C.CATEGORY_ID = P.CATEGORY_ID
                                            ORDER BY PRODUCT_ID'''
                                    cur.execute(sql1,id)
                                except:
                                    pass
                                frame12 = Frame(master1, bg="#FFDCE7")
                                heading2 = Label(frame12, bg="deep sky blue", height=80, width=240, relief="raised",
                                                 borderwidth=3)
                                heading2.config(highlightbackground="purple", highlightthickness=2)
                                label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                                label_2.place(x=1000, y=40)
                                label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                              font=("Arial", 14))
                                label.place(x=1020, y=70)
                                heading2.pack(padx=150, pady=170)
                                tree = Treeview(frame12, selectmode='browse')
                                tree["columns"] = ("one", "two", "three", "four", "five", "six","seven","eight")
                                tree.column("one", width=140)
                                tree.column("two", width=140)
                                tree.column("three", width=140)
                                tree.column("four", width=140)
                                tree.column("five", width=140)
                                tree.column("six", width=120)
                                tree.column("seven",width = 140)
                                tree.column("eight",width = 140)
                                tree.column("#0", anchor="w", width=0)
                                tree.heading("one", text='Product ID', anchor='w')
                                tree.heading("two", text="Name")
                                tree.heading("three", text="Quantity")
                                tree.heading("four", text="Price")
                                tree.heading("five", text="Discount")
                                tree.heading("six", text="Weight")
                                tree.heading("seven", text="In Stock")
                                tree.heading("eight", text="Category")
                                f = cur.fetchall()
                                for i in f:
                                    tree.insert("", tk.END,
                                                values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
                                tree.place(x=108, y=240)
                                scrollbar = Scrollbar(frame12, orient=tk.VERTICAL, command=tree.yview)
                                tree.configure(yscrollcommand=scrollbar.set)
                                scrollbar.pack(side='right', fill='y')

                                def but_112():
                                    frame10.pack(side="top", fill="both")
                                    frame12.forget()

                                button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2,
                                                   width=9,
                                                   font=("Arial", 14), command=but_112)
                                button_10.place(x=650, y=580)
                                frame12.pack(side="top", fill="both")
                                frame10.forget()

                    head7 = Button(frame10, text="Submit", bg="orange", bd=2, relief="groove", height=2, width=9,
                                   font=("Arial", 15), command=check_id)
                    head7.place(x=500, y=480)

                    def but_10():

                        frame7.pack(side="top", fill="both")
                        frame10.forget()

                    button_10 = Button(frame10, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                       font=("Arial", 14), command=but_10)
                    button_10.place(x=650, y=480)
                    frame10.pack(side="top", fill="both")
                    frame7.forget()
                headingc1 = Button(frame7, text="View Products by Category", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=view_products)
                headingc1.place(x=470, y=210)
                def view_orders():
                    orders = []
                    try:
                        user = "vielkawoodard@icloud.net"
                        sql1 = '''SELECT DISTINCT ORDER_ID,ORDER_TIME FROM PLACES_ORDER, CUSTOMER
                        WHERE PLACES_ORDER.CUST_ID = (SELECT CUST_ID FROM CUSTOMER C1 WHERE C1.EMAIL_ID = (%s))'''
                        cur.execute(sql1, user)
                    except:
                        pass
                    frame12 = Frame(master1, bg="#FFDCE7")
                    heading2 = Label(frame12, bg="deep sky blue", height=80, width=150, relief="raised",
                                     borderwidth=3)
                    heading2.config(highlightbackground="purple", highlightthickness=2)
                    label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                    label_2.place(x=1000, y=40)
                    label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                  font=("Arial", 14))
                    label.place(x=1020, y=70)
                    heading2.pack(padx=50, pady=170)
                    tree = Treeview(frame12, selectmode='browse')
                    tree["columns"] = ("one", "two")
                    tree.column("one", width=140)
                    tree.column("two", width=140)
                    tree.column("#0", anchor="w", width=0)
                    tree.heading("one", text='Order ID', anchor='w')
                    tree.heading("two", text="Date")
                    f = cur.fetchall()
                    for i in f:
                        orders.append(i[0])
                        tree.insert("", tk.END,
                                    values=(i[0], i[1]))
                    tree.place(x=120, y=240)
                    scrollbar = Scrollbar(frame12, orient=tk.VERTICAL, command=tree.yview)
                    tree.configure(yscrollcommand=scrollbar.set)
                    scrollbar.pack(side='right', fill='y')

                    def but_112():
                        frame7.pack(side="top", fill="both")
                        frame12.forget()

                    button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2,
                                       width=9,
                                       font=("Arial", 14), command=but_112)
                    button_10.place(x=590, y=480)
                    heading4 = Label(frame12, text="Enter Order ID", bg="IndianRed1", height=3, width=20,
                                     font=("Arial", 18))
                    heading4.place(x=440, y=250)
                    lab1 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                    lab1.place(x=440, y=380)
                    ent2 = Entry(frame12, textvariable=2, width=40)
                    ent2.place(x=460, y=410)
                    def check_order():
                        id1 = str(ent2.get())
                        if id1[0] != 'O':
                            messagebox.askokcancel("Error", "Order ID is not Valid!", parent=frame12)
                            ent2.delete(first=0, last=100)
                            ent3.delete(first=0, last=100)
                            return False
                        else:
                            sql1 = '''SELECT DISTINCT PRODUCT_NAME, O.UNIT_PRICE, QUANTITY FROM PRODUCT P, ORDER_DETAILS O 
                            WHERE P.PRODUCT_ID = O.PRODUCT_ID AND O.ORDER_ID = (%s)'''
                            cur.execute(sql1, id1)
                            f = cur.fetchall()
                            rows = orders
                            print(rows,f,id)
                            if len(rows) == 0 or id1 not in rows or len(f)==0:
                                ent2.delete(first=0, last=100)
                                messagebox.askokcancel("Error", "Order ID is not valid.")
                            else:
                                ent2.delete(first=0, last=100)
                                tree = Treeview(frame12, selectmode='browse')
                                tree["columns"] = ("one", "two","three")
                                tree.column("one", width=140)
                                tree.column("two", width=140)
                                tree.column("three", width=140)
                                tree.column("#0", anchor="w", width=0)
                                tree.heading("one", text='Name', anchor='w')
                                tree.heading("two", text="Price")
                                tree.heading("three", text="Quantity")
                                for i in f:
                                    tree.insert("", tk.END,
                                                values=(i[0], i[1],i[2]))
                                tree.place(x=740, y=240)
                                scrollbar = Scrollbar(frame12, orient=tk.VERTICAL, command=tree.yview)
                                tree.configure(yscrollcommand=scrollbar.set)
                                scrollbar.pack(side='right', fill='y')
                    head7 = Button(frame12, text="Submit", bg="orange", bd=2, relief="groove", height=2, width=9,
                                   font=("Arial", 15), command=check_order)
                    head7.place(x=450, y=480)
                    frame12.pack(side="top", fill="both")
                    frame7.forget()
                headingc2 = Button(frame7, text="View Previous Orders", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=view_orders)
                headingc2.place(x=470, y=260)
                def browse():
                    frame_customer = get_frame_customer(master_new)
                    frame_customer.pack(side="top", fill="both")
                    frame7.forget()
                headingc4 = Button(frame7, text="Browse and Shop!", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=browse)
                headingc4.place(x=470, y=310)
                headingc5 = Button(frame7, text="Update Personal Information", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=back)
                headingc5.place(x=470, y=360)
                def del_review():
                    reviews = []
                    try:
                        user = "vielkawoodard@icloud.net"
                        sql1 = '''SELECT DISTINCT R.PRODUCT_ID, PRODUCT_NAME, RATING FROM REVIEW R, CUSTOMER C, PRODUCT P
                        WHERE R.CUST_ID = (SELECT CUST_ID FROM CUSTOMER C1 WHERE C1.EMAIL_ID = (%s))
                        AND R.PRODUCT_ID = P.PRODUCT_ID;'''
                        cur.execute(sql1, user)
                    except:
                        pass
                    frame12 = Frame(master1, bg="#FFDCE7")
                    heading2 = Label(frame12, bg="deep sky blue", height=80, width=150, relief="raised",
                                     borderwidth=3)
                    heading2.config(highlightbackground="purple", highlightthickness=2)
                    label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                    label_2.place(x=1000, y=40)
                    label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                  font=("Arial", 14))
                    label.place(x=1020, y=70)
                    heading2.pack(padx=50, pady=170)
                    tree = Treeview(frame12, selectmode='browse')
                    tree["columns"] = ("one", "two","three")
                    tree.column("one", width=80)
                    tree.column("two", width=100)
                    tree.column("three", width=100)
                    tree.column("#0", anchor="w", width=0)
                    tree.heading("one", text='Product ID', anchor='w')
                    tree.heading("two", text="Name")
                    tree.heading("three", text="Rating (x/5)")
                    f = cur.fetchall()
                    for i in f:
                        reviews.append(i[0])
                        tree.insert("", tk.END,
                                    values=(i[0], i[1], i[2]))
                    tree.place(x=120, y=240)
                    scrollbar = Scrollbar(frame12, orient=tk.VERTICAL, command=tree.yview)
                    tree.configure(yscrollcommand=scrollbar.set)
                    scrollbar.pack(side='right', fill='y')

                    def but_112():
                        frame7.pack(side="top", fill="both")
                        frame12.forget()

                    button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2,
                                       width=9,
                                       font=("Arial", 14), command=but_112)
                    button_10.place(x=590, y=480)
                    heading4 = Label(frame12, text="Enter Product ID", bg="IndianRed1", height=3, width=20,
                                     font=("Arial", 18))
                    heading4.place(x=440, y=250)
                    lab1 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                    lab1.place(x=440, y=380)
                    ent2 = Entry(frame12, textvariable=2, width=40)
                    ent2.place(x=460, y=410)
                    def check_order():
                        id1 = str(ent2.get())
                        if id1[0] != 'P':
                            messagebox.askokcancel("Error", "Product ID is not Valid!", parent=frame12)
                            ent2.delete(first=0, last=100)
                            ent3.delete(first=0, last=100)
                            return False
                        else:
                            sql1 = '''SELECT DISTINCT R.PRODUCT_ID, PRODUCT_NAME, RATING FROM REVIEW R, CUSTOMER C, PRODUCT P
                            WHERE R.CUST_ID = (SELECT CUST_ID FROM CUSTOMER C1 WHERE C1.EMAIL_ID = (%s))
                            AND R.PRODUCT_ID = P.PRODUCT_ID AND R.PRODUCT_ID = (%s);'''
                            cur.execute(sql1, (user,id1))
                            f = cur.fetchall()
                            rows = reviews
                            print(rows,f,id)
                            if len(rows) == 0 or id1 not in rows or len(f)==0:
                                ent2.delete(first=0, last=100)
                                messagebox.askokcancel("Error", "Product ID is not valid.")
                            else:
                                ent2.delete(first=0, last=100)
                                tree = Treeview(frame12, selectmode='browse')
                                tree["columns"] = ("one", "two","three")
                                tree.column("one", width=140)
                                tree.column("two", width=140)
                                tree.column("three", width=140)
                                tree.column("#0", anchor="w", width=0)
                                tree.heading("one", text='Name', anchor='w')
                                tree.heading("two", text="Price")
                                tree.heading("three", text="Quantity")
                                for i in f:
                                    tree.insert("", tk.END,
                                                values=(i[0], i[1],i[2]))
                                tree.place(x=740, y=240)
                                scrollbar = Scrollbar(frame12, orient=tk.VERTICAL, command=tree.yview)
                                tree.configure(yscrollcommand=scrollbar.set)
                                scrollbar.pack(side='right', fill='y')
                                sql2 = '''DELETE FROM REVIEW R WHERE PRODUCT_ID = (%s) AND 
                                R.CUST_ID = (SELECT CUST_ID FROM CUSTOMER C1 WHERE C1.EMAIL_ID = (%s));'''
                                cur.execute(sql2,(id1,user))

                                # sql3 = '''INSERT INTO REVIEW VALUES ('C111','P129','2')'''
                                mydb.commit()
                    head7 = Button(frame12, text="Submit", bg="orange", bd=2, relief="groove", height=2, width=9,
                                   font=("Arial", 15), command=check_order)
                    head7.place(x=450, y=480)
                    frame12.pack(side="top", fill="both")
                    frame7.forget()
                headingc6 = Button(frame7, text="Delete Reviews", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=del_review)
                headingc6.place(x=470, y=410)
                def add_review():
                    pass
                headingc3 = Button(frame7, text="Add Review", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=back)
                headingc3.place(x=470, y=460)

                def but_10():
                    frame3.pack(side="top", fill="both")
                    frame7.forget()

                button_10 = Button(frame7, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                   font=("Arial", 15), command=but_10)
                button_10.place(x=300, y=600)
                frame7.pack(side="top", fill="both")
                frame3.forget()
            def back():
                frame1.pack(side = "top", fill = "both")
                frame3.forget()

            def get_frame_customer(master):

                frame = Frame(master, bg="#FFDCE7")
                def back():
                    frame3.pack(side = "top", fill = "both")
                    frame.forget()

                heading2 = Label(frame, bg="deep sky blue", height=30, width=100, relief="raised", borderwidth=3)
                heading2.config(highlightbackground="purple", highlightthickness=2)
                # heading2.pack(padx=250, pady=150)
                heading_2 = Label(frame, text="Customer", height=2, bg="#FFDCE7", font=("Helvetica Bold 16", 28))
                heading_2.pack(padx=0)
                button = Button(frame, text="cart", bg="deep sky blue", fg="black", font=("Arial", 16),
                                command=lambda: True)
                button.place(x=1050, y=10)
                button = Button(frame, text="logout", bg="deep sky blue", fg="black", font=("Arial", 16),
                                command=back)
                button.place(x=1150, y=10)

                button = Button(frame, text="Add to cart", bg="deep sky blue", fg="black", font=("Arial", 16),
                                command=back)
                button.place(x=1050, y=500)

                canvas = Canvas(frame, height=800)
                framescroll = Frame(canvas, bg="#FFDCE7")
                canvas.create_window((0, 0), window=framescroll, anchor='nw')
                # canvas.configure(scrollregion=(0, 0, 0, 1000))
                canvas.pack(side="left", fill="y",padx = 100,pady = 20)

                vbar = Scrollbar(frame, orient='vertical', command=canvas.yview)

                vbar.pack(side='right', fill='y')


                canvas.config(yscrollcommand=vbar.set)
                framescroll.bind('<Configure>', lambda event, canvas=canvas: canvas.configure(scrollregion=canvas.bbox('all')))
                # products =
                cur=mydb.cursor()
                sql = "SELECT PRODUCT_ID,PRODUCT_NAME,UNIT_PRICE,DISCOUNT,UNIT_WEIGHT,IN_STOCK from retailstore.PRODUCT;"
                cur.execute(sql)
                res = cur.fetchall()
                print(res)
                res = [[str(2*i),2*i+1,'product','name'] for i in range(100)]
                r,c  = 0,0
                order ={}
                order_label = {}

                def orderneg(pid):
                    if pid not in order or order[pid] == 0:
                        return
                    order[pid] -= 1
                    order_label[pid].config(text=str(order[pid]))


                def orderpos(pid):
                    if pid not in order:
                        order[pid] = 0
                    order[pid] += 1
                    order_label[pid].config(text=str(order[pid]))
                for i in res:
                    for j in i:
                        label = Label(framescroll, text=j, bg="deep sky blue", fg="black", font=("Arial", 16))
                        label.grid(row=r, column=c)
                        c+=1

                    buttonneg = Button(framescroll, text="-", bg="deep sky blue", fg="black", font=("Arial", 16),
                                command=lambda pid = i[0]: orderneg(pid))
                    buttonneg.grid(row=r, column=c)
                    c+=1
                    label = Label(framescroll, text="0", bg="deep sky blue", fg="black", font=("Arial", 16))
                    order_label[i[0]] = label
                    label.grid(row=r, column=c)
                    c+=1
                    buttonpos = Button(framescroll, text="+", bg="deep sky blue", fg="black", font=("Arial", 16),
                                command=lambda pid = i[0]: orderpos(pid))
                    buttonpos.grid(row=r, column=c)
                    c+=1
                    r+=1
                    c=0

                frame.place(x=0, y=118)
                frame.pack(side="top", fill="both")
                frame.forget()
                return frame

            def get(head):
                user = head.get()
                return user

            heading4_2 = Entry(frame3, textvariable=2, width=30)
            heading4_2.place(x=620, y=230)

            heading6_2 = Entry(frame3, textvariable=1, width=30, show="*")
            heading6_2.place(x=620, y=380)
            def back():
                frame1.pack(side = "top", fill = "both")
                frame3.forget()
            def callbac():
                passw = heading6_2.get()
                user = heading4_2.get()
                customer_pages(master_new,user,passw)
                return
                # if user in dict_customers.keys() and passw in dict_customers.values() and dict_customers[user] == passw:
                #     a = messagebox.askquestion("Success", "Would you like to continue?")
                #     if a == "yes":
                #         messagebox.showinfo("Success", "You will be directed to the page in a short while")
                #         heading6_2.delete(first=0, last=100)
                #         heading4_2.delete(first=0, last=100)
                #         frame_customer = get_frame_customer(master_new)
                #         frame_customer.pack(side="top", fill="both")
                #         frame3.forget()
                #     else:
                #         heading6_2.delete(first=0, last=100)
                #         heading4_2.delete(first=0, last=100)
                #         back()
                #         #('blythe_case7564@aol.net', 'NJJ74DHN7XA'),
                #         # ('c.erickson6969@outlook.edu', 'IYL06VQE3DK'),
                #         # ('hebertcharity5210@yahoo.in', 'BAY99IMX4JE')
                # elif user in dict_customers.keys() and passw not in dict_customers.values():
                #     messagebox.askokcancel("Error", "Enter the correct details")
                #     heading6_2.delete(first=0, last=100)
                #     heading4_2.delete(first=0, last=100)
                # elif user not in dict_customers.keys() and passw in dict_customers.values():
                #     messagebox.askokcancel("Error", "Enter the correct details")
                #     heading6_2.delete(first=0, last=100)
                #     heading4_2.delete(first=0, last=100)
                # else:
                #     messagebox.askokcancel("Error", "Enter the correct details")
                #     heading6_2.delete(first=0, last=100)
                #     heading4_2.delete(first=0, last=100)

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
            list_emp=[]
            heading2.pack(padx=250, pady=150)
            heading3 = Label(frame4, text="Email Address", bg="IndianRed1", height=3, width=12, font=("Arial", 18))
            heading3.place(x=380, y=200)

            heading5 = Label(frame4, bg="IndianRed1", height=5, width=30, relief="groove")
            heading5.place(x=600, y=200)

            heading8 = Label(frame4, text="Password", bg="IndianRed1", height=3, width=12, font=("Arial", 18))
            heading8.place(x=380, y=350)

            heading5 = Label(frame4, bg="IndianRed1", height=5, width=30, relief="groove")
            heading5.place(x=600, y=350)

            heading4_1 = Entry(frame4, textvariable=2, width=30)
            heading4_1.place(x=620, y=230)

            heading6_1 = Entry(frame4, textvariable=1, width=30, show="*")
            heading6_1.place(x=620, y=380)

            def frame_employee(master1):
                frame7 = Frame(master1, bg="#FFDCE7")
                heading2 = Label(frame7, bg="deep sky blue", height=80, width=60, relief="raised", borderwidth=3)
                heading2.config(highlightbackground="purple", highlightthickness=2)
                label_2 = Label(frame7, bg="yellow", height=6, width=30, relief="raised")
                label_2.place(x=1000, y=40)
                label = Label(frame7, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                              font=("Arial", 14))
                label.place(x=1020, y=70)
                heading2.pack(padx=150, pady=170)
                frame8 = Frame(master1, bg="#FFDCE7")
                def add_products():
                    frame8 = Frame(master1, bg="#FFDCE7")
                    heading2 = Label(frame8, bg="deep sky blue", height=60, width=80, relief="raised", borderwidth=3)
                    heading2.config(highlightbackground="purple", highlightthickness=2)
                    label_2 = Label(frame8, bg="yellow", height=6, width=30, relief="raised")
                    label_2.place(x=1000, y=20)
                    #+list_emp[-1]
                    label = Label(frame8, text="Hello, " + "John" , fg="dark green", bg="white", width=15,
                                  font=("Arial", 14))
                    label.place(x=1020, y=50)
                    heading2.place(x=20, y=150)
                    heading2.pack(side="left",padx = 20,pady = 150)
                    heading3 = Label(frame8, text="Product Name", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
                    heading3.place(x=40, y=180)
                    lab1 = Label(frame8, bg="IndianRed1", height=5, width=30, relief="groove")
                    lab1.place(x=370, y=180)
                    ent1 = Entry(frame8, textvariable=1, width=30)
                    ent1.place(x=385, y=210)
                    heading5 = Label(frame8, text="Unit Weight", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
                    heading5.place(x=40, y=280)
                    lab2 = Label(frame8, bg="IndianRed1", height=5, width=30, relief="groove")
                    lab2.place(x=370, y=280)
                    ent2 = Entry(frame8, textvariable=2, width=30)
                    ent2.place(x=385, y=310)
                    heading8 = Label(frame8, text="Unit Price", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
                    heading8.place(x=40, y=380)
                    lab3 = Label(frame8, bg="IndianRed1", height=5, width=30, relief="groove")
                    lab3.place(x=370, y=380)
                    ent3 = Entry(frame8, textvariable=3, width=30)
                    ent3.place(x=385, y=410)

                    ent4 = Entry(frame8,textvariable=4,width = 30)

                    c = 100
                    l = [False,False,False,False,False,False,False,False,False,False]
                    def cosmetics(value):
                        global c
                        c = 0
                        lab1 = Label(frame8,text = "Category ID: " + "CT10" + str(c),font=("Arial", 18),bg = "deep sky blue")
                        lab1.place(x = 150, y = 500)
                        ent4.insert(0,'0')
                        l[c] = True
                    heading1 = Button(frame8, text="Cosmetics", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=lambda *args: cosmetics(0))
                    heading1.place(x=770, y=120)
                    def grocery():
                        global c
                        c = 1
                        lab1 = Label(frame8,text = "Category ID: " + "CT10" + str(c),font=("Arial", 18),bg = "deep sky blue")
                        lab1.place(x = 150, y = 500)
                        ent4.insert(0,'1')
                        c = 1
                        l[c] = True
                    heading2 = Button(frame8, text="Grocery", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14),
                                      command=grocery)
                    heading2.place(x=770, y=170)
                    def clothes():
                        global c
                        c = 2
                        ent4.insert(0, str(c))
                        lab1 = Label(frame8,text = "Category ID: " + "CT10" + str(c),font=("Arial", 18),bg = "deep sky blue")
                        lab1.place(x = 150, y = 500)
                        c = 2
                        l[c] = True
                    heading3 = Button(frame8, text="Clothes", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14),
                                      command=clothes)
                    heading3.place(x=770, y=220)
                    def shoes():
                        global c
                        lab1 = Label(frame8,text = "Category ID: CT103",font=("Arial", 18),bg = "deep sky blue")
                        lab1.place(x = 150, y = 500)
                        c = 3
                        ent4.insert(0, str(c))
                        l[c] = True
                    heading4 = Button(frame8, text="Shoes", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=shoes)
                    heading4.place(x=770, y=270)
                    def toys():
                        global c
                        lab1 = Label(frame8,text = "Category ID: CT104",font=("Arial", 18),bg = "deep sky blue")
                        lab1.place(x = 150, y = 500)
                        c = 4
                        ent4.insert(0, str(c))
                        l[c] = True
                    heading5 = Button(frame8, text="Toys", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=toys)
                    heading5.place(x=770, y=320)
                    def furniture():
                        global c
                        lab1 = Label(frame8,text = "Category ID: CT105",font=("Arial", 18),bg = "deep sky blue")
                        lab1.place(x = 150, y = 500)
                        c = 5
                        ent4.insert(0, str(c))
                    heading6 = Button(frame8, text="Furniture", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=furniture)
                    heading6.place(x=770, y=370)
                    def electronics():
                        global c
                        lab1 = Label(frame8,text = "Category ID: CT106",font=("Arial", 18),bg = "deep sky blue")
                        lab1.place(x = 150, y = 500)
                        c = 6
                        ent4.insert(0, str(c))
                    heading7 = Button(frame8, text="Electronics", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=electronics)
                    heading7.place(x=770, y=420)
                    def sports():
                        global c
                        lab1 = Label(frame8,text = "Category ID: CT107",font=("Arial", 18),bg = "deep sky blue")
                        lab1.place(x = 150, y = 500)
                        c = 7
                        ent4.insert(0, str(c))
                    heading8 = Button(frame8, text="Sports", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=sports)
                    heading8.place(x=770, y=470)
                    def pharmacy():
                        global c
                        lab1 = Label(frame8,text = "Category ID: CT108",font=("Arial", 18),bg = "deep sky blue")
                        lab1.place(x = 150, y = 500)
                        c = 8
                        ent4.insert(0, str(c))
                    heading9 = Button(frame8, text="Pharmacy", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=pharmacy)
                    heading9.place(x=770, y=520)
                    def stationery():
                        global c
                        lab1 = Label(frame8,text = "Category ID: CT109",font=("Arial", 18),bg = "deep sky blue")
                        lab1.place(x = 150, y = 500)
                        c = 9
                        ent4.insert(0, str(c))
                    heading10 = Button(frame8, text="Stationery", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=stationery)
                    heading10.place(x=770, y=570)
                    def check_name():
                        name = str(ent1.get())
                        if name.isalpha() == True:
                            return True
                        elif name.isdigit() == True:
                            ent1.delete(first=0, last=100)
                            return False
                        elif name.isalnum() == True:
                            ent1.delete(first=0, last=100)
                            return False
                    def check_price():
                        price = str(ent3.get())
                        if price.isnumeric() == True and int(price) > 0:
                            return True
                        elif price.isalpha() or price.isalnum() == True:
                            return False
                        elif '-' in price or price=='0':
                            return False
                    def check_weight():
                        weight = str(ent2.get())
                        if weight.isnumeric() == True and int(weight) > 0:
                            return True
                        elif weight.isalpha() or weight.isalnum() == True:
                            return False
                        elif '-' in weight or weight == '0':
                            return False
                    def check_cat():
                        if ent4.get()=='':
                            return False
                        else:
                            return True
                    def chk_adm1():  # validating admission number
                        cur = mydb.cursor()
                        sql = "SELECT PRODUCT_ID from PRODUCT;"
                        cur.execute(sql)
                        res = cur.fetchall()
                        l = []
                        for i in res:
                            l.append(i[0])
                        c_id = 'P' + str(int(l[-1][1:]) + 1)
                        return c_id
                    def check_detail():
                        category = "CT10" + ent4.get()
                        product_id = chk_adm1()
                        print(c)
                        discount = 0
                        quantity = 1
                        f = 0
                        if (check_name()!=True):
                            ent1.delete(first=0, last=100)
                            f = 1
                        if (check_weight()!=True):
                            ent2.delete(first=0, last=100)
                            f = 1
                        if (check_price()!=True):
                            ent3.delete(first=0, last=100)
                            f = 1
                        if (check_cat()!=True):
                            f = 1
                            ent4.delete(first=0,last=100)
                            messagebox.askokcancel("Error", "Choose Category!", parent=frame8)

                        else:

                            if (f==1):
                                messagebox.askokcancel("Error", "Enter Correctly!", parent=frame8)
                            else:
                                messagebox.showinfo("Success", "Data Saved!", parent=frame8)
                                name = ent1.get()
                                weight,price = int(ent2.get()), int(ent3.get())
                                cur = mydb.cursor()
                                sql = 'INSERT INTO PRODUCT values(%s,%s,%s,%s,%s,%s,%s);'
                                val = (product_id, name, quantity, price,weight, discount, category)
                                print(val)
                                cur.execute(sql, val)
                                ent1.delete(first=0, last=100)
                                ent2.delete(first=0, last=100)
                                ent3.delete(first=0, last=100)
                                ent4.delete(first=0,last=100)
                                mydb.commit()
                                print("Data added")

                    head7 = Button(frame8, text="Submit", bg="orange", bd=2, relief="groove", height=2, width=9,
                                      font=("Arial", 15), command=check_detail)
                    head7.place(x=150, y=600)
                    def but_10():
                        ent1.delete(first=0, last=100)
                        ent2.delete(first=0, last=100)
                        ent3.delete(first=0, last=100)
                        ent4.delete(first=0, last=100)
                        frame7.pack(side="top", fill="both")
                        frame8.forget()
                    button_10 = Button(frame8, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                       font=("Arial", 15), command=but_10)
                    button_10.place(x=300, y=600)
                    frame8.pack(side="top", fill="both")
                    frame7.forget()
                heading1 = Button(frame7, text="Add Products", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=add_products)
                heading1.place(x=470, y=180)
                def delete_prod():
                    frame9 = Frame(master_new, bg="#FFDCE7")
                    heading2 = Label(frame9, bg="deep sky blue", height=60, width=60, relief="raised", borderwidth=3)
                    heading2.config(highlightbackground="purple", highlightthickness=2)
                    label_2 = Label(frame9, bg="yellow", height=6, width=30, relief="raised")
                    label_2.place(x=1000, y=40)
                    label = Label(frame9, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                  font=("Arial", 14))
                    label.place(x=1020, y=70)
                    heading2.pack(padx=150, pady=170)
                    def delete_prodid():
                        frame10 = Frame(master_new, bg="#FFDCE7")
                        heading2 = Label(frame10, bg="deep sky blue", height=60, width=60, relief="raised",
                                         borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame10, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame10, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        heading4 = Label(frame10, text="Enter Product ID", bg="IndianRed1", height=3, width=20,
                                         font=("Arial", 18))
                        heading4.place(x=490, y=250)
                        lab1 = Label(frame10, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab1.place(x=490, y=380)
                        ent2 = Entry(frame10, textvariable=2, width=40)
                        ent2.place(x=510, y=410)
                        frame10.pack(side="top", fill="both")
                        frame9.forget()
                        def check_id():
                            id = str(ent2.get())
                            if id[0]!='P' and id[0]!='p':
                                messagebox.askokcancel("Error","Product ID is not Valid!",parent=frame10)
                                ent2.delete(first=0, last=100)
                                ent3.delete(first=0, last=100)
                                return False
                            else:
                                sql1 = '''SELECT * FROM PRODUCT WHERE PRODUCT_ID = (%s)'''
                                cur.execute(sql1,id)
                                rows = cur.fetchall()
                                if len(rows)==0:
                                    ent2.delete(first = 0, last= 100)
                                    messagebox.askokcancel("Error","Product ID is not valid.")
                                else:
                                    ent2.delete(first=0, last=100)
                                    messagebox.showinfo("Success", "Item Deleted!")
                                    sql1 = '''DELETE FROM PRODUCT WHERE PRODUCT_ID=(%s)'''
                                    cur.execute(sql1,id)
                                    mydb.commit()

                        head7 = Button(frame10, text="Submit", bg="orange", bd=2, relief="groove", height=2, width=9,
                                       font=("Arial", 15), command=check_id)
                        head7.place(x=500, y=480)

                        def but_10():

                            frame9.pack(side="top", fill="both")
                            frame10.forget()

                        button_10 = Button(frame10, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                           font=("Arial", 14), command=but_10)
                        button_10.place(x=650, y=480)
                        frame10.pack(side="top", fill="both")
                        frame9.forget()
                    heading3 = Button(frame9, text="Delete by Product ID", bg="IndianRed1", height=3, width=20,
                                      font=("Arial", 18), command=delete_prodid)
                    heading3.place(x=490, y=180)
                    def delete_prodname():

                        frame10 = Frame(master_new, bg="#FFDCE7")
                        heading2 = Label(frame10, bg="deep sky blue", height=60, width=60, relief="raised",
                                         borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame10, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame10, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        heading4 = Label(frame10, text="Enter Product Name", bg="IndianRed1", height=3, width=20,
                                         font=("Arial", 18))
                        heading4.place(x=490, y=250)
                        lab1 = Label(frame10, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab1.place(x=490, y=380)
                        ent2 = Entry(frame10, textvariable=2, width=40)
                        ent2.place(x=510, y=410)
                        frame10.pack(side="top", fill="both")
                        frame9.forget()
                        def check_name():
                            id = str(ent2.get())
                            sql1 = '''SELECT * FROM PRODUCT WHERE PRODUCT_NAME = (%s)'''
                            cur.execute(sql1,id)
                            rows = cur.fetchall()
                            if len(rows)==0:
                                ent2.delete(first = 0, last= 100)
                                messagebox.askokcancel("Error","Product Name is not valid.")
                            else:
                                ent2.delete(first=0, last=100)
                                messagebox.showinfo("Success", "Item Deleted!")
                                sql1 = '''DELETE FROM PRODUCT WHERE PRODUCT_NAME=(%s)'''
                                cur.execute(sql1,id)
                                mydb.commit()

                        head7 = Button(frame10, text="Submit", bg="orange", bd=2, relief="groove", height=2, width=9,
                                       font=("Arial", 15), command=check_name)
                        head7.place(x=500, y=480)

                        def but_10():

                            frame9.pack(side="top", fill="both")
                            frame10.forget()

                        button_10 = Button(frame10, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                           font=("Arial", 14), command=but_10)
                        button_10.place(x=650, y=480)
                        frame10.pack(side="top", fill="both")
                        frame9.forget()
                    heading5 = Button(frame9, text="Delete by Product Name", bg="IndianRed1", height=3, width=20,
                                      font=("Arial", 18), command=delete_prodname)
                    heading5.place(x=490, y=310)
                    def delete_category():

                        frame10 = Frame(master_new, bg="#FFDCE7")
                        heading2 = Label(frame10, bg="deep sky blue", height=60, width=60, relief="raised",
                                         borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame10, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame10, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        heading4 = Label(frame10, text="Enter Category ID", bg="IndianRed1", height=3, width=20,
                                         font=("Arial", 18))
                        heading4.place(x=490, y=250)
                        lab1 = Label(frame10, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab1.place(x=490, y=380)
                        ent2 = Entry(frame10, textvariable=2, width=40)
                        ent2.place(x=510, y=410)
                        frame10.pack(side="top", fill="both")
                        frame9.forget()
                        def check_category():
                            id = str(ent2.get())
                            sql1 = '''SELECT * FROM CATEGORY'''
                            cur.execute(sql1)
                            rows = cur.fetchall()
                            cat = []
                            for i in rows:
                                cat.append(i[0])
                            if id not in cat:
                                messagebox.askokcancel("Error","Enter a valid Category ID")
                                ent2.delete(first = 0, last = 100)
                                return False
                            else:
                                heading3 = Label(frame10, bg="cyan", height=90, width=40, relief="raised",
                                                 borderwidth=3)
                                heading3.config(highlightbackground="purple", highlightthickness=2)
                                heading3.place(x = 100, y =5)
                                sql1 = '''SELECT PRODUCT_ID, PRODUCT_NAME FROM PRODUCT WHERE CATEGORY_ID=(%s)'''
                                val = str(ent2.get())
                                cur.execute(sql1,val)
                                rows = cur.fetchall()
                                row = []
                                prod_ids = []
                                for i in rows:
                                    row.append([i[0],i[1]])
                                    prod_ids.append(i[0])
                                for j in range(len(row)):
                                        but1 = Button(frame10, text = row[j][0] + ": " + row[j][1],font=("Arial", 12), bg="IndianRed1", height=2, width=20, relief="groove")
                                        but1.place(x = 150, y = 10 + j*45)
                                        row[j].append(but1)
                                heading2 = Label(frame10, bg="cyan", height=50, width=40, relief="raised",
                                                 borderwidth=3)
                                heading2.config(highlightbackground="purple", highlightthickness=2)
                                heading2.place(x = 900, y = 200)
                                heading4 = Label(frame10, text="Enter Product ID", bg="IndianRed1", height=3, width=15,
                                                 font=("Arial", 18))
                                heading4.place(x=940, y=250)
                                lab1 = Label(frame10, bg="IndianRed1", height=5, width=30, relief="groove")
                                lab1.place(x=940, y=380)
                                ent3 = Entry(frame10, textvariable=3, width=30)
                                ent3.place(x=955, y=410)
                                def check_id():
                                    val = str(ent3.get())
                                    if val not in prod_ids:
                                        messagebox.askokcancel("Error","Product ID not valid!",parent = frame10)
                                        ent3.delete(first = 0, last = 100)
                                    else:
                                        sql1 = '''DELETE FROM PRODUCT WHERE PRODUCT_ID=(%s)'''
                                        cur.execute(sql1,val)
                                        mydb.commit()
                                        ent3.delete(first = 0, last = 100)
                                        messagebox.showinfo("Success","Item Deleted!")
                                head7 = Button(frame10, text="Delete", bg="orange", bd=2, relief="groove", height=2, width=9,
                                               font=("Arial", 15), command=check_id)
                                head7.place(x = 970, y = 500)

                        head7 = Button(frame10, text="Submit", bg="orange", bd=2, relief="groove", height=2, width=9,
                                       font=("Arial", 15), command=check_category)
                        head7.place(x=500, y=480)

                        def but_10():
                            ent2.delete(first = 0, last = 100)
                            frame9.pack(side="top", fill="both")
                            frame10.forget()

                        button_10 = Button(frame10, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                           font=("Arial", 14), command=but_10)
                        button_10.place(x=650, y=480)
                        frame10.pack(side="top", fill="both")
                        frame9.forget()
                    heading8 = Button(frame9, text="Delete by Category", bg="IndianRed1", height=3, width=20,
                                      font=("Arial", 18), command=delete_category)
                    heading8.place(x=490, y=440)
                    def but_10():

                        frame7.pack(side="top", fill="both")
                        frame9.forget()
                    button_10 = Button(frame9, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                       font=("Arial", 14), command=but_10)
                    button_10.place(x=300, y=600)
                    frame9.pack(side="top", fill="both")
                    frame7.forget()

                heading2 = Button(frame7, text="Delete Products", bg="IndianRed1", height=2, width=30, font=("Arial", 14),
                                  command=delete_prod)
                heading2.place(x=470, y=230)
                def upd_products():
                    frame11 = Frame(master1, bg="#FFDCE7")
                    heading2 = Label(frame11, bg="deep sky blue", height=60, width=60, relief="raised", borderwidth=3)
                    heading2.config(highlightbackground="purple", highlightthickness=2)
                    label_2 = Label(frame11, bg="yellow", height=6, width=30, relief="raised")
                    label_2.place(x=1000, y=40)
                    label = Label(frame11, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                  font=("Arial", 14))
                    label.place(x=1020, y=70)
                    heading2.pack(padx=150, pady=170)
                    def upd_name():
                        frame12 = Frame(master1, bg="#FFDCE7")
                        heading2 = Label(frame12, bg="deep sky blue", height=100, width=60, relief="raised",
                                         borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        heading4 = Label(frame12, text="Enter Product ID", bg="IndianRed1", height=3, width=20,
                                         font=("Arial", 18))
                        heading4.place(x=490, y=180)
                        lab1 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab1.place(x=490, y=280)
                        ent2 = Entry(frame12, textvariable=2, width=40)
                        ent2.place(x=510, y=310)
                        heading_5 = Label(frame12, text="Enter Updated Name", bg="IndianRed1", height=3, width=20,
                                         font=("Arial", 18))
                        heading_5.place(x=490, y=370)
                        lab4 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab4.place(x=490, y=470)
                        ent3 = Entry(frame12, textvariable=3, width=40)
                        ent3.place(x=510, y=500)
                        def check_deets():
                            id = str(ent2.get())
                            print(id,ent3.get())
                            if id[0]!='P' and id[0]!='p':
                                messagebox.askokcancel("Error","Product ID is not Valid!",parent=frame12)
                                ent2.delete(first=0, last=100)
                                ent3.delete(first=0, last=100)
                                return False
                            else:
                                val2 = str(ent3.get())
                                sql1 = '''SELECT * FROM PRODUCT WHERE PRODUCT_ID = (%s)'''
                                cur.execute(sql1,id)
                                rows = cur.fetchall()
                                if len(rows)==0:
                                    ent2.delete(first = 0, last= 100)
                                    ent3.delete(first = 0, last = 100)
                                    messagebox.askokcancel("Error","Product ID is not valid.")
                                else:
                                    ent2.delete(first = 0, last= 100)
                                    ent3.delete(first = 0, last = 100)
                                    messagebox.showinfo("Success", "Item Name Updated!")
                                    sql1 = '''UPDATE PRODUCT SET PRODUCT_NAME=(%s) WHERE PRODUCT_ID=(%s)'''
                                    cur.execute(sql1,(val2,id))
                                    mydb.commit()
                        head_0 = Button(frame12, text="Submit", bg="orange", bd=2, relief="groove", height=2, width=9,
                                       font=("Arial", 15), command=check_deets)
                        head_0.place(x=500, y=580)

                        def but_10():
                            ent2.delete(first=0, last=100)
                            ent3.delete(first=0, last=100)
                            frame11.pack(side="top", fill="both")
                            frame12.forget()

                        button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                           font=("Arial", 14), command=but_10)
                        button_10.place(x=650, y=580)
                        frame12.pack(side="top", fill="both")
                        frame11.forget()
                    heading3 = Button(frame11, text="Update Name", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14),
                                      command=upd_name)
                    heading3.place(x=470, y=200)
                    def upd_weight():
                        frame12 = Frame(master1, bg="#FFDCE7")
                        heading2 = Label(frame12, bg="deep sky blue", height=100, width=60, relief="raised",
                                         borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        heading4 = Label(frame12, text="Enter Product ID", bg="IndianRed1", height=3, width=20,
                                         font=("Arial", 18))
                        heading4.place(x=490, y=180)
                        lab1 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab1.place(x=490, y=280)
                        ent2 = Entry(frame12, textvariable=2, width=40)
                        ent2.place(x=510, y=310)
                        heading_5 = Label(frame12, text="Enter Updated Weight", bg="IndianRed1", height=3, width=20,
                                          font=("Arial", 18))
                        heading_5.place(x=490, y=370)
                        lab4 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab4.place(x=490, y=470)
                        ent3 = Entry(frame12, textvariable=3, width=40)
                        ent3.place(x=510, y=500)

                        def check_deets():
                            id = str(ent2.get())
                            print(id, ent3.get())
                            if id[0] != 'P' and id[0] != 'p':
                                messagebox.askokcancel("Error", "Product ID is not Valid!", parent=frame12)
                                ent2.delete(first=0, last=100)
                                ent3.delete(first=0, last=100)
                                return False
                            else:
                                val2 = str(ent3.get())
                                sql1 = '''SELECT * FROM PRODUCT WHERE PRODUCT_ID = (%s)'''
                                cur.execute(sql1, id)
                                rows = cur.fetchall()
                                if len(rows) == 0:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.askokcancel("Error", "Product ID is not valid.")
                                elif val2<=0:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.askokcancel("Error", "Updated Weight is not valid.")
                                else:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.showinfo("Success", "Item Name Updated!")
                                    sql1 = '''UPDATE PRODUCT SET UNIT_WEIGHT=(%s) WHERE PRODUCT_ID=(%s)'''
                                    cur.execute(sql1, (val2, id))
                                    mydb.commit()

                        head_0 = Button(frame12, text="Submit", bg="orange", bd=2, relief="groove", height=2,
                                        width=9,
                                        font=("Arial", 15), command=check_deets)
                        head_0.place(x=500, y=580)

                        def but_10():
                            ent2.delete(first=0, last=100)
                            ent3.delete(first=0, last=100)
                            frame11.pack(side="top", fill="both")
                            frame12.forget()

                        button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2,
                                           width=9,
                                           font=("Arial", 14), command=but_10)
                        button_10.place(x=650, y=580)
                        frame12.pack(side="top", fill="both")
                        frame11.forget()
                    heading4 = Button(frame11, text="Update Unit Weight", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=upd_weight)
                    heading4.place(x=470, y=250)
                    def upd_discount():
                        frame12 = Frame(master1, bg="#FFDCE7")
                        heading2 = Label(frame12, bg="deep sky blue", height=100, width=60, relief="raised",
                                         borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        heading4 = Label(frame12, text="Enter Product ID", bg="IndianRed1", height=3, width=20,
                                         font=("Arial", 18))
                        heading4.place(x=490, y=180)
                        lab1 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab1.place(x=490, y=280)
                        ent2 = Entry(frame12, textvariable=2, width=40)
                        ent2.place(x=510, y=310)
                        heading_5 = Label(frame12, text="Enter Updated Discount", bg="IndianRed1", height=3, width=20,
                                          font=("Arial", 18))
                        heading_5.place(x=490, y=370)
                        lab4 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab4.place(x=490, y=470)
                        ent3 = Entry(frame12, textvariable=3, width=40)
                        ent3.place(x=510, y=500)

                        def check_deets():
                            id = str(ent2.get())
                            print(id, ent3.get())
                            if id[0] != 'P' and id[0] != 'p':
                                messagebox.askokcancel("Error", "Product ID is not Valid!", parent=frame12)
                                ent2.delete(first=0, last=100)
                                ent3.delete(first=0, last=100)
                                return False
                            else:
                                val2 = str(ent3.get())
                                sql1 = '''SELECT * FROM PRODUCT WHERE PRODUCT_ID = (%s)'''
                                cur.execute(sql1, id)
                                rows = cur.fetchall()
                                if len(rows) == 0:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.askokcancel("Error", "Product ID is not valid.")
                                elif val2<0:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.askokcancel("Error", "Updated Discount is not valid.")
                                else:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.showinfo("Success", "Item Name Updated!")
                                    sql1 = '''UPDATE PRODUCT SET DISCOUNT=(%s) WHERE PRODUCT_ID=(%s)'''
                                    cur.execute(sql1, (val2, id))
                                    mydb.commit()

                        head_0 = Button(frame12, text="Submit", bg="orange", bd=2, relief="groove", height=2,
                                        width=9,
                                        font=("Arial", 15), command=check_deets)
                        head_0.place(x=500, y=580)

                        def but_10():
                            ent2.delete(first=0, last=100)
                            ent3.delete(first=0, last=100)
                            frame11.pack(side="top", fill="both")
                            frame12.forget()

                        button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2,
                                           width=9,
                                           font=("Arial", 14), command=but_10)
                        button_10.place(x=650, y=580)
                        frame12.pack(side="top", fill="both")
                        frame11.forget()
                    heading5 = Button(frame11, text="Update Discount", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=upd_discount)
                    heading5.place(x=470, y=300)

                    def upd_qty():
                        frame13 = Frame(master1, bg="#FFDCE7")
                        heading2 = Label(frame13, bg="deep sky blue", height=100, width=60, relief="raised",
                                         borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame13, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame13, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        heading4 = Label(frame13, text="Enter Product ID", bg="IndianRed1", height=3, width=20,
                                         font=("Arial", 18))
                        heading4.place(x=490, y=180)
                        lab1 = Label(frame13, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab1.place(x=490, y=280)
                        ent2 = Entry(frame13, textvariable=2, width=40)
                        ent2.place(x=510, y=310)
                        heading_5 = Label(frame13, text="Enter Updated Quantity", bg="IndianRed1", height=3, width=20,
                                          font=("Arial", 18))
                        heading_5.place(x=490, y=370)
                        lab4 = Label(frame13, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab4.place(x=490, y=470)
                        ent3 = Entry(frame13, textvariable=3, width=40)
                        ent3.place(x=510, y=500)

                        def check_deets():
                            id = str(ent2.get())
                            print(id, ent3.get())
                            if id[0] != 'P' and id[0] != 'p':
                                messagebox.askokcancel("Error", "Product ID is not Valid!", parent=frame13)
                                ent2.delete(first=0, last=100)
                                ent3.delete(first=0, last=100)
                                return False
                            else:
                                val2 = str(ent3.get())
                                sql1 = '''SELECT * FROM PRODUCT WHERE PRODUCT_ID = (%s)'''
                                cur.execute(sql1, id)
                                rows = cur.fetchall()
                                if len(rows) == 0:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.askokcancel("Error", "Product ID is not valid.")
                                elif val2<=0:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.askokcancel("Error", "Updated Quantity is not valid.")
                                else:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.showinfo("Success", "Item  Updated!")
                                    sql1 = '''UPDATE PRODUCT SET QUANTITY=(%s) WHERE PRODUCT_ID=(%s)'''
                                    cur.execute(sql1, (val2, id))
                                    mydb.commit()

                        head_0 = Button(frame13, text="Submit", bg="orange", bd=2, relief="groove", height=2,
                                        width=9,
                                        font=("Arial", 15), command=check_deets)
                        head_0.place(x=500, y=580)

                        def but_11():
                            ent2.delete(first=0, last=100)
                            ent3.delete(first=0, last=100)
                            frame11.pack(side="top", fill="both")
                            frame13.forget()

                        button_10 = Button(frame13, text="Back", bg="orange", bd=2, relief="groove", height=2,
                                           width=9,
                                           font=("Arial", 14), command=but_11)
                        button_10.place(x=650, y=580)
                        frame13.pack(side="top", fill="both")
                        frame11.forget()
                    heading_6 = Button(frame11, text="Update Quantity", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=upd_qty)
                    heading_6.place(x=470, y=350)
                    def upd_price():
                        frame12 = Frame(master1, bg="#FFDCE7")
                        heading2 = Label(frame12, bg="deep sky blue", height=100, width=60, relief="raised",
                                         borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        heading4 = Label(frame12, text="Enter Product ID", bg="IndianRed1", height=3, width=20,
                                         font=("Arial", 18))
                        heading4.place(x=490, y=180)
                        lab1 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab1.place(x=490, y=280)
                        ent2 = Entry(frame12, textvariable=2, width=40)
                        ent2.place(x=510, y=310)
                        heading_5 = Label(frame12, text="Enter Updated Price", bg="IndianRed1", height=3, width=20,
                                          font=("Arial", 18))
                        heading_5.place(x=490, y=370)
                        lab4 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab4.place(x=490, y=470)
                        ent3 = Entry(frame12, textvariable=3, width=40)
                        ent3.place(x=510, y=500)

                        def check_deets():
                            id = str(ent2.get())
                            print(id, ent3.get())
                            if id[0] != 'P' and id[0] != 'p':
                                messagebox.askokcancel("Error", "Product ID is not Valid!", parent=frame12)
                                ent2.delete(first=0, last=100)
                                ent3.delete(first=0, last=100)
                                return False
                            else:
                                val2 = str(ent3.get())
                                sql1 = '''SELECT * FROM PRODUCT WHERE PRODUCT_ID = (%s)'''
                                cur.execute(sql1, id)
                                rows = cur.fetchall()
                                if len(rows) == 0:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.askokcancel("Error", "Product ID is not valid.")
                                elif val2<0:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.askokcancel("Error", "Updated Unit Price is not valid.")
                                else:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.showinfo("Success", "Item Unit Price Updated!")
                                    sql1 = '''UPDATE PRODUCT SET UNIT_PRICE=(%s) WHERE PRODUCT_ID=(%s)'''
                                    cur.execute(sql1, (val2, id))
                                    mydb.commit()

                        head_0 = Button(frame12, text="Submit", bg="orange", bd=2, relief="groove", height=2,
                                        width=9,
                                        font=("Arial", 15), command=check_deets)
                        head_0.place(x=500, y=580)

                        def but_10():
                            ent2.delete(first=0, last=100)
                            ent3.delete(first=0, last=100)
                            frame11.pack(side="top", fill="both")
                            frame12.forget()

                        button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2,
                                           width=9,
                                           font=("Arial", 14), command=but_10)
                        button_10.place(x=650, y=580)
                        frame12.pack(side="top", fill="both")
                        frame11.forget()
                    heading17 = Button(frame11, text="Update Unit Price", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=upd_price)
                    heading17.place(x = 470, y = 400)
                    def upd_catid():
                        frame12 = Frame(master1, bg="#FFDCE7")
                        heading2 = Label(frame12, bg="deep sky blue", height=100, width=60, relief="raised",
                                         borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        heading4 = Label(frame12, text="Enter Product ID", bg="IndianRed1", height=3, width=20,
                                         font=("Arial", 18))
                        heading4.place(x=490, y=180)
                        lab1 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab1.place(x=490, y=280)
                        ent2 = Entry(frame12, textvariable=2, width=40)
                        ent2.place(x=510, y=310)
                        heading_5 = Label(frame12, text="Enter New Category ID", bg="IndianRed1", height=3, width=20,
                                          font=("Arial", 18))
                        heading_5.place(x=490, y=370)
                        lab4 = Label(frame12, bg="IndianRed1", height=5, width=40, relief="groove")
                        lab4.place(x=490, y=470)
                        ent3 = Entry(frame12, textvariable=3, width=40)
                        ent3.place(x=510, y=500)

                        def check_deets():
                            id = str(ent2.get())
                            print(id, ent3.get())
                            if id[0] != 'P' and id[0] != 'p':
                                messagebox.askokcancel("Error", "Product ID is not Valid!", parent=frame12)
                                ent2.delete(first=0, last=100)
                                ent3.delete(first=0, last=100)
                                return False
                            else:
                                val2 = str(ent3.get())
                                sql1 = '''SELECT * FROM PRODUCT WHERE PRODUCT_ID = (%s)'''
                                cur.execute(sql1, id)
                                rows = cur.fetchall()
                                if len(rows) == 0:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.askokcancel("Error", "Product ID is not valid.")
                                elif val2[0]!='C' and val2[1]!='T':
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.askokcancel("Error", "Updated Category ID is not valid.")
                                else:
                                    ent2.delete(first=0, last=100)
                                    ent3.delete(first=0, last=100)
                                    messagebox.showinfo("Success", "Item Unit Price Updated!")
                                    sql1 = '''UPDATE PRODUCT SET CATEGORY_ID=(%s) WHERE PRODUCT_ID=(%s)'''
                                    cur.execute(sql1, (val2, id))
                                    mydb.commit()

                        head_0 = Button(frame12, text="Submit", bg="orange", bd=2, relief="groove", height=2,
                                        width=9,
                                        font=("Arial", 15), command=check_deets)
                        head_0.place(x=500, y=580)

                        def but_10():
                            ent2.delete(first=0, last=100)
                            ent3.delete(first=0, last=100)
                            frame11.pack(side="top", fill="both")
                            frame12.forget()

                        button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2,
                                           width=9,
                                           font=("Arial", 14), command=but_10)
                        button_10.place(x=650, y=580)
                        frame12.pack(side="top", fill="both")
                        frame11.forget()
                    heading18 = Button(frame11, text="Update Category ID", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=upd_catid)
                    heading18.place(x = 470, y = 450)

                    def but_10():
                        frame7.pack(side="top", fill="both")
                        frame11.forget()

                    button_10 = Button(frame11, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                       font=("Arial", 14), command=but_10)
                    button_10.place(x=650, y=580)
                    frame11.pack(side="top", fill="both")
                    frame7.forget()
                heading3 = Button(frame7, text="Update Products", bg="IndianRed1", height=2, width=30, font=("Arial", 14),
                                  command=upd_products)
                heading3.place(x=470, y=280)
                def view_stake():
                    frame11 = Frame(master1, bg="#FFDCE7")
                    heading2 = Label(frame11, bg="deep sky blue", height=60, width=60, relief="raised", borderwidth=3)
                    heading2.config(highlightbackground="purple", highlightthickness=2)
                    label_2 = Label(frame11, bg="yellow", height=6, width=30, relief="raised")
                    label_2.place(x=1000, y=40)
                    label = Label(frame11, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                  font=("Arial", 14))
                    label.place(x=1020, y=70)
                    heading2.pack(padx=150, pady=170)
                    def view_cust():
                        try:
                            sql1 = '''CREATE VIEW CUSTOMER_DETAILS AS
                                    SELECT CUST_ID,FIRST_NAME,LAST_NAME,EMAIL_ID,LOCALITY,CITY,STATE,COUNTRY,POSTAL_CODE,PHONE_NUMBER
                                    FROM CUSTOMER,CUSTOMER_INFORMATION WHERE CUSTOMER.CUST_ID = CUSTOMER_INFORMATION.PERSONAL_ID;'''
                            cur.execute(sql1)
                        except:
                            pass
                        frame12 = Frame(master1, bg="#FFDCE7")
                        heading2 = Label(frame12, bg="deep sky blue", height=80, width=240, relief="raised", borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        tree = Treeview(frame12,selectmode ='browse')
                        tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven","eight","nine","ten")
                        tree.column("one", width=50)
                        tree.column("two", width=80)
                        tree.column("three", width=80)
                        tree.column("four", width=140)
                        tree.column("five", width=140)
                        tree.column("six", width=100)
                        tree.column("seven", width=100)
                        tree.column("eight", width=100)
                        tree.column("nine", width=90)
                        tree.column("ten", width=100)
                        tree.column("#0", anchor="w",width=0)
                        tree.heading("one", text='Customer ID', anchor='w')
                        tree.heading("two", text="First Name")
                        tree.heading("three", text="Last Name")
                        tree.heading("four", text="Email Address")
                        tree.heading("five", text="Locality")
                        tree.heading("six", text="City")
                        tree.heading("seven", text="State")
                        tree.heading("eight", text="Country")
                        tree.heading("nine", text = "Postal Code")
                        tree.heading("ten", text = "Contact")
                        cur.execute("SELECT * FROM CUSTOMER_DETAILS;")
                        f = cur.fetchall()
                        for i in f:
                            tree.insert("", tk.END, values=(i[0],i[1], i[2], i[3], i[4], i[5], i[6], i[7],i[8],i[9]))
                        tree.place(x=148, y=240)
                        scrollbar = Scrollbar(frame12,orient = tk.VERTICAL, command = tree.yview)
                        tree.configure(yscrollcommand = scrollbar.set)
                        scrollbar.pack(side='right',fill='y')

                        def but_112():
                            frame11.pack(side="top", fill="both")
                            frame12.forget()

                        button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                           font=("Arial", 14), command=but_112)
                        button_10.place(x=650, y=580)
                        frame12.pack(side="top", fill="both")
                        frame11.forget()
                    heading_5 = Button(frame11, text="View Customers", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=view_cust)
                    heading_5.place(x=470, y=250)
                    def supp():
                        try:
                            sql1 = '''CREATE VIEW SUPPLIER_DETAILS AS
                                    SELECT SUPP_ID,COMPANY_NAME,EMAIL_ID,LOCALITY,CITY,STATE,COUNTRY,POSTAL_CODE,PHONE_NUMBER
                                    FROM SUPPLIER,SUPPLIER_INFORMATION WHERE SUPPLIER.SUPP_ID = SUPPLIER_INFORMATION.PERSONAL_ID;'''
                            cur.execute(sql1)
                        except:
                            pass
                        frame12 = Frame(master1, bg="#FFDCE7")
                        heading2 = Label(frame12, bg="deep sky blue", height=80, width=240, relief="raised", borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        tree = Treeview(frame12,selectmode ='browse')
                        tree["columns"] = ("one", "two", "three", "four", "five", "six", "seven","eight","nine")
                        tree.column("one", width=100)
                        tree.column("two", width=100)
                        tree.column("three", width=140)
                        tree.column("four", width=140)
                        tree.column("five", width=100)
                        tree.column("six", width=100)
                        tree.column("seven", width=100)
                        tree.column("eight", width=90)
                        tree.column("nine", width=100)
                        tree.column("#0", anchor="w",width=0)
                        tree.heading("one", text='Supplier ID', anchor='w')
                        tree.heading("two", text="Company Name")
                        tree.heading("three", text="Email Address")
                        tree.heading("four", text="Locality")
                        tree.heading("five", text="City")
                        tree.heading("six", text="State")
                        tree.heading("seven", text="Country")
                        tree.heading("eight", text = "Postal Code")
                        tree.heading("nine", text = "Contact")
                        cur.execute("SELECT * FROM SUPPLIER_DETAILS;")
                        f = cur.fetchall()
                        for i in f:
                            tree.insert("", tk.END, values=(i[0],i[1], i[2], i[3], i[4], i[5], i[6], i[7],i[8]))
                        tree.place(x=152, y=240)
                        scrollbar = Scrollbar(frame12,orient = tk.VERTICAL, command = tree.yview)
                        tree.configure(yscrollcommand = scrollbar.set)
                        scrollbar.pack(side='right',fill='y')

                        def but_112():
                            frame11.pack(side="top", fill="both")
                            frame12.forget()

                        button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                           font=("Arial", 14), command=but_112)
                        button_10.place(x=650, y=580)
                        frame12.pack(side="top", fill="both")
                        frame11.forget()
                    heading14 = Button(frame11, text="View Suppliers", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=supp)
                    heading14.place(x=470, y=300)
                    def ship():
                        try:
                            sql1 = '''CREATE VIEW SHIPPER_DETAILS AS
                                    SELECT SHIP_ID,COMPANY_NAME,PHONE_NUMBER
                                    FROM SHIPPER;'''
                            cur.execute(sql1)
                        except:
                            pass
                        frame12 = Frame(master1, bg="#FFDCE7")
                        heading2 = Label(frame12, bg="deep sky blue", height=80, width=80, relief="raised", borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        tree = Treeview(frame12,selectmode ='browse')
                        tree["columns"] = ("one", "two", "three")
                        tree.column("one", width=140)
                        tree.column("two", width=140)
                        tree.column("three", width=140)
                        tree.column("#0", anchor="w",width=0)
                        tree.heading("one", text='Shipper ID', anchor='w')
                        tree.heading("two", text="Company Name")
                        tree.heading("three", text="Phone Number")
                        cur.execute("SELECT * FROM SHIPPER_DETAILS;")
                        f = cur.fetchall()
                        for i in f:
                            tree.insert("", tk.END, values=(i[0],i[1], i[2]))
                        tree.place(x=422, y=240)
                        scrollbar = Scrollbar(frame12,orient = tk.VERTICAL, command = tree.yview)
                        tree.configure(yscrollcommand = scrollbar.set)
                        scrollbar.pack(side='right',fill='y')

                        def but_1112():
                            frame11.pack(side="top", fill="both")
                            frame12.forget()

                        button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                           font=("Arial", 14), command=but_1112)
                        button_10.place(x=650, y=580)
                        frame12.pack(side="top", fill="both")
                        frame11.forget()
                    heading114 = Button(frame11, text="View Shippers", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=ship)
                    heading114.place(x=470, y=350)
                    def prod():
                        try:
                            sql1 = '''CREATE VIEW PRODUCT_1 AS
                            SELECT distinct P.PRODUCT_ID,PRODUCT_NAME,PRODUCT_QUANTITY,UNIT_PRICE,UNIT_WEIGHT,
                            S.COMPANY_NAME, C.CATEGORY_NAME
                            FROM REVIEW AS R, SUPPLIER AS S, PRODUCT AS P, CATEGORY AS C, SUPPLIES AS Q
                            WHERE P.Product_ID = Q.product_ID and s.supp_id = q.supp_id AND C.CATEGORY_ID = P.CATEGORY_ID
                            order by p.product_id;'''
                            cur.execute(sql1)

                            sql2 = '''create view product_2 as 
                            (Select p1.product_id, avg(rating) as reviews from review r1, product p1 where r1.product_id = p1.product_id
                            group by p1.product_id);'''
                            cur.execute(sql2)

                            sql3 = '''create view product_details as
                            select product_1.PRODUCT_ID,PRODUCT_NAME,PRODUCT_QUANTITY,UNIT_PRICE,UNIT_WEIGHT,
                            COMPANY_NAME, CATEGORY_NAME, reviews from product_1,product_2
                            where product_1.product_id = product_2.product_id
                            order by product_id;'''
                            cur.execute(sql3)
                        except:
                            pass
                        frame12 = Frame(master1, bg="#FFDCE7")
                        heading2 = Label(frame12, bg="deep sky blue", height=80, width=200, relief="raised", borderwidth=3)
                        heading2.config(highlightbackground="purple", highlightthickness=2)
                        label_2 = Label(frame12, bg="yellow", height=6, width=30, relief="raised")
                        label_2.place(x=1000, y=40)
                        label = Label(frame12, text="Hello, " + "John", fg="dark green", bg="white", width=15,
                                      font=("Arial", 14))
                        label.place(x=1020, y=70)
                        heading2.pack(padx=150, pady=170)
                        tree = Treeview(frame12,selectmode ='browse')
                        tree["columns"] = ("one", "two", "three","four","five","six","seven","eight")
                        tree.column("one", width=140)
                        tree.column("two", width=140)
                        tree.column("three", width=140)
                        tree.column("four", width=140)
                        tree.column("five", width=140)
                        tree.column("six", width=140)
                        tree.column("seven", width=140)
                        tree.column("eight", width=140)
                        tree.column("#0", anchor="w",width=0)
                        tree.heading("one", text='Product ID', anchor='w')
                        tree.heading("two", text="Name")
                        tree.heading("three", text="Quantity")
                        tree.heading("four", text="Price")
                        tree.heading("five", text="Weight")
                        tree.heading("six", text="Company")
                        tree.heading("seven", text="Category")
                        tree.heading("eight", text="Avg Rating")
                        cur.execute("SELECT * FROM PRODUCT_DETAILS;")
                        f = cur.fetchall()
                        for i in f:
                            tree.insert("", tk.END, values=(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))
                        tree.place(x=80, y=240)
                        scrollbar = Scrollbar(frame12,orient = tk.VERTICAL, command = tree.yview)
                        tree.configure(yscrollcommand = scrollbar.set)
                        scrollbar.pack(side='right',fill='y')

                        def but_1112():
                            frame11.pack(side="top", fill="both")
                            frame12.forget()

                        button_10 = Button(frame12, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                           font=("Arial", 14), command=but_1112)
                        button_10.place(x=650, y=580)
                        frame12.pack(side="top", fill="both")
                        frame11.forget()
                    heading4 = Button(frame11, text="View Products", bg="IndianRed1", height=2, width=30,
                                      font=("Arial", 14), command=prod)
                    heading4.place(x=470, y=400)

                    def but_10():
                        frame7.pack(side="top", fill="both")
                        frame11.forget()

                    button_10 = Button(frame11, text="Back", bg="orange", bd=2, relief="groove", height=2, width=9,
                                       font=("Arial", 14), command=but_10)
                    button_10.place(x=650, y=580)
                    frame11.pack(side="top", fill="both")
                    frame7.forget()
                heading4 = Button(frame7, text="View Stakeholders", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=view_stake)
                heading4.place(x=470, y=330)
                def view_sales():
                    pass
                heading5 = Button(frame7, text="View Sales", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=view_sales)
                heading5.place(x=470, y=380)
                def upd_ent():
                    pass
                heading6 = Button(frame7, text="Update Entities", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=upd_ent)
                heading6.place(x=470, y=430)
                def place_ord():
                    pass
                heading7 = Button(frame7, text="Place Order for Supplies", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=place_ord)
                heading7.place(x=470, y=480)
                def butt_10():
                    frame4.pack(side="top", fill="both")
                    frame7.forget()
                def del_ent():
                    pass
                heading8 = Button(frame7, text="Delete Entities", bg="IndianRed1", height=2, width=30,
                                  font=("Arial", 14), command=del_ent)
                heading8.place(x=870, y=380)
                button_10 = Button(frame7, text="Logout", bg="orange", bd=2, relief="groove", height=2, width=9,
                                   font=("Arial", 15), command=butt_10)
                button_10.place(x=600, y=570)
                frame7.pack(side="top", fill="both")
                frame4.forget()

            def back1():
                frame1.pack(side = "top", fill = "both")
                frame4.forget()
            def callbac1():
                frame_employee(master_new)
                list_emp.append("John")
                return
                passw = heading6_1.get()
                user = heading4_1.get()
                if user in dict_employee.keys() and passw in dict_employee.values() and dict_employee[user]==passw:
                    a = messagebox.askquestion("Success", "Would you like to continue?")
                    sql1 = '''SELECT FIRST_NAME FROM ADMINISTRATOR WHERE EMAIL_ID = (%s)'''
                    cur.execute(sql1,user)
                    rows = cur.fetchall()
                    for i in rows:
                        login_name = i[0]
                        list_emp.append(login_name)
                    if a == "yes":
                        messagebox.showinfo("Success", "You will be directed to the page in a short while")
                        frame_employee(master_new)
                        heading6_1.delete(first=0, last=100)
                        heading4_1.delete(first=0, last=100)
                    else:
                        heading6_1.delete(first=0, last=100)
                        heading4_1.delete(first=0, last=100)
                        back()
                        #('blythe_case7564@aol.net', 'NJJ74DHN7XA'),
                        # ('c.erickson6969@outlook.edu', 'IYL06VQE3DK'),
                        # ('hebertcharity5210@yahoo.in', 'BAY99IMX4JE')
                elif user in dict_employee.keys() and passw not in dict_employee.values():
                    messagebox.askokcancel("Error", "Enter the correct details")
                    heading6_1.delete(first=0, last=100)
                    heading4_1.delete(first=0, last=100)
                elif user not in dict_employee.keys() and passw in dict_employee.values():
                    messagebox.askokcancel("Error", "Enter the correct details")
                    heading6_1.delete(first=0, last=100)
                    heading4_1.delete(first=0, last=100)
                else:
                    messagebox.askokcancel("Error", "Enter the correct details")
                    heading6_1.delete(first=0, last=100)
                    heading4_1.delete(first=0, last=100)

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
                sql = "SELECT CUST_ID from CUSTOMER;"
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
                    return True
                elif name.isdigit() == True:
                    ent1.delete(first=0, last=100)
                    return False
                elif name.isalnum() == True:
                    ent1.delete(first=0, last=100)
                    return False
            def chk_lname():  # validating name
                name = str(ent2.get())
                if name.isalpha() == True:
                    return True
                elif name.isdigit() == True:
                    ent2.delete(first=0, last=100)
                    return False
                elif name.isalnum() == True:
                    ent2.delete(first=0, last=100)
                    return False
            # but = Button(frame5, text="Save", fg="red", command=chk_fname)
            # but.place(x=930, y=210)
            heading5 = Label(frame5, text="Last Name", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
            heading5.place(x=320, y=280)
            lab2 = Label(frame5, bg="IndianRed1", height=5, width=30, relief="groove")
            lab2.place(x=670, y=280)
            ent2 = Entry(frame5, textvariable=2, width=30)
            ent2.place(x=685, y=310)

            # but1 = Button(frame5, text="Save", fg="red", command=chk_lname)
            # but1.place(x=930, y=310)
            heading8 = Label(frame5, text="Email Address", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
            heading8.place(x=320, y=380)
            lab3 = Label(frame5, bg="IndianRed1", height=5, width=30, relief="groove")
            lab3.place(x=670, y=380)
            ent3 = Entry(frame5, textvariable=3, width=30)
            ent3.place(x=685, y=410)

            def chk_email():  # validating grade
                grad = str(ent3.get())
                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                if (re.fullmatch(regex,grad)):
                    return True
                else:
                    ent3.delete(first=0, last=100)
                    return False
            #
            # but2 = Button(frame5, text="Save", fg="red", command=chk_email)
            # but2.place(x=930, y=410)
            heading6 = Label(frame5, text="Password", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
            heading6.place(x=320, y=480)
            lab4 = Label(frame5, bg="IndianRed1", height=5, width=30, relief="groove")
            lab4.place(x=670, y=480)
            ent4 = Entry(frame5, textvariable=4, width=30,show="<>")
            ent4.place(x=685, y=510)

            def chk_dob():  # validating date of birth
                dob = str(ent4.get())
                if len(dob)<1:
                    ent4.delete(first=0, last=100)
                    return False
                else:
                    return True

            # but3 = Button(frame5, text="Save", fg="red", command=chk_dob)
            # but3.place(x=930, y=510)

            def frame_cust_details(master1):
                frame6 = Frame(master_new, bg="#FFDCE7")
                heading2 = Label(frame6, bg="deep sky blue", height=40, width=200, relief="raised", borderwidth=3)
                heading2.config(highlightbackground="purple", highlightthickness=2)
                heading2.pack(padx=50, pady=150)
                heading3 = Label(frame6, text="Locality", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
                heading3.place(x=70, y=180)
                lab1 = Label(frame6, bg="IndianRed1", height=5, width=30, relief="groove")
                lab1.place(x=420, y=180)
                ent1 = Entry(frame6, textvariable=1, width=30)
                ent1.place(x=435, y=210)
                heading5 = Label(frame6, text="City", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
                heading5.place(x=70, y=280)
                lab2 = Label(frame6, bg="IndianRed1", height=5, width=30, relief="groove")
                lab2.place(x=420, y=280)
                ent2 = Entry(frame6, textvariable=2, width=30)
                ent2.place(x=435, y=310)
                heading8 = Label(frame6, text="State", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
                heading8.place(x=70, y=380)
                lab3 = Label(frame6, bg="IndianRed1", height=5, width=30, relief="groove")
                lab3.place(x=420, y=380)
                ent3 = Entry(frame6, textvariable=3, width=30)
                ent3.place(x=435, y=410)
                heading6 = Label(frame6, text="Postal Code", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
                heading6.place(x=650, y=180)
                lab4 = Label(frame6, bg="IndianRed1", height=5, width=30, relief="groove")
                lab4.place(x=1000, y=180)
                ent4 = Entry(frame6, textvariable=4, width=30)
                ent4.place(x=1015, y=210)
                heading0 = Label(frame6, text="Country", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
                heading0.place(x=650, y=280)
                lab5 = Label(frame6, bg="IndianRed1", height=5, width=30, relief="groove")
                lab5.place(x=1000, y=280)
                ent5 = Entry(frame6, textvariable=5, width=30, show="<>")
                ent5.place(x=1015, y=310)
                heading01 = Label(frame6, text="Phone Number", bg="IndianRed1", height=3, width=20, font=("Arial", 18))
                heading01.place(x=650, y=380)
                lab6 = Label(frame6, bg="IndianRed1", height=5, width=30, relief="groove")
                lab6.place(x=1000, y=380)
                ent6 = Entry(frame6, textvariable=6, width=30, show="<>")
                ent6.place(x=1015, y=410)
                frame6.pack(side = "top", fill = "both")
                heading7 = Button(frame6, text="Next", bg="orange", bd=2, relief="groove", height=2, width=7,
                                  font=("Arial", 15), command=check_details)
                heading7.place(x=600, y=500)

                def backk():
                    frame5.pack(side="top", fill="both")
                    frame6.forget()

                heading_7 = Button(frame6, text="Back", bg="orange", bd=2, relief="groove", height=2, width=7,
                                   font=("Arial", 15), command=backk)
                heading_7.place(x=750, y=500)
                frame5.forget()
            def check_details():
                # c = 0
                # if (chk_fname()!=True):
                #     ent1.delete(first=0, last=100)
                #     c = 1
                # if (chk_lname()!=True):
                #     ent2.delete(first=0, last=100)
                #     c = 1
                # if (chk_email()!=True):
                #     ent3.delete(first=0, last=100)
                #     c = 1
                # if (chk_dob()!=True):
                #     c = 1
                #     ent4.delete(first=0, last=100)
                # if (c==1):
                #     messagebox.askokcancel("Error", "Enter Correctly!", parent=frame5)
                # else:
                    messagebox.showinfo("Success","Data Saved!",parent = frame5)
                    ent1.delete(first=0, last=100)
                    ent2.delete(first=0, last=100)
                    ent3.delete(first=0, last=100)
                    ent4.delete(first=0, last=100)
                    frame_cust_details(master_new)
                    c_id = chk_adm()
                    print(c_id)
                    fname = ent1.get()
                    lname, email, passw = ent2.get(), ent3.get(), str(ent4.get())
                    cur = mydb.cursor()
                    sql = 'INSERT INTO CUSTOMER values(%s,%s,%s,%s,%s);'
                    val = (c_id,email,fname,lname,passw)
                    # cur.execute(sql, val)
                    mydb.commit()
                    print("Data added")
            heading7 = Button(frame5, text="Next", bg="orange", bd=2, relief="groove", height=2, width=7,
                              font=("Arial", 15), command=check_details)
            heading7.place(x=600, y=600)

            def backk():
                frame1.pack(side = "top", fill = "both")
                frame5.forget()
            heading_7 = Button(frame5, text="Back", bg="orange", bd=2, relief="groove", height=2, width=7,
                              font=("Arial", 15), command=backk)
            heading_7.place(x=750, y=600)
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

