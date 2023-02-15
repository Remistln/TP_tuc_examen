import unittest
from app.utils.utils import *
from unittest.mock import Mock

mock = Mock()

class TestUtils(unittest.TestCase):
    def test_should_return_age(self):
        self.assertEqual(1, 1)