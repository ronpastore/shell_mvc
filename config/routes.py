from controllers.projects import ProjectsController
from controllers.users import UsersController

"""Dispatching is based on the combination of inputs, where each unique combo routes to a controller method"""

dispatch_rules = {

	("user", "projects"): ProjectsController.list,
	("projects", ):ProjectsController.list,
	("user", ):UsersController.show,
	#("user", "add"):UsersController.create  -- example/no implementation

}
