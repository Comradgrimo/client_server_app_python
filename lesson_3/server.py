# Программа сервера для получения приветствия от клиента и отправки ответа
from sys import argv
from socket import *
from response import ServerResponse
import json
import logging
import lesson_5.server_log_config
logger = logging.getLogger('app.main')


def server_program():
    my_resp = ServerResponse()
    if len(argv) != 3:
        raise ValueError('Please provide ip or port (server.py localhost 7777)')

    objs = my_resp.response(200,'ok')

    s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    ip, port = str(argv[1]), int(argv[2])
    s.bind((ip, port))                # Присваивает IP, PORT
    while True:
        s.listen(5)                       # Переходит в режим ожидания запросов;
                                          # Одновременно обслуживает не более
                                          # 5 запросов.

        client, addr = s.accept()
        # ПРИНИМАЕМ
        if addr:
            while True:
                data = client.recv(1024)
                if data:
                    jdata = json.loads(data.decode('utf-8'))

                    try:
                        if jdata.get('user').get('account_name'):
                            logger.info(f"Подключился {addr} {jdata.get('user').get('account_name')}")
                    except AttributeError:
                        pass
                    if jdata.get('action') != 'quit':
                        logger.info(jdata)
                        msg = json.dumps(objs)
                        client.send(msg.encode('utf-8'))
                    else:
                        logger.info(f'Клиент {jdata.get("client_name")} отключился')
                        break



if __name__ == '__main__':
    server_program()

