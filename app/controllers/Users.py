from __future__ import print_function
import sys
from system.core.controller import *

class Users(Controller):
	def __init__(self, action):
		super(Users, self).__init__(action)
		self.load_model('User')
		self.db = self._app.db

	########## GET ##########
	def index(self):
		if session.get('id'):
			return self.load_view('main.html')
		return self.load_view('welcome.html')

	def dashboard(self):
		if session.get('id'):
			return self.load_view('dashboard.html')
		return redirect('/')

	def logout(self):
		session.clear()
		return redirect('/')				

	########## POST ##########      
	def login_user(self):
		output = self.models['User'].login(request.form)
		if output['status'] == True:
			session['id'] = output['user']['id']
		else:
			for message in output['log']:
				flash(message, 'error')
		return redirect('/')

	def register_user(self):
		output = self.models['User'].register(request.form)
		if output['status'] == True:
			session['id'] = output['user']['id']
		else:
			for message in output['log']:
				flash(message, 'error')
		return redirect('/')

