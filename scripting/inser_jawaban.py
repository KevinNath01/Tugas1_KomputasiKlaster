import random
import pandas as pd
import csv
'''
hati hati hasilnya bisa bergiga giga
'''

df = pd.DataFrame(columns=['id_jawaban', 'id_siswa',
                           'id_soal', 'pilihan_jawaban'])
print(df.head())

head = ['id_jawaban', 'id_siswa',
        'id_soal', 'pilihan_jawaban']

'''
siswa enek 500rb
soal enek 7*40 -> 280
berarti jawaban enek 500rb * 280 = akeh

'''
idjaw = 0
with open("jawaban1.csv", 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(head)
    for i in range(1, 500001):
        for j in range(1, 281):
            pilihan_jawaban = nama = ''.join(random.choice("ABCD"))
            idjaw += 1
            # print(f"{idjaw},{i},{j},{pilihan_jawaban}")
            # df.loc[idjaw] = [idjaw] + [i]+[j] + [pilihan_jawaban]
            fields = [idjaw, i, j, pilihan_jawaban]
            csvwriter.writerow(fields)

# df.to_csv("jawaban.csv", index=False)
