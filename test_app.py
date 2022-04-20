import unittest
from app import app

class TestSquare(unittest.TestCase):
    def test_positive(self):
        with app.test_client() as test_client:
            response = test_client.get('/square/2')
            self.assertTrue(response.status_code == 200)
            self.assertTrue(response.data == b'4')
            self.assertFalse(response.data == b'5')
    def test_negative(self):
        with app.test_client() as test_client:
            response = test_client.get('/square/-2')
            self.assertTrue(response.status_code == 200)
            self.assertTrue(response.data == b'4')
            self.assertFalse(response.data == b'-4')
    def test_zero(self):
        with app.test_client() as test_client:
            response = test_client.get('/square/0')
            self.assertTrue(response.status_code == 200)
            self.assertTrue(response.data == b'0')
            self.assertFalse(response.data == b'1')
if __name__ == '__main__':
    unittest.main()

