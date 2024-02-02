#!/usr/bin/env python3
'''unittesting utils module'''
from utils import access_nested_map, get_json
from unittest import TestCase, mock 
from parameterized import parameterized, parameterized_class
from typing import Mapping, Sequence, Any, Dict
import requests


class TestAccessNestedMap(TestCase):
    '''class that inherits from unittest.TestCase'''

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


@parameterized_class([
    {'test_url': "http://example.com", 'test_payload': {"payload": True}},
    {'test_url': "http://holberton.io", 'test_payload': {"payload": False}}
])
class TestGetJson(TestCase):
    '''class that inherits from unittest.TestCase'''

    @mock.patch('utils.requests.get')
    def test_get_json(self, mocked_get: mock.MagicMock):
        '''method to test that utils.get_json returns the expected result.'''
        mock_response = mock.Mock()
        response = self.test_payload
        mock_response.json.return_value = response
        mocked_get.return_value = mock_response
        result = get_json(self.test_url)
        mocked_get.assert_called_with(self.test_url)
        mocked_get.assert_called_once_with(self.test_url)
        self.assertEqual(result, self.test_payload)
