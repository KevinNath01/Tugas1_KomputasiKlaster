
import random
import string
import pandas as pd


df = pd.DataFrame(columns=['id_soal', 'id_mapel',
                           'nomor_soal', 'kunci_jawaban'])
print(df.head())

id_soal = 0
for i in range(1, 8):
    for j in range(1, 41):
        id_soal += 1
        jawaban = ''.join(random.choice("ABCD"))
        # print(f"{id_soal},{i},{j},{jawaban}")
        df.loc[id_soal] = [id_soal] + [i]+[j] + [jawaban]

# print(df.head())
df.to_csv("soal.csv", index=False)
