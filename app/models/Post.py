from __future__ import print_function
from system.core.model import Model
import sys

class Post(Model):
	def __init__(self):
		super(Post, self).__init__()

	def get_Post(self, Post_id):
		query = """SELECT * FROM posts where Posts.id = Post_id
						"""
		data =	{	'Post_id': Post_id
						}
		self.db.query_db(query, data)	

	def get_Posts(self):
		query = """SELECT * FROM Posts
						"""
		return self.db.query_db(query, data)
