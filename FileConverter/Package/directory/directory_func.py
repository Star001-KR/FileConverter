from Package.Directory.directory import *
import json
import platform
import glob

def deco_usedirmethod(directoryType):
    assert (type(directoryType) == EDirectory) or (type(directoryType) == list), 'err : wrong data type input.'

    _dirList = []
    
    def appear_dirList(dirType):
        if not FileConverterDirectory.Is_InitDirectoryType(dirType):
            FileConverterDirectory(dirType, Get_PathFromJson(str(dirType).split('.')[1]))

            if dirType == EDirectory.excelDirectory:
                FileConverterDirectory(EDirectory.allExcelDirectory, glob.glob('{0}*.xlsx'.format(Get_DirectoryDic()[EDirectory.excelDirectory])))

        _dirList.append(Get_DirectoryByType(dirType))

    def decorator(func):
        if (type(directoryType) == EDirectory):
            appear_dirList(directoryType)

        else:
            for _dirType in directoryType:
                assert (type(_dirType) == EDirectory), 'err : wrong data type in directoryType list.'
                
                appear_dirList(_dirType)

        def wrap():
            return func(*_dirList)

        def wrap_classmethod(self):
            return func(self, *_dirList)
        
        return (len(str(func.__qualname__).split('.')) > 1) and wrap_classmethod or wrap
    return decorator


def Add_Directory(directoryType, filePath):
    assert (type(directoryType) == EDirectory), 'err : wrong directory type input. (input key already)'
    
    FileConverterDirectory(directoryType, filePath)


def Del_Directory(directoryType):
    FileConverterDirectory.Del_Directory(directoryType)


def Get_DirectoryDic():
    return FileConverterDirectory.Get_DirectoryDic()


def Get_DirectoryByType(directoryType):
    _directoryDic = FileConverterDirectory.Get_DirectoryDic()

    assert (directoryType in _directoryDic.keys()), 'err : wrong directory type input. (key exist err){0}{1}'.format(directoryType, _directoryDic.keys())
    
    return _directoryDic[directoryType]


def Get_PathFromJson(directoryType):
    isMac = (platform.system() == "Darwin") and True or False
    jsonPath = (isMac) and 'Config/directory.json' or 'Config\\directory.json'

    with open (jsonPath) as file:
        file_json = json.load(file)
        directorySet = (isMac) and file_json['mac'] or file_json['windows']
    
    for key in directorySet:
        if key == directoryType:
            return directorySet[key]

    assert (False), 'err : input wrong directory type.'