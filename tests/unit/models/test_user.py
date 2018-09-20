from unittest import TestCase
from puppycompanyblog.models import User


class UserTest(TestCase):
	def test_create_user(self):
		user = User('test@gmail.com', 'testusername', 'testpassword')

		self.assertEqual('test@gmail.com', user.email)
		self.assertEqual('testusername', user.username)
		self.assertTrue(user.check_password('testpassword'))
