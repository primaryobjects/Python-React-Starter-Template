from time import gmtime, strftime
from flask import Flask

app = Flask(__name__, static_folder='../build', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api')
def hello():
  return { 'message': 'Hello World!' }

@app.route('/api/time')
def time():
  return { 'time': strftime('%a, %d %b %Y %H:%M:%S +0000', gmtime()) }