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
    l = read_csv('sup_prod.csv')
    x = 100;
    y = 0
    for i in l:
        prod = i[1]
        sup = i[2]
        sql = 'INSERT INTO supplies values(%s,%s);'
        val = (sup,prod)
        print(val)
        cur.execute(sql, val)
        mydb.commit()