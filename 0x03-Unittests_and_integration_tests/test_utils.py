#!/usr/bin/env python3
'''unittesting utils module'''
from utils import access_nested_map, get_json, memoize
from unittest import TestCase, mock
from parameterized import parameterized, parameterized_class
from typing import Mapping, Sequence, Any, Dict


class TestAccessNestedMap(TestCase):
    '''class that inherits from TestCase'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, dic: Mapping, path: Sequence,
                               output: Any) -> None:
        '''method to test that the method returns what it is supposed to'''
        self.assertEqual(access_nested_map(dic, path), output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, dic: Mapping,
                                         path: Sequence) -> Any:
        '''method that raises exception error'''
        with self.assertRaises(KeyError):
            access_nested_map(dic, path)


class TestGetJson(TestCase):
    '''class that inherits from TestCase'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url: str, payload: Dict) -> None:
        '''method to test that utils.get_json returns the expected result.'''
        with mock.patch('utils.requests.get') as mocked_get:
            mock_response = mock.Mock()
            mock_response.json.return_value = payload
            mocked_get.return_value = mock_response
            result = get_json(url)
            mocked_get.assert_called_with(url)
            mocked_get.assert_called_once_with(url)
            self.assertEqual(result, payload)


class TestMemoize(TestCase):
    '''class that inherits from TestCase'''

    def test_memoize(self) -> None:
        '''unittest for test_memoize method.'''

        class TestClass:
            '''The class we are going to unitest'''

            def a_method(self) -> None:
                '''metheod that we are unittesting'''
                return 42

            @memoize
            def a_property(self) -> None:
                '''a_propertyy that is going to call a_method'''
                return self.a_method()

        with mock.patch.object(TestClass, 'a_method') as mocked_get:
            mocked_get.return_value = 42
            instance = TestClass()
            result1 = instance.a_property
            result2 = instance.a_property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mocked_get.assert_called_once()
