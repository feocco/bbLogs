import re
from difflib import SequenceMatcher

class ErrorFile:
	"""Class that stores Blackboard log files and their locations"""


	def __init__(self, filename):
		self.filename = filename
		self.newName = self.filename[:-4] + '_formatted.txt'
		self.errors = self.createErrors()
		self.exclude = self.checkExclusions()
		self.count = []
		# Should switch to hashes
		# self.dict = {'ERROR': [exclude, count, exceptionType]}


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


	def createFile(self):
		f = open(self.newName, 'w')
		for x in range(len(self.errors)):
			if self.exclude[x] == False:
				f.write(self.errors[x])
		f.close()


	def createLineFile(self):
		f = open(self.newName[:-4] + 'Lines.txt', 'w')
		for x in range(len(self.errors)):
			if not self.exclude[x]:
				f.write(self.errors[x].split('\n')[0] + '\n')
		f.close()


	def checkExclusions(self):
		exclusionList = [i.rstrip('\n') for i in open('exclusionList.txt')]
		booleanList = []
		for err in self.errors:
			y = False
			for x in exclusionList:
				if x in err.split('\n')[0]:
					y = True
			booleanList.append(y)

		return booleanList


	# Writing new self.count function
	def counts(self):
		errors = []
		self.count = []
		
		date = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} -\d{4}')
		errorID = re.compile(r'\w{8}-\w{4}-\w{4}-\w{4}-\w{12}')

		patterns = [date, errorID]

		for err in self.errors:

			#Sort only by first line, no Caused By's taken into account. 
			err = err.split('\n')[0]

			# Replace unique patterns w/ ''
			for pattern in patterns:
				err = re.sub(pattern, '', err)

			# If error not in list, add it to the list. Then add a count of 1. 
			# Else add one to its count.
			if err not in errors:
				errors.append(err)
				self.count.append(1)
			else:
				self.count[errors.index(err)] += 1

		f = open(self.newName[:-4] + 'self.count.txt', 'w')
		for err in errors:
			f.write(err[2:] + '\n\tCount: {0}\n'.format(self.count[errors.index(err)]))
		f.close()
