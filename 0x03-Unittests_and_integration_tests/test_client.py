#!/usr/bin/env python3
'''unittesting client module'''
from client import GithubOrgClient
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from parameterized import parameterized
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    '''class that inherits from unittest.TestCase'''

    @parameterized.expand([
        ("google", {'payload': False}),
        ("abc", {'payload': False}),
    ])
    @patch('client.get_json')
    def test_org(self, url: str, payload: Dict, mocked_get):
        '''unittest for org'''
        mocked_get.return_value = MagicMock(return_value=payload)
        result = GithubOrgClient(url)
        self.assertEqual(result.org(), payload)
        mocked_get.assert_called_once_with(
            GithubOrgClient.ORG_URL.format(org=url))

    def test_public_repos_url(self):
        '''unittest for _public_repos_url'''
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_last_transaction:
            result = {'repos_url': 'result'}
            mock_last_transaction.return_value = result
            self.assertEqual(
                GithubOrgClient('google')._public_repos_url,
                'result')

    @patch('client.get_json')
    def test_public_repos(self, mocked_get):
        '''unittest public_repos'''
        mocked_get.return_value = [{"name": "alx"}, {"name": "backend"}]
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mocked:
            mocked.return_value = {"repos_url": "repos_url"}
            self.assertEqual(
                GithubOrgClient('google').public_repos(),
                ["alx", "backend"])
        mocked.assert_called_once()
        mocked_get.assert_called_once()
