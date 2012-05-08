
def defaultView(fn, *args, **kwargs):
	"""A Decorator, will wrap controller results in the default view when specified, which outputs headers, rows and columns."""

	def wrapped(*args, **kwargs):
		return ( "default", fn(*args, **kwargs) ) # tuple tells dispatcher that payload is second sequence item, first is view name

	#match decorator name to func name so dispatcher can still do inspection
	wrapped.__name__  =  fn.__name__  
	return wrapped

class ControllerBase:
	"""Base controller class, this doesn't do much except make sure controllers have user input"""

	def __init__(self, options):
		self.input = options

