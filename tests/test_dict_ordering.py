import unittest
from helpor.dict_ordering import add_orderings


class TestDictOrdering(unittest.TestCase):
    def test_empty_dict(self):
        self.assertEqual({}, add_orderings({}))

    def test_dict_without_nesting(self):
        self.assertEqual({'hello': 'world', 'counter': 1}, add_orderings({'hello': 'world', 'counter': 1}))

    def test_dict_with_one_level(self):
        original = {
            'nope': None,
            'first': {
                'type': 'string'
            },
            'second': {},
            'last': 1234
        }
        expected = {
            'nope': None,
            'first': {
                'type': 'string',
                'ordering': 0
            },
            'second': {},
            'last': 1234
        }
        self.assertEqual(expected, add_orderings(original))

    def test_deeper_dict(self):
        original = {
            'counter1': {'type': 'number'},
            'counter2': {'type': 'number'},
            'lets': {
                'type': 'list',
                'counter3': {'type': 'number'},
                'go': {
                    'type': 'object',
                    'deeper': {
                        'object1': {
                            'hello': 'world'
                        },
                        'object2': {
                            'type': 'string',
                            'this is': 'deep enough'
                        },
                        'type': {
                            'type': 'number'
                        }
                    }
                }
            }
        }
        expected = {
            'counter1': {
                'type': 'number',
                'ordering': 0
            },
            'counter2': {
                'type': 'number',
                'ordering': 1
            },
            'lets': {
                'type': 'list',
                'counter3': {
                    'type': 'number',
                    'ordering': 0
                },
                'go': {
                    'type': 'object',
                    'deeper': {
                        'object1': {
                            'hello': 'world',
                        },
                        'object2': {
                            'type': 'string',
                            'this is': 'deep enough',
                            'ordering': 0
                        },
                        'type': {
                            'type': 'number',
                            'ordering': 1
                        }
                    },
                    'ordering': 1
                },
                'ordering': 2
            }
        }
        self.assertEqual(expected, add_orderings(original))
