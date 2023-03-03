

import Timestamp

ts_obj = Timestamp.Timestamp()
timestamp = ts_obj.getTimestamp()

LOG_EVENT = 'EVENT'
LOG_ERROR = 'ERROR'
LOG_INFO = 'INFO'

logpath = 'logs/'
file = None

def openLog():

    try:
        global file
        file = open(logpath + timestamp + '.log', 'w')
        return True
    except:
        return False

def writeLog(type, filename, log):
    global file
    file.write(ts_obj.getTimestamp() + ' ' + type + ' ' + filename + ' ' + log + '\n')

def closeLog():
    try:
        global file
        file.close()
        return True
    except:
        return False