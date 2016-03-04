class ErrorFile:
	"""Class that stores Blackboard log files and their locations"""


	def __init__(self, filename):
		self.filename = filename
		self.newName = self.filename[:-4] + '_formatted.txt'
		self.errors = self.createErrors()
		self.exclusions = self.checkExclusions()
		self.count = []


	def createErrors(self):
		logFile = open(self.filename)
		errorString = ''
		errorList = []
		y = 0

		for line in logFile:
			if y == 0 or '2015-' not in line:
				errorString += str(line)
				y = 1
			else:
				errorList.append(errorString)
				errorString = line
		
		logFile.close()
		return errorList


	def printErrors(self):
		f = open(self.newName, 'w')
		for x in range(len(self.errors)):
			if self.exclusions[x] == False:
				f.write(self.errors[x])
		f.close()


	def printFirstLines(self):
		f = open(self.newName[:-4] + 'Lines.txt', 'w')
		for x in range(len(self.errors)):
			if self.exclusions[x] == False:
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