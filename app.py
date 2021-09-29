from flask.app import Flask
from flask.templating import render_template
from flask import request
from sql_helper import detail_siswa
app = Flask(__name__)

res = detail_siswa()

ms = {
    'matematika': 4,
    'fisika': 5,
    'biologi': 6,
    'bahasa indonesia': 7,
    'bahasa inggris': 8,
    'sejarah': 9,
    'kimia': 10
}

qs = {
    '>': lambda m, n: list(filter(lambda x: x[ms[m]] > n, res)),
    '<': lambda m, n: list(filter(lambda x: x[ms[m]] < n, res)),
    '=': lambda m, n: list(filter(lambda x: x[ms[m]] == n, res)),
    '>=': lambda m, n: list(filter(lambda x: x[ms[m]] >= n, res)),
    '<=': lambda m, n: list(filter(lambda x: x[ms[m]] <= n, res)),
}

@app.route("/")
def index():
    page = request.args.get('page', 0, type=int)
    return render_template('index.html', res=res, enumerate=enumerate, page=page)

@app.route("/filter")
def filter_page():
    mapel = request.args.get('mapel', 'matematika', type=str).strip().lower()
    symbol = request.args.get('symbol', '>', type=str).strip().lower()
    nilai = request.args.get('nilai', 0, type=int)
    page = request.args.get('page', 0, type=int)

    if mapel not in ms.keys():
        return 'error mapel'

    if symbol not in qs.keys():
        return 'error symbol'

    return render_template('index.html', res=qs[symbol](mapel, nilai), page=page, enumerate=enumerate)