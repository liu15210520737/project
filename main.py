from flask import *
app = Flask(__name__)

HOST,PORT = '0.0.0.0',8888

index_html = '''

<a>hello</a>
'''
login_html = '''
<a>this is login page</a>
'''

@app.route("/")
def index():
  return render_template_string(index_html)

@app.route('/login')
def login():
  return render_template_string(login_html)

if __name__ == '__main__':
  app.run(host=HOST, port=PORT)           