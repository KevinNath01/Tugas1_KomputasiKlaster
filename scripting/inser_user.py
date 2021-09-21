
import names
import random
import string
import pandas as pd
import csv
'''
hati hati hasilnya bisa bergiga giga
'''

df = pd.DataFrame(columns=['id_siswa', 'id_kota', 'nis', 'nama_siswa'])
print(df.head())

head = ['id_siswa', 'id_kota', 'nis', 'nama_siswa']
# 05311840000039
idsis = 0
with open("jawaban1.csv", 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(head)
    for i in range(1, 39):
        for j in range(1, 13158):
            # i = str(i)
            i = str(i).rjust(2, "0")
            j = str(j).rjust(12, "0")
            nama = names.get_full_name()
            idsis += 1
            nis = f"{i}{j}"
            # df.loc[idsis] = [idsis] + [i]+[nis] + [nama]
            fields = [idsis, i, nis, nama]
            csvwriter.writerow(fields)

# df.to_csv("user.csv", index=False)
