import os
import datetime
from bbLog import *
from accessLog import *
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
				bbFiles.append((f,False))
			elif re.search(r'[b]{2}-access-log.*.txt', f):
				bbFiles.append((f, True))
		return bbFiles

	def createInstances(self):
		bbFiles = []
		for bbFile, isAccessLog in self.bbFiles:
			if isAccessLog:
				instance = accessLog(bbFile)
			else:
				instance = bbLog(bbFile)
			bbFiles.append(instance)

		return bbFiles