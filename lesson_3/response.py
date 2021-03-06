import json
from datetime import datetime

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('../lesson_3/json_response.json', encoding='utf-8') as f_n:
    objs = json.load(f_n)


class ServerResponse(object):
    """docstring"""

    def __init__(self):
        """Constructor"""
        self.time = current_time

    def authentication(self, time):
        """
        authentication on server
        """
        for i in objs:
            if i.get('action') == 'authenticate':
                auth = i
                auth['time'] = time
                return auth

    def response(self, code, msg):
        """
        response
        """
        for i in objs:
            if i.get('name') == 'response':
                res = i
                res['response'] = code
                res['alert'] = msg
                return res

    def exit(self) :
        """
        exit
        """
        for i in objs:
            if i.get('action') == 'quit':
                res = i
                return res

    def presence(self, login, time):
        """
        authentication on server
        """
        for i in objs:
            if i.get('action') == 'presence':
                pres = i
                pres['time'] = time
                pres['user']['account_name'] = login
                return pres

    def msg(self, time,to, f_from,message):
        """
        msg
        """
        for i in objs:
            if i.get('action') == 'msg':
                msg = i
                msg['time'] = time
                msg['to'] = to
                msg['from'] = f_from
                msg['message'] = message
                return msg


if __name__ == "__main__":

    foo = ServerResponse()
    # print(foo.authentication(current_time))
    # print(foo.response(200, 'OK'))
    # print(foo.exit())
    # print(foo.presence('Comrad', current_time))
    # print(foo.msg(current_time, 'all', 'Comrad', 'Hello'))