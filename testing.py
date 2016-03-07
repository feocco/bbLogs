from errorFile import *
import time
start_time = time.time()
test = bbLog('bb-services-log.2016-03-02.txt')
test.createDict()
print("--- %s seconds ---" % (time.time() - start_time))