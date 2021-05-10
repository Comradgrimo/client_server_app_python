# Программа клиента для отправки приветствия серверу и получения ответа
from sys import argv
from socket import *
import json
from datetime import datetime
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if len(argv) != 3:
    raise ValueError('Please provide ip and port (client.py localhost 7777)')

ip, port = str(argv[1]), int(argv[2])
s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect((ip, port))   # Соединиться с сервером

with open('staff.json') as f_n:
    objs = json.load(f_n)
objs['time'] = current_time
# ОТСЫЛАЕМ
msg = json.dumps(objs)
s.send(msg.encode('utf-8'))
# ПРИНИМАЕМ
data = s.recv(1024)
print('Сообщение от сервера: ', data.decode('utf-8'))
s.close()
