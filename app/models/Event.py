from __future__ import print_function
from system.core.model import Model
import sys

class Event(Model):
	def __init__(self):
		super(Event, self).__init__()


	def get_event(self, event_id):
		query = """SELECT * FROM events WHERE events.id = event_id
						"""
		data =	{	'event_id': event_id
						}
		self.db.query_db(query, data)	

	def get_events(self):
		query = """SELECT * FROM events
						"""
		return self.db.query_db(query, data)
