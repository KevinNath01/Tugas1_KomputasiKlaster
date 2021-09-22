from flask.app import Flask
from flask.templating import render_template
from sql_helper import select_nilai, detail_siswa

app = Flask(__name__)

@app.route("/")
def index():
    rows = []
    res = select_nilai()
    mapel = ["Matematika", "Fisika", "Biologi", "Bahasa Indonesia", "Bahasa Inggris", "Sejarah", "Kimia"]
    for i in range(len(res)//7):
        rows.append(list(detail_siswa(i+1)))
        row = res[i:i+7]
        _, nilai, _ = zip(*row)
        nilai = list(map(float, nilai))
        rows[i].append(nilai)
    return render_template('index.html', rows=rows, mapel=mapel, enumerate=enumerate)
