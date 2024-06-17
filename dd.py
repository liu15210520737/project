from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session  # 需要安装 flask-session 来支持会话
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