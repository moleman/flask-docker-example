import unittest

from mock import patch

import app as web


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        web.app.config['TESTING'] = True
        self.app = web.app.test_client()

    @patch('app.redis')
    def test_get(self, redis):
        response = self.app.get('/')
        assert response.data.startswith('Hey!!, we have Flask in a Docker container!')


if __name__ == '__main__':
    unittest.main()