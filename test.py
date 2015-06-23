import os
import unittest

from views import app, db
from _config import basedir
from models import User


TEST_DB = 'test.db'

class AllTests(unittest.TestCase):

	############################
	### set up and tear down ###  
	############################

	def setUp(self):
		app.config['TESTING'] = True
		app.config['WTF_CSRF_ENABLED'] = False
		app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
		self.app = app.test_client()
		db.create_all()

	# executed after each test
	def tearDown(self):
		db.drop_all()

	# helper functions
	def login(self, name, password):
		return self.app.post('/', data=dict(
			name=name, password=password), follow_redirects=True
		)

	# each test should start with 'test'
	def test_user_setup(self):
		new_user = User('michael', 'michael@mherman.org', 'michaelherman')
		db.session.add(new_user)
		db.session.commit()
		test = db.session.query(User).all()
		for t in test:
			t.name
		assert t.name == "michael"

	def test_form_is_present_on_login_page(self):
		response = self.app.get('/')
		self.assertEqual(response.status_code, 200)
		self.assertIn(b'Please sign in to access your task list', response.data)

	def test_users_cannot_login_unless_registered(self):
		response = self.login('foo', 'bar')
		self.assertIn(b'Invalid username or password', response.data)






if __name__ == "__main__":
	unittest.main()
