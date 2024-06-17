from flask import *
app = Flask(__name__)

HOST,PORT = '0.0.0.0',8888
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

if __name__ == __main__:
  app.run(host=HOST, port=PORT)