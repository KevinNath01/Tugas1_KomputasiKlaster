from flask.app import Flask
from flask.templating import render_template
from flask import request
from sql_helper import detail_siswa
app = Flask(__name__)

res = detail_siswa()

@app.route("/")
def index():
    page = request.args.get('page', 0, type=int)
    return render_template('index.html', res=res, enumerate=enumerate, page=page)