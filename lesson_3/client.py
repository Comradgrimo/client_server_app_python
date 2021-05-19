# Программа клиента для отправки приветствия серверу и получения ответа
from socket import *
import json
from datetime import datetime
from lesson_3.response import ServerResponse
import logging
import lesson_5.client_log_config
logger = logging.getLogger('app1.main')

def send_json(arg: dict) -> bytes:
    return json.dumps(arg).encode('utf-8')


def current_time() -> str:
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


while True: #ДОДЕЛАТЬ ОБРАБОТКУ ВВОДА
    # login = input('Введите новый логин: ')
    login = 'Comrad'
    # pswrd = input('Введите новый пароль: ')
    pwd = '123'
    break


def authorized(user: str, pswrd: str, openfile: list) -> str:
    for i in openfile:
        if user in i:
            return user
    open_file('user.json', 'w', {user: pswrd})  # Здесь должно быть добавление в базу


def open_file(name: str, flag: str, info=None) -> list:           # Здесь должно быть чтение из базы
    if flag != "w":
        with open(f'../lesson_3/{name}', f'r', encoding='utf-8') as f_n:
            objs = json.load(f_n)
        return objs
    else:
        with open(f'../lesson_3/{name}', 'r', encoding='utf-8') as f_n:
            objs = json.load(f_n)
            objs.append(dict(info))
        # print(objs)
        with open(f'../lesson_3/{name}', 'w', encoding='utf-8') as f_n:
            json.dump(objs, f_n)
        return objs


foo = open_file('user.json','r')
aut = authorized(login, pwd, foo)

my_resp = ServerResponse()

# if len(argv) != 3:
#     raise ValueError('Please provide ip and port (client.py localhost 7777)')

# ip, port = str(argv[1]), int(argv[2])
ip, port = 'localhost', 7777

s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
s.connect((ip, port))

# ОТСЫЛАЕМ ПРИВЕТСТВИЕ
msg = json.dumps(my_resp.presence(login, current_time()))
s.send(msg.encode('utf-8'))

# ПРИНИМАЕМ ИНФУ ОТ СЕРВЕРА
data = s.recv(1024).decode('utf-8')
foo = json.loads(data)

if foo['response'] == 200:                                                  #ДОДЕЛАТЬ ВОЗМОЖНЫЕ ОШИБКИ
    print(f'Добро пожаловать {login}')
    logger.info(data)

# _____________________________________________________________
while True:
    msg = str(input('Введите сообщение: '))
    if msg == '_exit':
        s.send(send_json(my_resp.exit(login)))
        print('exit')
        logger.info('Выход')
        break


    msg_server = my_resp.msg(current_time(), 'all', aut, msg)
    # print(msg_server, type(msg_server))
    to_server = send_json(msg_server)
    s.send(to_server)
    print(f'Вы отправили:{msg}')

    data = s.recv(1024)
    if data:
        logger.info(data.decode("utf-8"))
s.close()

# ________________________________________________________________________
