

class ViewBase:
	"""Base view class, can be used for most output where listing dictionaries.  Prints header then rows and columns from data."""
	
	_delimeter = "\t"

	def __init__(self, list_of_dicts):
		self._list_of_dicts = list_of_dicts
	
	def flush(self):
		"""Will print out all results in column format."""
	
		if not self._list_of_dicts:
			print "Empty result set"
		else:
			self._getHeaders()
			self._printHeaders()
			self._writeRows()
	
	def _getHeaders(self):
		"""Uses dictionary keys as column headers. All dicts must match."""

		self.headers = [k for k,v in self._list_of_dicts[0].items()]			

	def _printHeaders(self):
		"""Will output the header plus a line border directly below"""
	
		header = self._delimeter.join(self.headers)
		header_border = "".join(["-" for x in header])
		
		# If delimeter is a tab, add 3 spaces for each so border length matches header length (visually).
		if self._delimeter == "\t":
			header_border+= "".join(["---" for x in header if x=="\t"])

		print header
		print header_border
		
		
	def _writeRows(self):
		"""Loop through results in list and print out rows"""

		for record in self._list_of_dicts:
			row_data = []
			for column_data in self.headers:
				row_data.append(str(record[column_data]))
			print self._delimeter.join(row_data )

if __name__=="__main__":
	d = [{"foo":"bar1","foo2":"bar2" }, {"foo":"bar2", "foo2":"bar3"}]
	vb = ViewBase(d)
	vb.flush()


	d = []
	vb = ViewBase(d)
	vb.flush()
