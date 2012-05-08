from core.model import ModelBase

class User(ModelBase):
	"""Model class for User"""
        
	def list(self):
		"""Return all users"""
                return self.data.users

