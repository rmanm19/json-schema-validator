import unittest
from main import sanitize_text

class TestMain(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(sanitize_text("token=ghp_1234567890abcdef"), "token=[REDACTED]")
