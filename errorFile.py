import re

class ErrorFile:
	"""Class that stores Blackboard log files and their locations"""


	def __init__(self, filename):
		self.filename = filename
		self.newName = self.filename[:-4] + '_formatted.txt'
		self.errors = self.createErrors()
		self.exclude = self.checkExclusions()
		self.count = []


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


	def getCounts(self):
		counts = []
		countedAlready = []
		# Get rid of timestamp using string indexing [28:]
		# Can we count # of duplicate items in a list easily? 
		for err in self.errors:
			counter = 0
			err = err.split('\n')[0][28:]
			#print(err)
			if err not in countedAlready:
				for x in self.errors:
					x = x.split('\n')[0][28:]
					#print(x)
					#UnicodeEncodeError: 'charmap' codec can't encode characters in position 137-138: character maps to <undefined>
					if x in err:
						counter += 1
				countedAlready.append(err)
			counts.append(counter)
		return counts

		# Need to account for "Error ID is XXXX-XXXXX-XXXXX"
		# Need to account for different PK1's, URL's, etc

	def stripErrorId(self, firstLine):
		if 'Error ID is' in firstLine:
			pass

	# Writing new counts function
	def counts(self):
		errors = []
		counts = []
		
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
				counts.append(1)
			else:
				counts[errors.index(err)] += 1

		f = open(self.newName[:-4] + 'Counts.txt', 'w')
		for err in errors:
			f.write(err + '\n\tCount: {0}\n'.format(counts[errors.index(err)]))
		f.close()
