from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello_world():
    redis.incr('hits')
    return 'Hey, we have Flask in a Docker container! TEST 5!!!!! Hits: %s' % redis.get('hits')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')