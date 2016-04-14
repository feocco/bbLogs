# bbLogs

Parses Blackboard Learn log files that fit the bb-logName-log.txt format. Access logs not included.

The formatted log file will include:
* No error files which include a string from exclusionList.txt
* First line of unique error messages
	* A count of this error message in the log
	* Time of each occurrence
