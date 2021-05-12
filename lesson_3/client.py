# Программа клиента для отправки приветствия серверу и получения ответа
from sys import argv
from socket import *
import json
from datetime import datetime
from response import ServerResponse

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
my_resp = ServerResponse()

authorized_user = ['Comrad', ['user1'], ['user2']]

while 1:
    # login = input('Введите логин: ')
    login = 'Comrad'
    if login in authorized_user:
        break
    else:
        login = input('Введите новый логин: ')
        pswrd = input('Введите новый пароль: ')
        break
if len(argv) != 3:
    raise ValueError('Please provide ip and port (client.py localhost 7777)')

ip, port = str(argv[1]), int(argv[2])
s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
result = s.connect((ip, port))
# ОТСЫЛАЕМ
msg = json.dumps(my_resp.presence(login))
s.send(msg.encode('utf-8'))
# ПРИНИМАЕМ
data = s.recv(1024).decode('utf-8')
foo = json.loads(data)
if foo['response'] == 200:
    print(f'Добро пожаловать {login}\nСообщение от сервера: {data} ')
s.close()
