# bbLogs

Parses Blackboard Learn log files that fit the bb-logName-log.txt format. Access logs not included.

After each log file is parsed, an HTML file is created to summarize its content. 
Duplicate errors are removed, in favor of timestamps and a count. 
The error message is listed initially with an option to expand the stack. 
A nav bar is created to access each log file parsed
The table is sortable by first time of occurrence(Error) and Count. 

This is a work in progress. I'll need to add error handling and fine tune the GUI. It doesn't work how I'd like it to right now. 

To use:
* Download: https://github.com/feocco/bbLogs/blob/master/bbLog1.0.zip?raw=true
* Unzip package
* Open bbLog.exe
* Select Directory where logs reside > Press Ok
* Wait for parsing to complete, should be logged in CMD window
  * GUI looks awful. I know.
* Log directory will now contain HTML reports for each log. Open em up!

Example Output:
* https://i.imgur.com/oFnsM87.png
