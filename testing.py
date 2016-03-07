from errorFile import *
from fileFactory import *
import time
start_time = time.time()
#test = bbLog('bb-services-log.2016-03-02.txt')
#test.createDict()
#test.getBbFiles(r'C:\Users\jfeocco\Downloads\bb-services-log.2016-02-27')
test = fileFactory(r'C:\Users\jfeocco\Downloads\bb-services-log.2016-02-27').writeLogs()
print("--- %s seconds ---" % (time.time() - start_time))