from flask import *
app = Flask(__name__)

HOST,PORT = '0.0.0.0',8888
DEBUG_MODE = True

index_html = '''
<html>
<body>
<a>hello</a>
</body>
</html>
'''
login_html = '''
<html>
<body>
<a>this is login page</a>
</body>
</html>
'''

@app.route("/")
def index():
  return render_template_string(index_html)

@app.route('/login')
def login():
  return render_template_string(login_html)

if __name__ == '__main__':
  app.run(host=HOST, port=PORT, debug=DEBUG_MODE)