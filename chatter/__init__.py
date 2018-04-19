import os
import sqlite3
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

_basedir = os.path.abspath(os.path.dirname(__file__))
db_file  = 'sqlite:///' + os.path.join(_basedir, 'chatter.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Test(db.Model):
    col = db.Column(db.String(10), primary_key=True)

db.create_all()
try:
    t = Test(col="ok")
    db.session.add(t)
    db.session.commit()
except Exception as e:
    pass

@app.route('/test')
def test():
    #import pdb; pdb.set_trace()
    #from chatter.models import Test
    result = Test.query.all()[0].col
    return jsonify({
        'result': result,
        'backend': 'python',
    })
