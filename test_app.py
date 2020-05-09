import unittest
import app


class TestApp(unittest.TestCase):
    def test_01(self):
        result = app.method()
        self.assertEqual('Hello World!', result)
