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
    def Init_Directory(cls):
        pass


    @classmethod
    def Set_Directory(cls):
        pass


    @classmethod
    def Get_DirectoryDic(cls):
        return cls.directoryDic