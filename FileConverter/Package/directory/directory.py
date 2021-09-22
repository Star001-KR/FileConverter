from enum import Enum, auto

class EDirectory(Enum):
    excelDirectory = auto()
    allExcelDirectory = auto()
    jsonDirectory = auto()
    gameConfigDirectory = auto()
    validationDirectory = auto()


class FileConverterDirectory():
    directoryDic = {}

    def __init__(self, directoryType, filePath):
        self.directoryDic[directoryType] = filePath


    @classmethod
    def Set_Directory(cls, directoryType, filePath):
        if not directoryType in cls.directoryDic.keys:
            return 'err : wrong directory type input. (key exist err)'

        else:
            cls.directoryDic[directoryType] = filePath


    @classmethod
    def Del_Directory(cls, directoryType):
        if not directoryType in cls.directoryDic.keys:
            return 'err : wrong directory type input. (key exist err)'
        
        else:
            del cls.directoryDic[directoryType]


    @classmethod
    def Get_DirectoryDic(cls):
        return cls.directoryDic