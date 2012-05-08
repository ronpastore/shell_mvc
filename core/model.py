from db import data

class ModelBase:
	"""Model base class, attaches data source (dummy data).  Also contains stubs for future crud operations."""

	def __init__(self):
		self.data = data  # dummy data source, must change if use-case exceeds read-only, single process/thread execution

	def save(self):
		pass
	
	def update(self):
		pass 
	
	def get(self,id):
		pass
