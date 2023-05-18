#!/usr/bin/env python3
'''
Tests that the method access_nested_map returns what it is suppose
to return
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    Class that inherits from unittest and implements different methods
    '''
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''Method that tests the provided method (access_nested_map)'''
        self.assertEqual(access_nested_map(nested_map, path), expected)
