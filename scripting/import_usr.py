from mysql.connector import Error
import mysql.connector as msql
import pandas as pd
import os

import pandas as pd
csv = os.getcwd() + "\\user.csv"
empdata = pd.read_csv(csv, index_col=False, delimiter=',')
empdata.head()
print(empdata)
# print(df)

try:
    conn = msql.connect(host='localhost', user='root',
                        password='')  # give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
except Error as e:
    print("Error while connecting to MySQL", e)

try:
    conn = msql.connect(host='localhost', database='kluster',
                        user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS siswa;')
        print('Creating table....')
        cursor.execute(
            "CREATE TABLE siswa(id_siswa int(11),id_kota int(11),nisn varchar(255),nama_siswa varchar(255))")
        print("Table is created....")
        for i, row in empdata.iterrows():
            sql = "INSERT INTO kluster.siswa VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # print("Record inserted")
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
