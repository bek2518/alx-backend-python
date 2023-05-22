#!/usr/bin/env python3
'''
Tests the GithubOrgClient class
'''
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        '''
        Method that tests _public_repos_url of the GithubOrgClient
        '''
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) \
                as mock_thing:
            repo_url = 'https://api.github.com/orgs/google/repos'
            mock_thing.return_value = {"repos_url": repo_url}
            result = GithubOrgClient('google')._public_repos_url
            self.assertEqual(result, repo_url)

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_method, mock_thing):
        '''
        Method that tests public_repos of GithubOrgClient
        '''
        test_payload = [
            {'name': 'nginx', 'owner': {'login': 'MIT'}},
            {'name': 'apache', 'owner': {'login': 'Apache'}},
            {'name': 'webkit', 'owner': {'login': 'GPL'}},
        ]
        repos_url = 'https://api.github.com/orgs/google/repos'
        mock_method.return_value = repos_url
        mock_thing.return_value = test_payload
        result = GithubOrgClient('google').public_repos()
        mock_thing.assert_called_once_with(repos_url)
        mock_method.assert_called_once()
        self.assertEqual(result, ['nginx', 'apache', 'webkit'])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        '''
        Method that tests has_license from GithubOrgClient
        '''
        self.assertEqual(GithubOrgClient.has_license(repo, license), expected)

    if __name__ == '__main__':
        unittest.main()
