from flask import *
import secrets, os, sys
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import base64

HOST,PORT = '0.0.0.0',8888
DEBUG_MODE = True

app = Flask(__name__)
def generate_key(length):
  key = secrets.token_hex(length)  # 生成指定长度的随机十六进制字符串
  return key
def favicon_encoded(favicon_file_path):
  with open(favicon_file_path, 'rb') as image_file:
    encoded_string = base64.ded_string = base64.b64encode(image_file.read()).decode('utf-8')
  return encoded_string

# 设置密钥用于会话签名
app.config['SECRET_KEY'] = 'your-secret-key'
# 设置会话类型为文件系统（或其他你选择的类型）
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
# 假设我们有一个管理员用户名和密码的字典
admin_credentials = {'username': 'admin', 'password': generate_password_hash('password123')}

index_html = '''
<html>
<body>
<a>hello</a>
</body>
</html>
'''
login_html = '''
<form action="/submit_data" method="post">
  <input type="text" name="username" placeholder="Username">
  <input type="password" name="password" placeholder="Password">
  <button type="submit">Submit</button>
</form>
'''

panel_html = '''
null
'''
error_404_html = '''
'''
error_500_html = '''
'''
error_html = '''
'''

@app.route('/')
def index():
  return render_template_string(index_html)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    # 检查用户名和密码是否匹配
    if username == admin_credentials['username'] and check_password_hash(admin_credentials['password'], password):
      # 如果匹配，将管理员标识放入会话
      session['admin_logged_in'] = True
      return redirect(url_for('admin_panel'))
    else:
      # 如果不匹配，返回错误消息
      error = 'Invalid username or password'
      return redirect(url_for('error',back='login'))
    # 如果是 GET 请求，则渲染登录页面
  return render_template_string(login_html)

@app.route('/panel')
def panel():
  return render_template_string(panel_html)

@app.route('/logout')
def logout():
    # 清除会话中的管理员标识
    session.pop('admin_logged_in', None)
    return redirect(url_for('login'))

@app.route('/error/<back>')
def error(back):
  return render_template_string(error_html, back=back)

@app.route('/404')
def error_404():
  return render_template_string(error_404_html)

@app.route('/500')
def error_500():
  return render_template_string(error_500_html)
if __name__ == '__main__':
  app.run(host=HOST, port=PORT, debug=DEBUG_MODE)