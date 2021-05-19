import unittest
from lesson_3.response import ServerResponse


class TestResponse(unittest.TestCase):

    def test_authentication(self):
        time = '2021-05-17 16:39:05'
        self.assertEqual(ServerResponse.authentication(self,time),
                         ({'action': 'authenticate', 'time': '2021-05-17 16:39:05', 'user': {'account_name': 'account_name', 'password': 'account_pass'}})),

    def test_response(self):
         self.assertEqual(ServerResponse.response(self,200, 'OK'),({'name': 'response', 'response': 200, 'alert': 'OK'}))

    def test_exit(self):
        self.assertEqual(ServerResponse.exit(self),({'action': 'quit'}))

    def test_presence(self):
        self.assertEqual(ServerResponse.presence(self, 'Comrad', '2021-05-17 17:08:34'), ({'action': 'presence', 'time': '2021-05-17 17:08:34', 'type': 'status', 'user': {'account_name': 'Comrad', 'status': 'Yep, I am here!'}}))


    def test_msg(self):
        self.assertEqual(ServerResponse.msg('time', '2021-05-17 21:21:43', 'all', 'Comrad', 'Hello'), ({'action': 'msg', 'time': '2021-05-17 21:21:43', 'to': 'all', 'from': 'Comrad', 'encoding': 'utf-8', 'message': 'Hello'}))


if __name__ == "__main__":
    unittest.main()
