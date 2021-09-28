from Package.Directory.directory_func import *
from Package.Debug.Error import *
import time
import os

class ELogTpye(Enum):
    normal = auto()
    error = auto()
    warning = auto()


class Log():
    def __init__(self):
        self._logFileName = 'log_' + time.strftime('%Y_%m_%d_%H:%M:%S', time.localtime(time.time())) + '.txt'
        self._logFullDirectory = Get_DirectoryByType(EDirectory.logs) + self._logFileName
        
        with open(self._logFullDirectory, 'w'):
            pass

        self._logLine = 1


    def Write_Log(self, logType, logContent):
        try:
            if (not type(logType) == ELogTpye) | (not type(logContent) == str):
                raise ParamDataTypeError

        
            if logType == ELogTpye.normal:
                _logStr = ' '

            elif logType == ELogTpye.error:
                _logStr = '*'

            elif logType == ELogTpye.warning:
                _logStr = '>'

            else:
                _logStr = '?'

        except ParamDataTypeError:
            pass


    def Del_LogFile(self):
        os.remove(self._logFullDirectory)


    def Get_LogFullDirectory(self):
        return self._logFullDirectory


    def __del__(self):
        with open(self._logFullDirectory, 'r') as logFile:
            _log = logFile.read()
        
        if not len(_log):
            os.remove(self._logFullDirectory)