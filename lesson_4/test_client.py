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

if __name__ == "__main__":
    unittest.main()