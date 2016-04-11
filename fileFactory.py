import os
from bbLog import *

class fileFactory:
	"""Class for obtaining log files in a directory"""

	def __init__(self, directory=os.getcwd()):
		self.directory = directory
		self.bbFiles = self.getBbFiles()

	def setDir(self):
		self.directory = input('Please input a directory. \n The default directory, is the current working directory( {0} )'.format(self.directory))

	def getBbFiles(self):
		dirFiles = [self.directory + '\\' + f for f in os.listdir(self.directory) if re.search(r'[b]{2}-\w+-log.*', f)]
		bbFiles = []
		for f in dirFiles:
			answer = input("Format: {0}?".format(f))
			if len(answer) == 0:
				bbFiles.append((f,False))
			elif answer[0].lower() == 'y':
				bbFiles.append((f,True))
			else:
				bbFiles.append((f,False))
		return bbFiles

	def createInstances(self):
		bbFiles = []
		for bbFile, doFormat in self.bbFiles:
			if doFormat:
				instance = bbLog(bbFile)
				bbFiles.append(instance)
		return bbFiles

	def writeLogs(self):
		bbFiles = self.createInstances()
		for bbLog in bbFiles:
			bbLog.writeLog()