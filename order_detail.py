import pymysql as pm
import csv

def read_csv(filename):
    file = open(filename);
    csvreader = csv.reader(file);
    header = next(csvreader);
    print(header)
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    return rows

if __name__ == '__main__':
    mydb = pm.connect(host="localhost",  # setting up connection
                      user="root",
                      passwd="root",
                      database="retailstore")
    print("Connection is successful")
    cur = mydb.cursor();
    l = read_csv('order_details.csv')
    x = 100;
    y = 0
    for i in l:
        id = i[1]
        y+=1
        pid = i[2]
        quantity = int(i[4])
        price = int(i[3])
        discount = int(i[5])
        sql = 'INSERT INTO order_details values(%s,%s,%s,%s,%s);'
        val = (id,pid,quantity,price,discount)
        print(val)
        cur.execute(sql, val)
        mydb.commit()