import datetime

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
    l = read_csv('file19.csv')
    x = 100;
    y = 0
    for i in l:
        oid = i[1]
        y+=1
        bid = i[2]
        o_date = i[3]
        s_id = i[4]
        s_date = i[5]
        c_id = i[6]

        sql = 'INSERT INTO orders values(%s,%s,%s,%s,(%s),(%s));'
        val = (oid,bid,s_id,c_id,o_date,s_date)
        print(val)
        cur.execute(sql, val)
        mydb.commit()