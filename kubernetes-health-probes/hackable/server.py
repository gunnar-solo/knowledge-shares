from flask import Flask
import os

app = Flask(__name__)

database_path = './DATABASE.db'

@app.route('/')
def index():
    return open(database_path, "r").read()

@app.route('/healthcheck')
def healthcheck():
    if os.path.exists(database_path):
        return 'OK'
    return Flask.Response('NOT OK', status=500)

@app.route('/hack')
def hack():
    os.remove(database_path)
    return 'You have hacked this webapp.  :('

app.run(host='0.0.0.0', port=8080)