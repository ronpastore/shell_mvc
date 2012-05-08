from core.model import ModelBase


class Project(ModelBase):
	"""Model class for projects"""

        def list(self):
		"""return all projects"""
                return self.data.projects


