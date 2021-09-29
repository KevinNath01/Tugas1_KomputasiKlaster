import mysql.connector as msql
from mysql.connector import Error
import time
try:
    conn = msql.connect(host='localhost', database='kluster',
                        user='root', password='')
    if conn.is_connected():
        cursor = conn.cursor(buffered=True)
        idnilai = 0
        start = time.perf_counter()
        for i in range(1, 24547):
            idnilai += 1
            query = f"SELECT SUM(`jawaban`.`pilihan_jawaban`=`soal`.`kunci_jawaban`)*2.5 AS nilai FROM `soal` INNER JOIN `jawaban` ON `soal`.`id_soal` = `jawaban`.`id_soal` INNER JOIN `mapel` ON `soal`.`id_mapel` = `mapel`.`id_mapel` WHERE `jawaban`.`id_siswa`={i} GROUP BY `soal`.`id_mapel`;"
            cursor.execute(query)
            res = cursor.fetchall()
            conn.commit()
            perid1 = [idnilai, i, 1, res[0][0]]
            perid2 = [idnilai+1, i, 2, res[1][0]]
            perid3 = [idnilai+2, i, 3, res[2][0]]
            perid4 = [idnilai+3, i, 4, res[3][0]]
            perid5 = [idnilai+4, i, 5, res[4][0]]
            perid6 = [idnilai+5, i, 6, res[5][0]]
            perid7 = [idnilai+6, i, 7, res[6][0]]
            # fields = [, res[1][0], res[2][0], res[3][0]]
            sql = "INSERT INTO kluster.nilai VALUES ( %s, %s, %s, %s)"
            cursor.execute(sql, perid1)
            cursor.execute(sql, perid2)
            cursor.execute(sql, perid3)
            cursor.execute(sql, perid4)
            cursor.execute(sql, perid5)
            cursor.execute(sql, perid6)
            cursor.execute(sql, perid7)
            idnilai += 6
            # print("res", (res[0][0]))
            # print("type", type(res))
        end = time.perf_counter()
        diff = end - start
        print(f'Finished in {diff} s')

except Error as e:
    print("Error while connecting to MySQL", e)