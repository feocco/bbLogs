import re
import xml.etree.ElementTree as etree

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
		
		logFile = open(self.fileName, encoding="utf8")
		errorString = ''

		for line in logFile:
			if errorString == '': # For first line in log
				errorString += str(line)
			elif dateReg.search(line): # If date pattern in line
				orig = errorString # Store full error
				errLine = errorString.split('\n')[0][27:] # Strip date
				errorString = line # Start new error
				errLine = re.sub(errorIDReg, '', errLine) # Replace RegEx patterns w/ ''
				errLine = ''.join([i for i in errLine if not i.isdigit()]) # Remove #'s

				if errLine not in myDict:
					if not self.exclude(orig):
						myDict[errLine] = [1, orig, []]
				else:
					a, c, d = myDict[errLine]
					a += 1 # Add 1 to count
					d.append(re.compile('\\d{2}:\\d{2}:\\d{2}').search(orig).group(0))
					myDict[errLine] = [a,c,d]
			else:
				errorString += str(line)

		logFile.close()

		return myDict

	def exclude(self, error):
		xml = etree.parse('knownIssues.xml')
		root = xml.getroot()
		y = False
		
		for issue in root.findall('issue'):
			keyword = issue.find('keywords').text
			if keyword in error:
				y = True
				break
		return y