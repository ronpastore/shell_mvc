from core.view import ViewBase

class RawView(ViewBase):
	
	"""A raw data viewer, does no formatting, just print objects"""

	def __init__(self, results):
		self.results = results

	def flush(self):
		print self.results

