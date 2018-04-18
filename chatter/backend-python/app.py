import flask
import pymysql
import pymysql.cursors

app = flask.Flask(__name__)
database = pymysql.connect(
    user='root',
    password='testpass',
    host='db',
    db='chatter',
)

@app.route('/test')
def test():
    with database.cursor() as cur:
        cur.execute("SELECT col FROM test;")
        result, = cur.fetchone()
        return flask.jsonify({
            'result': result,
            'backend': 'python',
        })
