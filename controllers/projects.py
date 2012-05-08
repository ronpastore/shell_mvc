from core.controller import *
from models.project import Project
from models.user import User

class ProjectsController(ControllerBase):
	"""Projects controller, can add projects related logic here"""        
	

	@defaultView
	def list(self):
		"""List all projects, if user is supplied, filter by user."""

                projects = Project().list()
                if self.input.user:
                        user_ids = [ u["id"] for u in User().list() if u["name"] == self.input.user ]
                        if not user_ids:
                                raise Exception("User was not found, %s" % self.input.user)

			#note: this will return projects from multiple users if they share a name
                        return [p for p in projects if p["user_id"] in user_ids]  
                return projects

