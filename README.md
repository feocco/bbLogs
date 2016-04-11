# bbLogs

Parses Blackboard Learn log files that fit the bb-logName-log.txt format. Access logs not included.

The formatted log file will include:
* No error files which include a string from exclusionList.txt
* First line of unique error messages
** A count of this error message in the log
** Time of each occurrence

To use, execute the following commands in a python shell:
* from fileFactory import *
* files = fileFactory(r'C:\Users\jfeocco\Downloads\logs')
	* Respond y to each log file you want to parse
* files.writeLogs()

The formatted files are then pushed to the working directory defined by fileFactory in the following format:
* bb-logName-log_formatted.txt