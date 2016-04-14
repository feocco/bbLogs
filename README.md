# bbLogs

Parses Blackboard Learn log files that fit the bb-logName-log.txt format. Access logs not included.

After each log file is parsed, an HTML file is created to summarize its content. 
Duplicate errors are removed, in favor of timestamps and a count. 
The error message is listed initially with an option to expand the stack. 
A nav bar is created to access each log file parsed
The table is sortable by first time of occurrence(Error) and Count. 

I'm still developing this project and will work towards a standalone app soon. For now, use the following steps to parse files:
* Install Python 3.4+
* Clone project & cd into directory
* cmd: python htmlFactory.py
* Input log file directory or press enter to parse log files in current directory
* Open the HTML generated in the log directory

Example Output:
* https://i.imgur.com/yC8yodT.png