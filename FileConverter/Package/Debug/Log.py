from Package.Directory.directory_func import *
from Package.Debug.Error import *
from enum import Enum, auto
import time
import os

class ELogTpye(Enum):
    normal = auto()
    error = auto()
    warning = auto()


class Log():
    logDirectory = ''
    logName = []
    logLine = 0
    
    def __init__(self):
        self._logFileName = 'log_' + time.strftime('%Y_%m_%d_%H:%M:%S', time.localtime(time.time())) + '.txt'
        self._logFullDirectory = self.Init_LogDirectory() + self._logFileName

        try:
            with open(self._logFullDirectory, 'w'):
                pass

        except FileNotFoundError:
            self._logFullDirectory = self._logFileName

            with open(self._logFullDirectory, 'w'):
                pass

        self.Init_LogLine()

        if not len(self.logName):
            self.logName.clear

        self.logName.append(self._logFileName)
        self.logName.append(self._logFullDirectory)


    @deco_usedirmethod(EDirectory.logs)
    def Init_LogDirectory(self, directory):
        self.logDirectory = directory
        return self.logDirectory


    @classmethod
    def Init_LogLine(cls):
        cls.logLine = 0


    @classmethod
    def Push_LogLine(cls):
        cls.logLine += 1
        return cls.logLine


    @classmethod
    def Is_LogFileName(cls):
        return (len(cls.logName)) and True or False


    @classmethod
    def Get_LogFullName(cls):
        try:
            if cls.Is_LogFileName():
                return cls.logName[1]

            else:
                raise FileNameNotInitError
    
        except FileNameNotInitError:
            return 'TEMP_LOG'


    def __del__(self):
        with open(self._logFullDirectory, 'r') as logFile:
            _log = logFile.read()
        
        if not len(_log):
            os.remove(self._logFullDirectory)