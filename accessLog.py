import re
import os

class accessLog:
	"""Stores Access Logs and their associated data"""
	def __init__(self, fileName):
		self.fileName = fileName
		self.dict = self.createDict()

	def createDict(self):
		# RegEx Patterns
		ipAddressReg = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
		userPk1Reg = re.compile(r'\s_(\d*)_1\s')
		timestampReg = re.compile(r'\d\d/\w+/\d{4}:\d\d:\d\d:\d\d')
		requestReg = re.compile(r'\"(.*)HTTP/\d.\d\"')
		httpStatusReg = re.compile(r'HTTP/\d.\d"\s\d\d\d')
		ttsReg = re.compile(r'HTTP/\d.\d"\s\d\d\d\s(-|\d*)')

		myDict = {}
		
		logFile = open(self.fileName, encoding='utf8')

		for line in logFile:
			# Get values from line
			ipAddress = self.returnMatch(ipAddressReg, line)
			userPk1	= self.returnMatch(userPk1Reg, line)
			timestamp = self.returnMatch(timestampReg, line)
			request = self.returnMatch(requestReg, line)
			httpStatus = self.returnMatch(httpStatusReg, line)[-3:]
			# TTS isn't correct. I think it's bytes to serve. 
			tts = self.returnMatch(ttsReg, line)[-1]

			if request in myDict:
				# Unpack values, append duplicate request's values, repack. 
				preTimestamp, preUserPk1, preIpAddress, preHttpStatus, preTts = myDict[request]
				preTimestamp.append(timestamp)
				preUserPk1.append(userPk1)
				preIpAddress.append(ipAddress)
				preHttpStatus.append(httpStatus)
				preTts.append(tts)
				myDict[request] = [preTimestamp, preUserPk1, preIpAddress, preHttpStatus, preTts]
			else:
				myDict[request] = [[timestamp], [userPk1], [ipAddress], [httpStatus], [tts]]

		return myDict

	def returnMatch(self, regex, data):
		result = regex.search(data)
		if result:
			return result.group(0)
		else:
			return ''

	# Functions / Goals:
	# - Log Size
	# - Top requests sorted by hits
	# - Unique visitors/users sorted by hits (IP or User_ID)
	# - Top HTTP Status Codes sorted by hits

	def requestStats(self):
		# Valid Requests / Total Requests
		validRequests = 0
		totalRequsts = 0
		for request, values in self.dict.items():
			httpStatus = values[3]
			for status in httpStatus:
				if status != '404':
					totalRequsts += 1
					validRequests += 1
				else:
					totalRequsts += 1
		
		return (validRequests, totalRequsts)

	def count404(self):
		# Failed requests(404)
		pass

	def uniqueVisitors(self):
		# Unique Visitors
		pass

	def peakHourly(self):
		# Peak hits by hour
		pass

a = accessLog(r'D:\Downloads\02327934\p001a\bb-access-log.2016-05-12_p001a.txt')

# for key, values in a.dict.items():
# 	print(key, 'Count: ', len(values[0]))
# 	print(values)
# 	print('\n--')
print(a)
print(a.requestStats())