from Package.Directory.directory_func import *
import time

class Log():
    def __init__(self):
        self._logFileName = 'log_' + time.strftime('%Y_%m_%d_%H:%M:%S', time.localtime(time.time())) + '.txt'
        self._logFullDirectory = Get_DirectoryByType(EDirectory.logs) + self._logFileName

        with open(self._logFullDirectory, 'w'):
            pass
