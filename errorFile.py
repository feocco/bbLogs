import re

class bbLog:
	"""Class that stores Blackboard log files and their locations"""


	def __init__(self, fileName):
		self.fileName = fileName
		self.dict = self.createDict()

	def createDict(self):
		myDict = {}
		# RegEx Patterns
		errorIDReg = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')
		dateReg = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} -\d{4}')
		
		logFile = open(self.fileName)
		errorString = ''

		for line in logFile:
			if errorString == '': # For first line in log
				errorString += str(line)
			elif dateReg.search(line): # If date pattern in line
				orig = errorString # Store full error
				errLine = errorString.split('\n')[0][27:] # Strip all lines
				errorString = line # Start new error
				errLine = re.sub(errorIDReg, '', errLine) # RegEx Replace
				errLine = ''.join([i for i in errLine if not i.isdigit()]) # Remove #'s

				if errLine not in myDict:
					myDict[errLine] = [1, self.checkExclusion(orig), orig]
				else:
					a, b, c = myDict[errLine]
					a += 1 # Add 1 to count
					myDict[errLine] = [a,b,c]
			else:
				errorString += str(line)

		logFile.close()

		return myDict

	def checkExclusion(self, error):
		exclusionList = [i.rstrip('\n') for i in open('exclusionList.txt')]
		y = False
		for x in exclusionList:
			if x in error:
				y = True
		return y

	def writeLog(self):
		f = open(self.fileName[:-4] + '_formatted.txt', 'w')
		for key, value in self.dict.items():
			if not value[1]:
				f.write('Error: ' + value[2].split('\n')[0] + '\n\tCount: ' + str(value[0]) + '\n')
		f.close()

	def writeExclusionSummary(self):
		pass
		# Print the counts of excluded errors.