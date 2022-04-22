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
    l = read_csv('suppliers.csv')
    x = 100;
    y = 0
    for i in l:
        id = "S" + str(x+y)
        y+=1
        email = i[2]
        company_name = i[1]
        sql = 'INSERT INTO supplier values(%s,%s,%s);'
        val = (id,email,company_name)
        print(val)
        cur.execute(sql, val)
        mydb.commit()