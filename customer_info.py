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
    l = read_csv('cust_info.csv')
    x = 100;
    y = 0
    for i in l:
        if (y>=100):
            id = "C" + str(y)
        else:
            id = "C" + str(x+y)
        y+=1
        locality = i[1]
        city = i[2]
        state = i[3]
        country = i[4]
        zipcode = i[5]
        phone = i[6]

        sql = 'INSERT INTO customer_information values(%s,%s,%s,%s,%s,%s,%s);'
        val = (id,locality,city,state,country,zipcode,phone)
        print(val)
        cur.execute(sql, val)
        mydb.commit()

