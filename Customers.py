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
    l = read_csv('customers.csv')
    x = 100;
    y = 0
    for i in l:
        id = i[0][0].upper() + str(x+y)
        y+=1
        fname = i[1]
        lname = i[2]
        email = i[3]
        password = i[4]
        sql = 'INSERT INTO customer values(%s,%s,%s,%s,%s);'
        val = (id,email,fname,lname,password)
        print(val)
        cur.execute(sql, val)
        mydb.commit()



