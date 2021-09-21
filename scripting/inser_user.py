
import names
import random
import string
import pandas as pd

'''
hati hati hasilnya bisa bergiga giga
'''

df = pd.DataFrame(columns=['id_siswa', 'id_kota', 'nis', 'nama_siswa'])
print(df.head())


# 05311840000039
idsis = 0
for i in range(1, 39):
    for j in range(1, 13158):
        i = str(i)
        i = i.rjust(2, "0")
        j = str(j).rjust(12, "0")
        nama = names.get_full_name()
        idsis += 1
        nis = f"{i}{j}"
        # print(f"{idsis},{i},{i}{j},{nama}")
        df.loc[idsis] = [idsis] + [i]+[nis] + [nama]
        # print(nama)

df.to_csv("user.csv", index=False)
