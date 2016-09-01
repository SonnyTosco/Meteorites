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

	def toggle_join(self, user_id, event_id):
		query = """SELECT * FROM users_has_events WHERE user_id = :user_id
							AND event_id = :event_id LIMIT 1
						"""
		data =	{	'user_id': user_id,
							'event_id': event_id
						}

		if len(self.db.query_db(query, data)) == 0:
			query = """INSERT INTO users_has_events (user_id, event_id, created_at, updated_at)
								VALUES (:user_id, :event_id, NOW(), NOW())
							"""
		else:
			query = """DELETE FROM users_has_events WHERE user_id = :user_id
								AND event_id = :event_id LIMIT 1
							"""			
		return self.db.query_db(query, data)
