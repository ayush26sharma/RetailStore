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
    l = read_csv('products.csv')
    x = 100;
    y = 0
    for i in l:
        id = i[0]
        y+=1
        pname = i[1]
        quantity = int(i[2])
        price = int(i[3])
        weight = int(i[4])
        discount = int(i[5])
        cat = i[6]
        sql = 'INSERT INTO product values(%s,%s,%s,%s,%s,%s,%s);'
        val = (id,pname,quantity,price,weight,discount,cat)
        print(val)
        cur.execute(sql, val)
        mydb.commit()