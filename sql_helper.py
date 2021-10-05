from mysql.connector import Error
import mysql.connector as msql

def select_detail_nilai(id_siswa):
    try:
        conn = msql.connect(host='localhost', user='root', password='')
        if conn.is_connected():
            cursor = conn.cursor()
    except Error as e:
        print("Error while connecting to MySQL", e)

    try:
        conn = msql.connect(host='localhost', database='kluster', user='root', password='')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(f"SELECT `mapel`.`nama_mapel`, SUM(`jawaban`.`pilihan_jawaban`=`soal`.`kunci_jawaban`)*2.5 AS nilai FROM `soal` INNER JOIN `jawaban` ON `soal`.`id_soal` = `jawaban`.`id_soal` INNER JOIN `mapel` ON `soal`.`id_mapel` = `mapel`.`id_mapel` WHERE `jawaban`.`id_siswa`={id_siswa} GROUP BY `soal`.`id_mapel`;")
            record = cursor.fetchall()
            return record
    except Error as e:
        print("Error while connecting to MySQL", e)

def select_nilai():
    try:
        conn = msql.connect(host='localhost', user='root', password='')
        if conn.is_connected():
            cursor = conn.cursor()
    except Error as e:
        print("Error while connecting to MySQL", e)

    try:
        conn = msql.connect(host='localhost', database='kluster', user='root', password='')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT MAX(CASE WHEN `query_nilai`.`id_mapel`=1 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_1, MAX(CASE WHEN `query_nilai`.`id_mapel`=2 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_2, MAX(CASE WHEN `query_nilai`.`id_mapel`=3 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_3, MAX(CASE WHEN `query_nilai`.`id_mapel`=4 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_4, MAX(CASE WHEN `query_nilai`.`id_mapel`=5 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_5, MAX(CASE WHEN `query_nilai`.`id_mapel`=6 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_6, MAX(CASE WHEN `query_nilai`.`id_mapel`=7 THEN `query_nilai`.`nilai` ELSE 0 END) AS mapel_7 FROM `query_nilai` GROUP BY `query_nilai`.`id_siswa`;")
            record = cursor.fetchall()
            return record
    except Error as e:
        print("Error while connecting to MySQL", e)

def detail_siswa():
    try:
        conn = msql.connect(host='localhost', user='root', password='')
        if conn.is_connected():
            cursor = conn.cursor()
    except Error as e:
        print("Error while connecting to MySQL", e)

    try:
        conn = msql.connect(host='localhost', database='kluster', user='root', password='')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute(f"SELECT `siswa`.`nama_siswa`, `siswa`.`nisn`, `kota`.`nama_kota` FROM `siswa` INNER JOIN `kota` ON `siswa`.`id_kota`=`kota`.`id_kota`;")
            record = cursor.fetchall()
            return record
    except Error as e:
        print("Error while connecting to MySQL", e)