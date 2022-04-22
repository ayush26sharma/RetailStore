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
    l = read_csv('shippers.csv')
    x = 100;
    y = 0
    for i in l:
        id = "SH" + str(x+y)
        y+=1
        company = i[1]
        phone = i[2]
        sql = 'INSERT INTO shipper values(%s,%s,%s);'
        val = (id,phone,company)
        print(val)
        cur.execute(sql, val)
        mydb.commit()