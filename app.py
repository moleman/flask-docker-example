import os

from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    redis.incr('hits')
    return 'Hey, we have Flask in a Docker container! Host: %s. TEST 5!!!!! Hits: %s' % \
        (os.environ.get('HOSTNAME'), redis.get('hits'))
