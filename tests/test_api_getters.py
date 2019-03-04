import unittest
import responses
import json
from os.path import join
from unittest.mock import patch

from . import FIXTURES_DIR

from circle_tui.api import CircleApi

class TestApiGetters(unittest.TestCase):
    def setUp(self):
        self.api = CircleApi()
    
    @responses.activate
    def test_get_me(self):
        with open(join(FIXTURES_DIR, 'me.json')) as me_json:
            responses.add(responses.GET, 'https://circleci.com/api/v1.1/me',
                          json=json.load(me_json), status=200)

        api_me = self.api.get_me()
        self.assertIsNotNone(api_me)
        self.assertEqual(api_me['login'], 'wurbanski')
        self.assertNotIn('__circle_yml', api_me)
