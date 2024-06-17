from flask import *
app = Flask(__name__)

index = '''
<a>hello</a>
'''
login = '''
<a>this is login page</a>
'''

@app.route("/")
def index():
  return index

@app.route('/login')
def login():
  return login
  