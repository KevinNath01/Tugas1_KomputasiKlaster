from mysql.connector import Error
import mysql.connector as msql
import pandas as pd
import os

import pandas as pd
csv = os.getcwd() + "\\soal.csv"
data = pd.read_csv(csv, index_col=False)
empdata = pd.DataFrame(
    data, columns=['id_soal', 'id_mapel', 'nomor_soal', 'kunci_jawaban'])
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

try:
    conn = msql.connect(host='localhost', database='kluster',
                        user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS soal;')
        print('Creating table....')
        cursor.execute(
            "CREATE TABLE soal(id_soal int(11),id_mapel int(11),nomor_soal int(11),kunci_jawaban varchar(255))")
        print("Table is created....")
        for i, row in empdata.iterrows():
            sql = "INSERT INTO kluster.soal VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
