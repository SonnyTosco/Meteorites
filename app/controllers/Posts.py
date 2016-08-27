from system.core.controller import *

class Posts(Controller):
	def __init__(self, action):
		super(Posts, self).__init__(action)
		self.load_model('Event')
		self.load_model('User')
		self.db = self._app.db

	########## GET ##########      

	########## POST ##########      
	def add_post(self):
		output = self.models['Post'].add_post(request.form)
		if output['status'] == False:
		return redirect('/')

	def delete_post(self):
		output = self.models['Post'].delete_post(request.form)
		return redirect('/')