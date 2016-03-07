import re

class ErrorFile:
	"""Class that stores Blackboard log files and their locations"""


	def __init__(self, filename):
		self.filename = filename
		self.newName = self.filename[:-4] + '_formatted.txt'
		self.dict = {} # "Error": [Quantity, Exclude]


	def createDict(self):
		errorID = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
		regex = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} -\d{4}')
		errorString = ''

		logFile = open(self.filename)

		for line in logFile:
			
			if errorString == '':
				# If error empty, add to errorString
				errorString += str(line)
			elif regex.search(line):
				orig = errorString # Store original, full error
				errLine = errorString.split('\n')[0][27:] # Strip error to 1 line
				errorString = line # Begin new error
				errLine = re.sub(errorID, '', errLine) # Remove ErrorID
				errLine = ''.join([i for i in errLine if not i.isdigit()]) # Remove #'s

				if errLine not in self.dict:
					# If error not in dictionary, create entry
					self.dict[errLine] = [1, self.checkExclusion(orig), orig]
				else:
					# unpack values and recreate after adding to quantity
					a, b, c = self.dict[errLine]
					a += 1
					self.dict[errLine] = [a,b,c]
			else:
				errorString += str(line)

		logFile.close()

		# Print test values
		f = open(self.newName, 'w')
		for key, value in self.dict.items():
			# If Exclude == False, print to file
			if not value[1]:
				f.write('Error: ' + value[2].split('\n')[0] + '\n\tCount: ' + str(value[0]) + '\n')
		f.close()


	def checkExclusion(self, error):
		exclusionList = [i.rstrip('\n') for i in open('exclusionList.txt')]
		y = False
		for x in exclusionList:
			if x in error:
				y = True
		return y