import unittest
from .context import helpor


class TestDictOrdering(unittest.TestCase):
    def test_something(self):
        helpor.dict_ordering.add_orderings({"hello": "world"})
        self.assertEqual(True, False)
