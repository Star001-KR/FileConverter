from enum import Enum, auto

class EDirectory(Enum):
    excelDirectory = auto()
    jsonDirectory = auto()
    gameConfigDirectory = auto()
    validationDirectory = auto()
    logs = auto()


class FileConverterDirectory():
    directoryDic = {}

    def __init__(self, directoryType, filePath):
        self.directoryDic[directoryType] = filePath


    @classmethod
    def Set_Directory(cls, directoryType, filePath):
        assert (directoryType in cls.directoryDic.keys), 'err : wrong directory type input. (key exist err)'
        cls.directoryDic[directoryType] = filePath


    @classmethod
    def Del_Directory(cls, directoryType):
        assert (directoryType in cls.directoryDic.keys), 'err : wrong directory type input. (key exist err)'
        del cls.directoryDic[directoryType]


    @classmethod
    def Get_DirectoryDic(cls):
        return cls.directoryDic


    @classmethod
    def Is_InitDirectoryType(cls, directoryType):
        assert type(directoryType) == EDirectory, 'err : wrong directory type input.'

        return (directoryType in cls.directoryDic.keys()) and True or False