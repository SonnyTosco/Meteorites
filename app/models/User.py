from __future__ import print_function
import sys
from system.core.model import Model
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User(Model):
	def __init__(self):
		super(User, self).__init__()

	def get_users(self):
		query = """SELECT * FROM users
						"""
		return self.db.query_db(query, data)

	def login_user(self, data):
		query = "SELECT * FROM users WHERE id = :id LIMIT 1"	
		print("DATA", file=sys.stderr)
		print(data, file=sys.stderr)			
		user = self.db.query_db(query, data)
		print("USER INFO", file=sys.stderr)
		print(user, file=sys.stderr)

		# If new user:
		if len(user) == 0:
			# Add user to database:
			query = """INSERT INTO users (id, created_at, updated_at)
								VALUES (:id, NOW(), NOW())
							"""
			self.db.query_db(query, data)
			return {'log': ['Greetings, {}! Please enjoy your stay amongst the stars!'.format(data['name'])]}

		return {'log': ['Welcome back, {}!'.format(data['name'])]}							

	def register(self, data):
		log = []

		# Check if any fields are empty:                
		for key, value in data.iteritems():
			if len(value) == 0:
				log.append('Registration error: please fill in all form fields.')
				return {'status': False, 'log': log}

		# Check for valid first name:
		if len(data['name']) < 2:
			log.append('Registration error: please enter a valid first name (letters only).')
			return {'status': False, 'log': log}

		# Check for valid alias:
		if len(data['alias']) < 2:
			log.append('Registration error: please enter a longer alias.')
			return {'status': False, 'log': log}

		# Check for valid email:
		if not EMAIL_REGEX.match(data['email']):
			log.append("Registration error: please enter a valid email (example: name@mailserver.com)")
			return {'status': False, 'log': log}

		# Check if the email is a new/unique entry:
		query = "SELECT email FROM users WHERE email = :email LIMIT 1"
		if len(self.db.query_db(query, data)) > 0:
			log.append("Registration error: email already registered, please log in.")
			return {'status': False, 'log': log}

		# Check password length:
		if len(data['password']) < 8:
			log.append('Registration error: password must be at least 8 characters long.')
			return {'status': False, 'log': log}

		# Check if the password matches the confirmation:
		if data['password'] != data['password_confirmation']:
			log.append('Registration error: password confirmation does not match.')
			return {'status': False, 'log': log}

		# # Set user level:
		# query = "SELECT * FROM users LIMIT 1"
		# if len(self.db.query_db(query)) == 0:
		# 	level = 'Admin'     
		# else:
		# 	level = 'Normal'

		# dat = {'level': level}
		dat = {}
		for key, value in data.iteritems():
			dat[key] = value

		# All conditions met. Encrypt password:
		dat['password'] = self.bcrypt.generate_password_hash(dat['password'])

		# Add to database:
		query = """INSERT INTO users (name, email, alias, password, birthday, created_at, updated_at)
							VALUES (:name, :email, :alias, :password, :birthday, NOW(), NOW())
						"""
		self.db.query_db(query, dat)						
		query = "SELECT * FROM users WHERE email = :email LIMIT 1"		
		return {'status': True, 'user': self.db.query_db(query, dat)[0]}        