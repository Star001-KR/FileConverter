from Package.Directory.directory import *
import json
import platform

def deco_usedirmethod(directoryType):
    assert (type(directoryType) == EDirectory) or (type(directoryType) == list), 'err : wrong data type input.'

    _dirList = []
    
    def appear_dirList(dirType):
        if not FileConverterDirectory.Is_InitDirectoryType(dirType):
            FileConverterDirectory(dirType, Get_PathFromJson(str(dirType).split('.')[1]))

        _dirList.append(Get_DirectoryByType(dirType))

    def decorator(func):
        def wrap(*args):
            def inner_param_0():
                return func(*_dirList)
            
            def inner_param_1(param1):
                return func(param1, *_dirList)

            def inner_param_2(param1, param2):
                return func(param1, param2, *_dirList)

            def inner_param_3(param1, param2, param3):
                return func(param1, param2, param3, *_dirList)

            _lenParam = len(args)

            if _lenParam == 0:
                return inner_param_0()

            elif _lenParam == 1:
                return inner_param_1(args[0])

            elif _lenParam == 2:
                return inner_param_2(args[0], args[1])

            elif _lenParam == 3:
                return inner_param_3(args[0], args[1], args[2])

        if (type(directoryType) == EDirectory):
            appear_dirList(directoryType)

        else:
            for _dirType in directoryType:
                assert (type(_dirType) == EDirectory), 'err : wrong data type in directoryType list.'
                
                appear_dirList(_dirType)
        
        return wrap
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