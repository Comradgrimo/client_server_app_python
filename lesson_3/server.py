# Программа сервера для получения приветствия от клиента и отправки ответа
from sys import argv
from socket import *

import json


if len(argv) != 3:
    raise ValueError('Please provide ip or port (server.py localhost 7777)')


objs = {
    'response': 200,
    'alert': 'OK'
}

s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
ip, port = str(argv[1]), int(argv[2])
s.bind((ip, port))                # Присваивает IP, PORT
s.listen(5)                       # Переходит в режим ожидания запросов;
                                  # Одновременно обслуживает не более
                                  # 5 запросов.
while True:
    client, addr = s.accept()
    # ПРИНИМАЕМ
    data = client.recv(1024)
    print(data.decode('utf-8'))
    # ОТСЫЛАЕМ
    msg = json.dumps(objs)
    client.send(msg.encode('utf-8'))
    client.close()
