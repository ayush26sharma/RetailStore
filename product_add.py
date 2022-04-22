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
    l = read_csv('admin_pro.csv')
    x = 100;
    y = 0
    for i in l:
        admin = i[1]
        prod = i[2]
        sql = 'INSERT INTO adds_product values(%s,%s);'
        val = (admin,prod)
        print(val)
        cur.execute(sql, val)
        mydb.commit()