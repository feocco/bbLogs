import os
import datetime
from bbLog import *

class fileFactory:
	"""Class for obtaining log files in a directory"""

	def __init__(self, directory=os.getcwd()):
		self.directory = directory
		self.bbFiles = self.getBbFiles()

	def getBbFiles(self):
		dirFiles = [self.directory + '\\' + f for f in os.listdir(self.directory) if re.search(r'[b]{2}-\w+-log.*', f)]
		bbFiles = []
		for f in dirFiles:
			answer = input("Format: {0}?\nResponse(y/n): ".format(f))
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
				print('{0} : Parsing {1}'.format(datetime.datetime.now(), bbFile))
				instance = bbLog(bbFile)
				bbFiles.append(instance)
		return bbFiles