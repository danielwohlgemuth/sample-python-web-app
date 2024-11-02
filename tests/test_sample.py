import unittest
from moto import mock_aws
from application import application
from utils import create_table


class TestHello(unittest.TestCase):

    def setUp(self):
        application.testing = True
        self.application = application.test_client()

    def test_hello(self):
        rv = self.application.get('/')
        self.assertEqual(rv.status, '200 OK')

    @mock_aws
    def test_signup(self):
        create_table()
        rv = self.application.post('/signup', data={ "email": "test@example.com" })
        self.assertEqual(rv.status, '201 CREATED')
        self.assertEqual(rv.data, b'{"email": "test@example.com"}')

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-report'))
    unittest.main()