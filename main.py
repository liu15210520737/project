from flask import *
import secrets, os, sys, base64, json
from flask_session import Session
from getpass import getpass
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
def generate_key(length):
  key = secrets.token_hex(length)  # 生成指定长度的随机十六进制字符串
  return key
def favicon_encoded(favicon_file_path):
    with open(favicon_file_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
config_file_path = os.path.join(current_directory, 'config.json')
if not os.path.exists(config_file_path):
  print('检测到配置文件不存在,请设定管理员账号密码')
  username = input('账号:')
  password = getpass('密码:')
  print('正在随机生成会话密钥')
  secret_key = generate_key(18)
  print('你的会话密钥为', secret_key)
  config_data = {
    'username' : username,
    'password' : generate_password_hash(password),
    'host' : '0.0.0.0',
    'port' : 8888,
    'debug' : False,
    'secret_key' : secret_key
  }
  print('正在写入配置文件')
  with open(config_file_path, 'w', encoding='utf-8') as f:
    json.dump(config_data, f, ensure_ascii=False, indent=4)
  print('设定成功')

with open(config_file_path, 'r', encoding='utf-8') as file:
  config_data = json.load(file)
HOST = config_data['host']
PORT = config_data['port']
DEBUG_MODE = config_data['debug']
username = config_data['username']
password_hash = config_data['password']
secret_key = config_data['secret_key']
#HOST,PORT = '0.0.0.0',8888
#DEBUG_MODE = True

# 设置密钥用于会话签名
app.config['SECRET_KEY'] = secret_key
# 设置会话类型为文件系统（或其他你选择的类型）
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
# 假设我们有一个管理员用户名和密码的字典
admin_credentials = {'username': username, 'password': password}

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
    if username == admin_credentials['username'] and check_password_hash(admin_credentials['password_hash'], password):
      # 如果匹配，将管理员标识放入会话
      session['admin_logged_in'] = True
      return redirect(url_for('panel'))
    else:
      # 如果不匹配，返回错误消息
      error = 'Invalid username or password'
      return redirect(url_for('error',back='login'))
    # 如果是 GET 请求，则渲染登录页面
  return render_template_string(login_html)

@app.route('/panel')
def panel():
  if 'admin_logged_in' in session and session['admin_logged_in']:
    return render_template_string(panel_html)
  else:
    return redirect(url_for('login'))

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
  print('默认服务器端口号为8888')
  app.run(host=HOST, port=PORT, debug=DEBUG_MODE)