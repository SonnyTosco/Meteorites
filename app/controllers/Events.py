from system.core.controller import *

class Events(Controller):
	def __init__(self, action):
		super(Events, self).__init__(action)
		self.load_model('Event')
		self.load_model('User')
		self.db = self._app.db

	############### GET ###################
	def join(self):
		pass

	def unjoin(self):
		pass

	def view(self):
		return self.load_view('view.html')

