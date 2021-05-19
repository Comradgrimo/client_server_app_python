import unittest
from lesson_3.response import ServerResponse
from lesson_3.client import *
import json


# def send_json(arg: dict) -> bytes:
#     return json.dumps(arg).encode('utf-8')

class TestClient(unittest.TestCase):

    def test_send_json(self):
        foo = {'grimo':1}
        self.assertEqual(send_json(foo), b'{"grimo": 1}')

    def test_authorized(self):
        r = [{"Comrad": "12345"}, {"User": "123"}, {"grimo": "123"}, {"grimo1": "123"}]
        self.assertEqual(authorized('Comrad','123', r), 'Comrad')


if __name__ == "__main__":
    unittest.main()