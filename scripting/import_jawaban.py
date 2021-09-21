from mysql.connector import Error
import mysql.connector as msql
import pandas as pd
import os

import pandas as pd
csv = os.getcwd() + "\\jawaban1.csv"
data = pd.read_csv(csv, index_col=False)
empdata = pd.DataFrame(
    data, columns=['id_jawaban', 'id_siswa',
                   'id_soal', 'pilihan_jawaban'])
empdata.head()
print(empdata.head())
# print(df)

try:
    conn = msql.connect(host='localhost', user='root',
                        password='')
    if conn.is_connected():
        cursor = conn.cursor()
except Error as e:
    print("Error while connecting to MySQL", e)

# empdata.to_sql("table", conn,  if_exists="append", index=False)
try:
    conn = msql.connect(host='localhost', database='kluster',
                        user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS jawaban;')
        print('Creating table....')
        cursor.execute(
            "CREATE TABLE jawaban(id_jawaban int(11),id_siswa int(11),id_soal int(11),pilihan_jawaban varchar(255))")
        print("Table is created....")
        for i, row in empdata.iterrows():
            sql = "INSERT INTO kluster.jawaban VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            # print("Record inserted")
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
