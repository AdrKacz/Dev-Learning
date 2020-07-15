class A:
	def a(self, params):
	   print("a", params)
	def b(self, params):
	   print("b", params)   
	def c(self, function, *params):
		function(*params)
	def d(self, params):
		self.c(self.a, params)
		self.c(self.b, params)

if __name__=='__main__':
	my_A = A()
	my_A.a('I am a')
	my_A.b('I am b')
	my_A.d('I am d')