from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Sess            ion  # 需要安装 flask-session 来支持会话
import os
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# 设置密钥用于会话签名
app.config['SECRET_KEY'] = 'your-secret-key'

# 设置会话类型为文件系统（或其他你选择的类型）
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# 假设我们有一个管理员用户名和密码的字典（在真实应用中，这应该在数据库中）
admin_credentials = {'username': 'admin', 'password': generate_password_hash('password123', method='sha256')}

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
            return render_template('login.html', error=error)
    
    # 如果是 GET 请求，则渲染登录页面
    return render_template('login.html')

@app.route('/admin')
def admin_panel():
    # 检查管理员是否已登录
    if 'admin_logged_in' not in session:
        return redirect(url_for('login'))
    
    # 如果已登录，显示管理员面板
    return render_template('admin_panel.html')

@app.route('/logout')
def logout():
    # 清除会话中的管理员标识
    session.pop('admin_logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    # 确保在运行时有一个指向模板文件夹的路径
    app.run(debug=True)

a = '''<form action="/submit_data" method="post">
    <input type="text" name="username" placeholder="Username">
    <input type="password" name="password" placeholder="Password">
    <button type="submit">Submit</button>
</form>
'''

import base64
with open('path/to/your/image.png', 'rb') as image_file:
    encoded_string = base64.ded_string = base64.b64encode(image_file.read()).decode('utf-8')
import base64

def favicon_encoded(favicon_file_path):
    with open(favicon_file_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string


import os

# 文件路径
file_path = 'path/to/your/file.txt'

# 检查文件是否存在
if os.path.exists(file_path):
    print(f"文件 {file_path} 存在")
else:
    print(f"文件 {file_path} 不存在")

# 如果你还想检查它是否是一个文件（而不是目录）
if os.path.isfile(file_path):
    print(f"{file_path} 是一个文件")
elif os.path.isdir(file_path):
    print(f"{file_path} 是一个目录")
else:
    print(f"{file_path} 不存在")
    
  
import os

# 获取当前执行脚本的完整路径
current_file_path = os.path.abspath(__file__)

# 获取当前执行脚本所在的目录
current_directory = os.path.dirname(current_file_path)

# 打印当前目录
print("当前文件目录:", current_directory)

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
if not os.path.exists(current_directory + 'config.json'):
  print('检测到配置文件不存在,请设定管理员账号密码')
  username = input('账号:')
  password = getpass('密码:')
  data = {
    'username' : username,
    'password' : password
  }
  with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
  print('设定成功')



import json

with open('data.json', 'r') as file:
    data = json.load(file)

print(data)  # 输出: {'name': 'John', 'age': 30, 'city': 'New York'}
import json

# 假设我们有以下JSON字符串
json_str = '{"name": "John", "age": 30, "hobby": null, "description": ""}'

# 解析JSON字符串为Python字典
data = json.loads(json_str)

# 检查'hobby'是否为空（这里我们定义为None）
if data.get('hobby') is None:
    print("'hobby' 是空的")

# 检查'description'是否为空字符串
if data.get('description') == "":
    print("'description' 是空字符串")

# 如果你想检查所有值并标记为空或非空
for key, value in data.items():
    if value is None or (isinstance(value, str) and value == ""):
        print(f"'{key}' 的值是空的")
    else:
        print(f"'{key}' 的值不是空的")
import json

data = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open('data.json', 'w') as file:
    json.dump(data, file)

import json

# 要写入JSON文件的数据
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# 将数据写入JSON文件
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)






import json
from flask import Flask, session
from flask_session import Session  # 假设您正在使用flask_session扩展
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# 假设 config_file_path 是您的配置文件路径
with open(config_file_path, 'r', encoding='utf-8') as file:
    config_data = json.load(file)

HOST = config_data['host']
PORT = config_data['port']
DEBUG_MODE = config_data['debug']
username = config_data['username']
# 假设 password_hash 是已哈希的密码（在配置文件中存储）
password_hash = config_data['password_hash']  # 注意这里使用了 password_hash 而不是 password

# 设置 Flask 应用的配置
app.config['SECRET_KEY'] = 'your-secret-key'  # 请确保这是一个安全的密钥
app.config['SESSION_TYPE'] = 'filesystem'

# 初始化 Flask-Session
Session(app)

# 假设我们有一个用于验证管理员凭据的函数
def verify_admin_credentials(provided_username, provided_password):
    # 这里我们假设 admin_credentials 是在 Flask 应用初始化时创建的，并且只包含哈希过的密码
    admin_credentials = {'username': username, 'password_hash': password_hash}
    if admin_credentials['username'] == provided_username and check_password_hash(admin_credentials['password_hash'], provided_password):
        return True
    return False

# ... 其他 Flask 应用代码 ...

# 当需要验证管理员凭据时
provided_username = 'admin'  # 假设这是从某个请求中获取的
provided_password = 'mypassword'  # 假设这是从某个请求中获取的
if verify_admin_credentials(provided_username, provided_password):
    print("登录成功！")
else:
    print("用户名或密码错误！")
