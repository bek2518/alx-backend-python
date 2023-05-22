#!/usr/bin/env python3
'''
Tests the GithubOrgClient class
'''
import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''
    Class that is inherits from unittest and impements tests for
    GithubOrgClient
    '''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_org(self, org_examples):
        '''
        Method that tests GithubOrgClient.org returns correct value
        '''
        with patch('client.get_json') as mock_thing:
            test_payload = {'test': org_examples}
            mock_thing.return_value = test_payload

            github_org_client = GithubOrgClient(org_examples)

            self.assertEqual(github_org_client.org, test_payload)
            mock_thing.assert_called_once_with(GithubOrgClient.ORG_URL.
                                               format(org=org_examples))

    if __name__ == '__main__':
        unittest.main()
