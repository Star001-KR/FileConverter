from Package.Debug.Error import ParamDataTypeError, FileNameNotInitError
from Package.Debug.Log import ELogTpye, Log
import time
import os

def Init_Log(isDelOldLog):
    if isDelOldLog and Log.Is_LogFileName():
        os.remove(Log.Get_LogFullName())

    Log()


def Write_Log(logType, logContent):
    assert type(logType) == ELogTpye, 'err : wrong data type in log type param.'
    
    _logContent = (type(logContent) == str) and logContent or str(logContent)

    # prefix string.
    if logType == ELogTpye.normal:
        _logStr = '  {0:<6}\t|\t{1}\t|\t'.format(Log.Push_LogLine(), 
        time.strftime('%H:%M:%S', time.localtime(time.time())))

    elif logType == ELogTpye.error:
        _logStr = '* {0:<6}\t|\t{1}\t|\t'.format(Log.Push_LogLine(), 
        time.strftime('%H:%M:%S', time.localtime(time.time())))

    elif logType == ELogTpye.warning:
        _logStr = '> {0:<6}\t|\t{1}\t|\t'.format(Log.Push_LogLine(), 
        time.strftime('%H:%M:%S', time.localtime(time.time())))

    else:
        _logStr = '? {0:<6}\t|\t{1}\t|\t'.format(Log.Push_LogLine(), 
        time.strftime('%H:%M:%S', time.localtime(time.time())))

    _logStr = _logStr + _logContent

    with open(Log.Get_LogFullName(), 'a') as logFile:
        logFile.write(_logStr + '\n')
