from flask import Flask, render_template, request,session
from flask_sqlalchemy import SQLAlchemy
import json


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.config.update()
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)
class Table(db.Model):
    sno = db.Column(db.String(4), primary_key=True)
    segment = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(21), nullable=False)
    production = db.Column(db.String(120), nullable=False)
    year = db.Column(db.String(12), nullable=True)

@app.route("/")
def home():
    posts = Table.query.filter_by().all()
    return render_template('display.html', posts = posts )

app.run(debug=True)