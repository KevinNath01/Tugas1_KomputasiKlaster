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
            cursor.execute("SELECT `mapel`.`nama_mapel`, SUM(`jawaban`.`pilihan_jawaban`=`soal`.`kunci_jawaban`)*2.5 AS nilai, `jawaban`.`id_siswa` FROM `soal` INNER JOIN `jawaban` ON `soal`.`id_soal` = `jawaban`.`id_soal` INNER JOIN `mapel` ON `soal`.`id_mapel` = `mapel`.`id_mapel` GROUP BY  `jawaban`.`id_siswa`, `soal`.`id_mapel`;")
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
            cursor.execute(f"SELECT `nilai`.`id_siswa`,`siswa`.`nama_siswa`,`siswa`.`nisn`,`kota`.`nama_kota`,MAX(CASE WHEN `nilai`.`id_mapel`='1' THEN `nilai`.`nilai` END) 'Matematika',MAX(CASE WHEN `nilai`.`id_mapel`='2' THEN `nilai`.`nilai` END) 'Fisika',MAX(CASE WHEN `nilai`.`id_mapel`='3' THEN `nilai`.`nilai` END) 'Biologi',MAX(CASE WHEN `nilai`.`id_mapel`='3' THEN `nilai`.`nilai` END) 'Bahasa Indonesia',MAX(CASE WHEN `nilai`.`id_mapel`='3' THEN `nilai`.`nilai` END) 'Bahasa Inggris',MAX(CASE WHEN `nilai`.`id_mapel`='3' THEN `nilai`.`nilai` END) 'Sejarah',MAX(CASE WHEN `nilai`.`id_mapel`='3' THEN `nilai`.`nilai` END) 'Kimia' FROM nilai INNER JOIN `siswa` ON `siswa`.`id_siswa` = `nilai`.`id_siswa` INNER JOIN `kota` ON `kota`.`id_kota`= `siswa`.`id_kota` GROUP BY `nilai`.`id_siswa`;")
            record = cursor.fetchall()
            return record
    except Error as e:
        print("Error while connecting to MySQL", e)