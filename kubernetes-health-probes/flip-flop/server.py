import time
from flask import Flask
import os

app = Flask(__name__)

def valid_time():
    return int(time.time()) % 100 > 50

@app.route('/')
def index():
    if valid_time():
        return "Hello!  This app is up and running!"
    
    return Flask.Response('NOT OK', status=500)

@app.route('/healthcheck')
def healthcheck():
    if valid_time():
        return "OK"
    return Flask.Response('NOT OK', status=500)

app.run(host='0.0.0.0', port=8000)