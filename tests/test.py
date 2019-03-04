import unittest

from circle_tui.api import CircleApi

class TestCircleApiProjectProp(unittest.TestCase):
    def setUp(self):
        self.api = CircleApi()

    def test_get_project(self):
        self.assertIsNone(self.api.project)

    def test_set_project(self):
        self.api.project = 'github/test/project'
        self.assertIsNotNone(self.api.project)

if __name__ == '__main__':
    unittest.main()

