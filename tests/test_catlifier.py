from unittest import TestCase
from catlifier import Catlifier


class TestCatlifier(TestCase):
    def setUp(self) -> None:
        self.test_str = "hello world"

    def test_catlify(self):
        catlifier = Catlifier(self.test_str)
        catlified = catlifier.catlify()
        self.assertEqual(catlifier.base_text, self.test_str)
        self.assertEqual(catlified, self.test_str + "🐈")

    def test_uncatlify(self):
        catlified = self.test_str + "🐈"
        catlifier = Catlifier.uncatlify(catlified)
        self.assertEqual(catlifier.base_text, self.test_str)
