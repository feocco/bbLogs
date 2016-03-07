import os
from errorFile import *

class fileFactory:
	"""Class for obtaining log files in a directory"""

	def __init__(self, directory=os.getcwd()):
		self.directory = directory
		self.bbFiles = self.getBbFiles()

	def getBbFiles(self):
		dirFiles = [self.directory + '\\' + f for f in os.listdir(self.directory) if re.search(r'bb-.+\.\d{4}-\d{2}-\d{2}.txt', f)]
		bbFiles = []
		for f in dirFiles:
			answer = input("Format: {0}?".format(f))
			if answer[0].lower() == 'y':
				bbFiles.append((f,True))
			else:
				bbFiles.append((f,False))
		return bbFiles

	def createInstances(self):
		bbFiles = []
		for bbFile, form in self.bbFiles:
			if form:
				instance = bbLog(bbFile)
				bbFiles.append(instance)
		return bbFiles

	def writeLogs(self):
		bbFiles = self.createInstances()
		print(str(bbFiles))
		for bbLog in bbFiles:
			bbLog.writeLog()