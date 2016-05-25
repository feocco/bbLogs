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
		# Should we expand this from 404 to all 400 / 500 errors? 
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
		# Returns count of unique user pk1's for entire log
		uniqueVisitors = []
		for request, values in self.dict.items():
			visitors = values[1]
			for visitor in visitors:
				if visitor not in uniqueVisitors:
					uniqueVisitors.append(visitor)

		return len(uniqueVisitors)

	def peakHourly(self):
		# Peak hits by hour
		hitsPerHr = []
		for hour in range(1,24):
			count = 0
			if hour < 10:
				timestampReg = re.compile('\d\d/\w+/\d{4}:0' + str(hour) + r':\d\d:\d\d')
			else:
				timestampReg = re.compile('\d\d/\w+/\d{4}:' + str(hour) + r':\d\d:\d\d')
			
			for request, values in self.dict.items():
				for time in values[0]:
					match = timestampReg.search(time)
					if match:
						count += 1
			hitsPerHr.append((hour, count))
		return hitsPerHr

	def peakMinutes(self):
		hitsPerMin = []
		for request, values in self.dict.items():
			for hour in range(1,24):
				for minute in range(1, 60):
					count = 0
					if hour < 10:
						if minute < 10:
							timestampReg = re.compile('\d\d/\w+/\d{4}:0' + str(hour) + ':0' + str(minute) + r':\d\d')
							timestamp = '0' + str(hour) + ':0' + str(minute)
						else:
							timestampReg = re.compile('\d\d/\w+/\d{4}:0' + str(hour) + ':' + str(minute) + r':\d\d')
							timestamp = '0' + str(hour) + ':' + str(minute)
					else:
						timestampReg = re.compile('\d\d/\w+/\d{4}:' + str(hour) + ':' + str(minute) + r':\d\d')
						timestamp = str(hour) + ':' + str(minute)

					for time in values[0]:
						match = timestampReg.search(time)
						if match:
							count += 1
					hitsPerMin.append((timestamp, count))
		return hitsPerMin