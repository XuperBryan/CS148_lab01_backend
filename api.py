import time
from flask import Flask

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/')
def index():
  return "<h1>Welcome to our server!</h1>"