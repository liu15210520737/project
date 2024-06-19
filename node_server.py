from flask import *
import os, json, secrets
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

def generate_key(length):
  key = secrets.token_hex(length)  # 生成指定长度的随机十六进制字符串
  return key

current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
config_file_path = os.path.join(current_directory, 'config.json')
if not os.path.exists(config_file_path):
  print('检测到配置文件不存在')
  print('正在生成token')
  token = generate_key(36)
  print('正在生成会话密钥')
  secret_key = generate_key(18)
  print('正在生成伪装域名')
  domain = generate_key(5)
  config_data ={
    'token' : token,
    'secret_key' : secret_key,
    'domain' : domain,
    'host' : '0.0.0.0',
    'port' : 9999,
    'debug_mode' : False
  }
  print('正在写入配置文件')
  with open(config_file_path, 'w', encoding='utf-8') as f:
    json.dump(config_data, f, ensure_ascii=False, indent=4)
  print('设定成功')

with open(config_file_path, 'r', encoding='utf-8') as file:
  config_data = json.load(file)
secret_key = config_data['secret_key']
token = config_data['token']
domain = config_data['domain']
HOST = config_data['host']
PORT = config_data['port']

# 设置密钥用于会话签名
app.config['SECRET_KEY'] = secret_key
# 设置会话类型为文件系统（或其他你选择的类型）
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
# 假设我们有一个管理员token的字典
admin_credentials = {'token': token}

@route('/' + domain)