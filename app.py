import os

from flask import Flask
from redis import Redis
from flask_mysqldb import MySQL

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

# MySQL configurations
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'database'
app.config['MYSQL_HOST'] = 'mysql'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    redis.incr('hits')
    return 'Hey, we have Flask in a Docker container! Host: %s. TEST 7!!!!! Hits: %s' % \
        (os.environ.get('HOSTNAME'), redis.get('hits'))

@app.route('/versions')
def users():
    cur = mysql.connection.cursor()
    cur.execute('SHOW VARIABLES LIKE "%version%";')
    rv = cur.fetchall()
    return str(rv)
