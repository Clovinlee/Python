
class Math:
	def __init__(self,a,b,operator):
		self.a = a
		self.b = b
		self.operator = operator

	def calc(self):
		opt = {'+':self.a+self.b, '-':self.a-self.b, '*':self.a*self.b, '/':self.a/self.b, '^':self.a**self.b}
		print(opt.get(self.operator))
while True:
	try:
		start = Math(int(input('First Number >')),int(input('Second Number>')),input('Operator >'))
		start.calc()
		break
	except ZeroDivisionError:
		print("Cannot divide integer by zero!")
	except:
		print("Invalid Input!")

print("Task completed")
