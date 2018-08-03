from app import app
import unittest

class FlaskappTests(unittest.TestCase):
	def setUp(self):
		#create a test client
		self.app = app.test_client()
		#propagate the exceptions to the test client
		self.app.testing = True

	def test_users_status_code(self):
		result = self.app.get('/api/v1/users')
		self.assertEqual(result.status_code, 200)