import sys
import os
import unittest

src_dir = os.path.join(os.getcwd(), "src")
sys.path.append(src_dir)

from hello_world_lambda_handler import lambda_handler

class TestHelloWorldLambda(unittest.TestCase):
    def test_lambda_handler_empty_event(self):
        event = {}
        context = None
        result = lambda_handler(event, context)
        self.assertEqual(result, "Hello, World!")

    def test_lambda_handler_custom_event(self):
        event = {"name": "John Doe"}
        context = None
        result = lambda_handler(event, context)
        self.assertEqual(result, "Hello, World!")

if __name__ == "__main__":
    unittest.main()
