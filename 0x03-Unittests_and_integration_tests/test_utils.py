#!/usr/bin/env python3
'''
Tests that the method access_nested_map returns what it is suppose
to return
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest import mock
from unittest.mock import patch


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        '''
        Tests if the method access_nested_map raises KeyError
        '''
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''
    Class that inherits from unittest and implements different methods
    to test get_json function in utils
    '''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''
        Method that tests get_json  using mock
        '''
        with patch('requests.get') as mock_thing:
            mock_response = mock.Mock()
            mock_response.json.return_value = test_payload
            mock_thing.return_value = mock_response

            result = get_json(test_url)
            mock_thing.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemorize(unittest.TestCase):
    '''
    Class that inherits from unittest and implements different methods
    to test memoize decorator in utils
    '''
    def test_memoize(self):
        '''
        Method that tests memoize using mock patch
        '''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        
        with patch.object(TestClass, "a_method") as mock_method:
            mock_response = mock.Mock()
            mock_response.return_value = 42
            mock_method.return_value = mock_response

            thing = TestClass()
            self.assertEqual(thing.a_property(), 42)
            self.assertEqual(thing.a_property(), 42)
            mock_method.assert_called_once_with()

    if __name__ == '__main__':
        unittest.main()
