from core.controller import *
from models.user import User

class UsersController(ControllerBase):
	"""Users controller"""

	
	def list(self, clause=None):
		"""List all users"""
                return User().list()
	

	@defaultView
	def show(self):
		"""Show user entries, matching the given name, or all is specified"""
		
		if self.input.user == "all":
			return self.list()

		return [u for u in User().list() if u["name"]==self.input.user]
