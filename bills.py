import pymysql as pm
import csv

def read_csv(filename):
    file = open(filename);
    csvreader = csv.reader(file);
    rows = []
    for row in csvreader:
        rows.append(row)
    file.close()
    return rows

if __name__ == '__main__':
    mydb = pm.connect(host="localhost",  # setting up connection
                      user="root",
                      passwd="root",
                      database="midsem")
    print("Connection is successful")
    cur = mydb.cursor();
    l = read_csv('status.csv')
    x = 100;
    y = 0
    for i in l:
        p1 = i[0]
        p2 = i[1]
        p3 = i[2]
        print(p1)

        sql = 'INSERT INTO citi_status values(%s,%s,%s);'
        val = (p1,p2,p3)
        print(val)
        cur.execute(sql, val)
        mydb.commit()