from json.decoder import JSONDecodeError
from Package.Directory.directory import *
import json
import platform
import glob

def Init_Directory():
    FileConverterDirectory(EDirectory.excelDirectory, Get_PathFromJson('excelDirectory'))
    FileConverterDirectory(EDirectory.allExcelDirectory, glob.glob('{0}*.xlsx'.format(Get_DirectoryDic()[EDirectory.excelDirectory])))
    FileConverterDirectory(EDirectory.jsonDirectory, Get_PathFromJson('jsonDirectory'))
    FileConverterDirectory(EDirectory.gameConfigDirectory, Get_PathFromJson('gameConfigDirectory'))
    FileConverterDirectory(EDirectory.validationDirectory, Get_PathFromJson('validationDirectory'))
    FileConverterDirectory(EDirectory.logs, Get_PathFromJson('logs'))
    print('here')
    

def Add_Directory(directoryType, filePath):
    if not directoryType in Get_DirectoryDic().keys:
        return 'err : wrong directory type input. (input key already)'

    else:
        FileConverterDirectory(directoryType, filePath)


def Del_Directory(directoryType):
    FileConverterDirectory.Del_Directory(directoryType)


def Get_DirectoryDic():
    return FileConverterDirectory.Get_DirectoryDic()


def Get_DirectoryByType(directoryType):
    _directoryDic = FileConverterDirectory.Get_DirectoryDic()

    if not directoryType in _directoryDic.keys():
        return 'err : wrong directory type input. (key exist err)'

    else:
        return _directoryDic[directoryType]


def Get_PathFromJson(directoryType):
    isMac = (platform.system() == "Darwin") and True or False
    jsonPath = (isMac) and 'Config/directory.json' or 'Config\\directory.json'

    try:
        with open (jsonPath) as file:
            file_json = json.load(file)
            directorySet = (isMac) and file_json['mac'] or file_json['windows']

    except JSONDecodeError:
        return 'err : json file error'
    
    for key in directorySet:
        if key == directoryType:
            return directorySet[key]

    return 'err : input wrong directory type.'