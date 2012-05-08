from optparse import OptionParser
from controllers.projects import ProjectsController
from controllers.users import UsersController
from config.routes import dispatch_rules
from core.view import ViewBase
from views.raw_view import RawView


class Dispatcher:
	"""Primary flow control and MVC support. Will reconcile input with controller/handler and output with a view"""


	def __init__(self):
		"""Initialize support structures"""
	
		self.callables = {}
		self.dispatch_rules = dispatch_rules  # attached for easier/explicit access within instance

	def loadControllers(self):
		"""Load controllers into a dict (self.callables) for easy dispatching. Keys will represent unique combinations of input"""

		for param_tuple, handler in self.dispatch_rules.items():
			callable_key = self.__conventionalizeParams(param_tuple)		
			controller = handler.im_class(self.options)
			self.callables[callable_key] = getattr(controller, handler.__name__)
	
	def __conventionalizeParams(self, iterable):
		"""For using input params as a key to a controller route, we need to convenionalize (sort and make string)"""

		return "|".join(sorted(iterable))
	

	def dispatch(self):
		"""Using input, route to the appropriate controller handler, output type will reconcile and invoke view as specified by handler decorators"""	

		input = []
		for option_tuple in self.options.__dict__.items():  #build list of input for route reconciliation
			if option_tuple[1]:
				input.append(option_tuple[0])
		try:
			controller_results = self.callables[self.__conventionalizeParams(input)].__call__()

		except KeyError:
			raise Exception("Undefined route given params, %s" % self.__conventionalizeParams(input))

		
		if type(controller_results) is tuple:  #TODO make decorator pass in view name, instead of a default
			return ViewBase(controller_results[1]).flush()
		elif type(controller_results) is list:
			return RawView(controller_results).flush()
		else:
			raise Exception("Unsupported controller result type: %s" % str(type(controller_results)))
	

	def parseOptions(self):
		"""Parse options inputted at runtime"""

		parser = OptionParser()
                parser.add_option(
                  "-u",
                  "--user",
                  dest="user",
                  help="enter a user or 'all'"
                )

                parser.add_option(
                  "-p",
                  "--projects",
                  dest="projects",
                  help="enter a project or 'all'"
                )
                (self.options, self.args) = parser.parse_args()
		
