#!/usr/bin/env python3
'''unittesting client module'''
from client import GithubOrgClient
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    '''class that inherits from unittest.TestCase'''

    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    @parameterized.expand([
        ("google", {'payload': False}),
        ("abc", {'payload': False}),
    ])
    @patch('client.get_json',)
    def test_org(self, url: str, payload: Dict, mocked_get):
        '''unittest for org'''
        mocked_get.return_value = MagicMock(return_value=payload)
        result = GithubOrgClient(url)
        self.assertEqual(result.org(), payload)
        mocked_get.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=url))
