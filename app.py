import os
import random

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
    return 'Hey, we have Flask in a Docker container! Host: %s. UPDATE 11! Hits: %s' % \
        (os.environ.get('HOSTNAME'), redis.get('hits'))


@app.route('/insert', methods=['GET'])
def insert_test():
    rnd = random.randint(1, 10)
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Test VALUES ('%s')" % rnd)
    mysql.connection.commit()
    return 'Inserted %s into the database!' % rnd


@app.route('/list', methods=['GET'])
def list_test():
    cur = mysql.connection.cursor()
    cur.execute('SELECT test FROM Test')
    rv = cur.fetchall()
    return str(rv)
