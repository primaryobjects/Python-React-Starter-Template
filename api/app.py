from time import gmtime, strftime
from flask import Flask

app = Flask(__name__)

@app.route('/api')
def index():
  return { 'message': 'Hello World!' }

@app.route('/time')
def time():
  return { 'time': strftime('%a, %d %b %Y %H:%M:%S +0000', gmtime()) }