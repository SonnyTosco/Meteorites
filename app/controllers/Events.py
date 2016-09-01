from __future__ import print_function
import sys
from system.core.controllindex

class Events(Controller):
	def __init__(self, action):
		super(Events, self).__init__(action)
		self.load_model('Event')
		self.load_model('User')
		self.db = self._app.db

	############### GET ###################
	def view(self):
		return self.load_view('view.html')

	############### POST ###################
	def index(self, event_id):
		self.model['Event'].toggle_join(session['id'], event_id)
		return redirect('/')
