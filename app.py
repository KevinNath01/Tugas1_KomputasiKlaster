from flask.app import Flask
from flask.templating import render_template
from flask import request
from sql_helper import select_nilai, detail_siswa

app = Flask(__name__)

rows = []
res = select_nilai()
mapel = ["Matematika", "Fisika", "Biologi", "Bahasa Indonesia", "Bahasa Inggris", "Sejarah", "Kimia"]
for i in range(len(res)//7):
    nama, nrp, kota = (detail_siswa(i + 1))
    nrp = nrp.rjust(14, '0')
    rows.append([nama, nrp, kota])
    row = res[i:i+7]
    _, nilai, _ = zip(*row)
    nilai = list(map(float, nilai))
    rows[i].append(nilai)

@app.route("/")
def index():
    page = request.args.get('page', 0, type=int)
    return render_template('index.html', rows=rows, mapel=mapel, enumerate=enumerate, page=page)
