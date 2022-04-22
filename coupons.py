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
    l = read_csv('coupons.csv')
    x = 100;
    y = 0
    for i in l:
        id = i[0]
        y+=1
        method = i[1]
        disc = int(i[2])
        sql = 'INSERT INTO coupons values(%s,%s,%s);'
        val = (id,method,disc)
        print(val)
        cur.execute(sql, val)
        mydb.commit()