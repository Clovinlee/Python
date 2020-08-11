"""
1.	Print Data
2.	Change Data
	a.	Add Data
	b.	Change Data
	c.	Erase Data
3.	Find Max,Min,Avg
4.	Sort Data
	a.	Ascending
	b.	Descending
5.	Move Data
	a.	Direction(L/R)
	b.	Range(Move distance)
6.	Reverse Position
7.	Compare Data
	a.	Same Values
	b.	Different Values
	c.  Concatenate Data
	d. 	Remove Duplicates
0.	Quit
"""

__author__ = 'Chrisanto'
__date__ = '$Date: 2020-08-11 $'
__source__ = '''http://pyparsing.wikispaces.com/file/view/fourFn.py
http://pyparsing.wikispaces.com/message/view/home/15549426
'''


class Menu:
	def __init__(self, data1):
		self.data1 = data1

	def menu(self):
		global option
		if option != '0':
			pass
		else:
			option = None
		order = {
			'1':self.printData,
			'2':self.changeData,
			'3':self.statisticData,
			'4':self.sortData,
			'5':self.moveData,
			'6':self.reverseData,
			'7':self.compareData,
			'0':self.quit
					}		
		while True:
			menu = input("===================\nMenu List : \n\t1.Print\n\t2.Change Data\n\t3.Statistic Data\n\t4.Sort Data\n\t5.Move Data\n\t6.Reverse Data\n\t7.Compare Data\n\t0.Quit\n===================\nMenu Input : ")
			if menu not in [x for x,y in order.items()]:
				print('\nError! Invalid menu input.')
				continue
			else:
				break
				
		order.get(menu)()

	def printData(self):
		print('\n============\nCurrent Data : ',self.data1,'\n============\n')
		self.menu()

	def changeData(self):
		global option
		def addData(self):
			global option
			while option != '0':
				print('\nCurrent Data : ',self.data1)
				while True:
					try:
						index_insert = int(input('Index of insert : '))
						if index_insert <= 0 or index_insert > len(self.data1)+1:
							print('\n Error Invalid Index!')
							continue
						else:
							pass
						self.data1.insert(index_insert-1,int(input('Value of Insert : ')))
					except:
						print('\nInvalid Value. Please input an integer')
						continue
					break
				print('\nCurrent Data : ',self.data1)
				option = input('\nPress enter to continue, or 0 to quit.')
		def replaceData(self):
			global option
			while option != '0':
				print('Current Data :',self.data1)
				if len(self.data1) == 0:
					print('\nError! Data is empty. Please add some value to it!')
					break
				else:
					pass
				while True:
					try:
						index_change = int(input('Index data to be changed : '))
						index_change -= 1
						value_change = int(input('Replace by value : '))
						self.data1[index_change] = value_change
						break
					except:
						print('Invalid Value. Please input an integer')
				print('Current Data :',self.data1)
				option = input('\nPress enter to continue, or 0 to quit')
		def eraseData(self):
			global option
			while option != '0':
				print('Current Data : ',self.data1)
				option = input('\nErase Data\n\ti.Erase by index\n\tii.Erase by value\n\tiii.Erase last index\n\tiv.Erase first value\n\tv.Erase all data\n\t0.Exit\nOption Input : ').lower()
				if len(self.data1) == 0:
					print('\nError! Data is empty.\nReturning to menu...')
					break
				else:
					pass
				if option.lower() == 'i':
					print('Current data : ',self.data1)
					while True:
						if len(self.data1) == '0':
							print('Data is empty! Nothing to delete')
							break
						try:
							del self.data1[int(input('Index of deletion : '))-1]
							print('\nDeletion success. Current data : ',self.data1)
							break
						except:
							print('\nError invalid integer input!\n')
				elif option.lower() == 'ii':
					print('Current data : ',self.data1)
					while True:
						temp = []
						if len(self.data1) == '0':
							print('\nData is empty! Nothing to delete')
							break
						try:
							val_delete = int(input('Value of deletion : '))
							[temp.append(x) for x in self.data1 if x != val_delete]
							self.data1 = temp
							print('Deletion success. {} is removed from data'.format(val_delete))
							print('')
							break
						except:
							print('\nError invalid value input!\n')
				elif option.lower() == 'iii':
					if len(self.data1) == '0':
						print('Data is empty! Nothing to delete')
					else:
						print('\nSuccessfully deleted ',self.data1.pop(),'from data')
						print('Current data : ',self.data1)
				elif option.lower() == 'iv':
					if len(self.data1) == '0':
						print('Data is empty! Nothing to delete')
					else:
						print('\nSuccessfully deleted ',self.data1.pop(0),'from data')
						print('Current Data : ',self.data1)
				elif option.lower() == 'v':
					if len(self.data1) == '0':
						print('Data is empty! Nothing to clear')
					else:
						self.data1.clear()
						print('Data cleared!. Current data : ',self.data1)
		order = {
			'a':addData,
			'b':replaceData,
			'c':eraseData,
				}
		while True:
			option = input('\nInput your option : \n\ta.Add Data\n\tb.Change Data\n\tc.Erase Data\n\t0.Exit\nOption Input : ').lower()
			print('')
			if option not in ['a','b','c','0']:
				print("\nPlease input a valid option!")
				continue
			if option != '0':
				order.get(option)(self)
			else:
				break
		self.menu()
	def statisticData(self):
		maxdata = self.data1[0]
		mindata = self.data1[0]
		sumdata = 0
		for x in self.data1:
			sumdata += x
			if x >= maxdata:
				maxdata = x
			elif x <= mindata:
				mindata = x
		print('\n==========\nMin Value :\t{}\nMax Value :\t{}\nAvg Value :\t{}\n==========\n'.format(mindata,maxdata,sumdata/len(self.data1)))
		self.menu()

	def sortData(self):
		def ascend():
			temp = []
			if len(self.data1) == 0:
				print('\nError. Empty data!')
			else:
				while len(self.data1) != 0:
					current = self.data1[0]
					for x in self.data1:
						if x <= current:
							current = x
					temp.append(self.data1.pop(self.data1.index(current)))
				self.data1 = temp
				print('Data successfully sorted by ascending order')
		def descend():
			temp = []
			if len(self.data1) == 0:
				print('\nError. Empty data!')
			else:
				while len(self.data1) != 0:
					current = self.data1[0]
					for x in self.data1:
						if x >= current:
							current = x
					temp.append(self.data1.pop(self.data1.index(current)))
				self.data1 = temp
			print('Data successfully sorted by descending order')
		global option
		order = {
			'a':ascend,
			'b':descend,
				}
		while True:
			print('\nCurrent Data : ',self.data1)
			option = input('\nInput your option : \n\ta.Ascending Order\n\tb.Descending Order\n\t0.Exit\nOption Input : ')
			if option not in ['a','b','0']:
				print('Error! Invalid option input.')
				continue
			elif option == '0':
				print('')
				break
			else:
				order.get(option)()
		self.menu()

	def moveData(self):
		global option
		while option != '0':
			print('\nCurrent Data : ',self.data1)
			option = input('\nInput your direction\n\tR.Right\n\tL.Left\n\t0.Exit\nDirection input : ')
			if option.upper() not in ['L','R','0']:
				print('Error! Invalid option input!')
				continue
			elif option == '0':
				print('')
				continue
			while True:
				try:
					distance = int(input('Enter the distance of movement : '))
					break
				except:
					print("Please input valid distance integer")
					continue
			if option.upper() == 'L':
				for x in range(distance):
					temp = self.data1[0]
					for move in range(len(self.data1)-1):
						self.data1[move] = self.data1[move+1]
					self.data1[-1] = temp
				print('Data Successfully Moved to Left')
			elif option.upper() == 'R':
				for x in range(distance):
					temp = self.data1[-1]
					for move in range(len(self.data1)-1,0,-1):
						self.data1[move] = self.data1[move-1]
					self.data1[0] = temp
				print('Data Successfully Moved to Right')
		self.menu()

	def reverseData(self):
		temp = []
		for x in range(len(self.data1)-1,0,-1):
			temp.append(self.data1[x])
		temp.append(self.data1[0])
		self.data1 = temp
		print("\nData successfully reversed to",self.data1,'\n')
		self.menu()

	def compareData(self):
		global option
		def sameValue():
			for x in self.data1:
				for y in data2:
					if x == y:
						if x not in temp:
							temp.append(x)
			print('\n========\n1st data : ',self.data1)
			print('2nd data : ',data2)
			print('Same values of both data :',temp,'\n========')
		def differentValue():
			global option
			for x in self.data1:
				if x not in data2:
					if x not in temp:
						temp.append(x)
			for z in data2:
				if z not in self.data1:
					if z not in temp:
						temp.append(z)
			print('\n========\n1st data : ',self.data1)
			print('2nd data : ',data2)
			print('Different values of both data :',temp,'\n========')	
		def concatData():
			print('==========\n1st data : ',self.data1)
			print('2nd data : ',data2)
			self.data1 += data2
			print('Concatenation of both data : ',self.data1,'\n==========')
		def duplicatesData():
			global option
			temp = self.data1
			temp = [i for n,i in enumerate(temp) if i not in temp[:n]]
			print('============\nCurrent data : ',self.data1)
			print('Cleaned duplicates of data :',temp,'\n============')
			self.data1 = temp
		order = {
					'a':sameValue,
					'b':differentValue,
					'c':concatData,
					'd':duplicatesData
					}
		while option != '0':
			option = input('\nInput your option : \n\ta.Same Values\n\tb.Different Values\n\tc.Concatenate data\n\td.Remove Duplicates\n\t0.Exit\nOption Input : ').lower()
			if option not in ['a','b','c','d','0']:
				print('Error! Invalid option input.')
				continue
			elif option == '0':
				print('')
				continue
			if option == 'd':
				pass
			else:
				data2 = []
				temp = []
				i = 1
				print('\nCurrent data : {}'.format(self.data1))
				while True:
					try:
						print('\nEnter \'x\' to stop adding.')
						addon = input('Enter 2nd data values of {} : '.format(i))
						if addon == 'x':
							break
						data2.append(int(addon))
						print('\nCurrent 2nd data : ',data2)
						i+=1
					except:
						print('Invalid integer value for 2nd data\n')
						continue
			order.get(option)()
			
		self.menu()

	def quit(self):
		global option
		option = '0'
		print("\n=======================\nQuitting Menu. Good bye\n=======================")

data1 = []
while True:
	try:
		length_data = int(input('Number of Data : '))+1
		break
	except:
		print('Error! Please input a valid integer.\n')
for x in range(1,length_data):
	while True:
		try:
			data1.append(int(input("Insert Data {} : ".format(x))))
			break
		except:
			print('Error! Please input a valid integer.\n')

option = None
start = Menu(data1)
start.menu()