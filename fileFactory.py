import os
import datetime
from bbLog import *
from time import sleep

class fileFactory:
	"""Class for obtaining log files in a directory"""

	def __init__(self, directory=os.getcwd()):
		self.directory = directory
		self.bbFiles = self.getBbFiles()

	def getBbFiles(self):
		dirFiles = [self.directory + '\\' + f for f in os.listdir(self.directory)]
		bbFiles = []
		for f in dirFiles:
			if re.search(r'[b]{2}-\w+-log.*.txt', f) and not re.search(r'[b]{2}-access-log.*.txt', f):
				bbFiles.append((f,True))
		return bbFiles

	def createInstances(self):
		bbFiles = []
		for bbFile, doFormat in self.bbFiles:
			if doFormat:
				print('{0} : Parsing {1}'.format(datetime.datetime.now(), bbFile))
				instance = bbLog(bbFile)
				bbFiles.append(instance)
		sleep(2)
		return bbFiles