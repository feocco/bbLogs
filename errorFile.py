import re

class ErrorFile:
	"""Class that stores Blackboard log files and their locations"""


	def __init__(self, filename):
		self.filename = filename
		self.newName = self.filename[:-4] + '_formatted.txt'
		self.errors = self.createErrors()
		self.count = []
		self.dict = {} # "Error": [Quantity, Exclude]

	def createDict(self):
		errorID = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
		
		for error in self.errors:
			orig = error
			error = error.split('\n')[0][27:]
			values = [1, self.checkExclusion(error), orig]

			# Get rid of error-id
			error = re.sub(errorID, '', error)
			# Get rid of all numbers
			error = ''.join([i for i in error if not i.isdigit()])

			if error not in self.dict:
				self.dict[error] = values
			else:
				a, b, c = self.dict[error]
				a += 1
				self.dict[error] = [a,b,c]


		f = open(self.newName, 'w')
		for key, value in self.dict.items():
			if not value[1]:
				f.write('Error: ' + value[2].split('\n')[0] + '\n\tCount: ' + str(value[0]) + '\n')
		f.close()


	def createErrors(self):
		logFile = open(self.filename)
		errorString = ''
		errorList = []
		regex = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} -\d{4}')		

		for line in logFile:
			if not regex.search(line):
				errorString += str(line)
			else:
				errorList.append(errorString)
				errorString = line
		
		logFile.close()
		
		# First list item is empty string
		errorList = errorList[1:]
		return errorList


	def checkExclusion(self, error):
		exclusionList = [i.rstrip('\n') for i in open('exclusionList.txt')]
		y = False
		for x in exclusionList:
			if x in error:
				y = True
		return y