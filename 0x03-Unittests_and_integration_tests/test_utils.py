#!/usr/bin/env python3
'''unittesting utils module'''
from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    '''class that inherits from unittest.TestCase'''

    @parameterized.expand([
        ({"a": 1}, ("a",)),
        ({"a": {"b": 2}}, ("a",)),
        ({"a": {"b": 2}}, ("a", "b"))
    ])
    def test_test_access_nested_map(self, dic: Mapping, path: Sequence) -> Any:
        '''method to test that the method returns what it is supposed to'''
        result = access_nested_map(dic, path)
        self.assertEqual(access_nested_map(dic, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_test_access_nested_map_exception(self, dic: Mapping,
                                              path: Sequence) -> Any:
        '''method that raises exception error'''
        with self.assertRaises(KeyError):
            access_nested_map(dic, path)
