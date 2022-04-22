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
    l = read_csv('file22.csv')
    x = 100;
    y = 0
    for i in l:
        oid = i[1]
        y+=1
        p1 = int(i[2])
        p2 = int(i[3])
        p3 = i[4]
        sql = 'INSERT INTO cart values(%s,%s,%s,%s);'
        val = (oid,p1,p2,p3)
        print(val)
        cur.execute(sql, val)
        mydb.commit()