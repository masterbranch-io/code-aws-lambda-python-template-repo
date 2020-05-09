import unittest
from entry_point import app


class TestEntryPoint(unittest.TestCase):
    def test_01(self):
        result = app.lambda_handler(None, None)
        self.assertEqual({'statusCode': 200, 'body': 'Hello from Lambda!'}, result)
