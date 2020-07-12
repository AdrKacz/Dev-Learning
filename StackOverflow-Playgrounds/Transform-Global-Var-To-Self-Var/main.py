class Hello():
	a = 4
	b = 4
	c = 4
	def __init__(self):
		d = 4
		for attr in dir(self):
			if not callable(attr) and not attr.startswith('__'):
				self.__dict__.setdefault(attr, Hello.__dict__.get(attr) + 1)