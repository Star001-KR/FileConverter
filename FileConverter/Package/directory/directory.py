from enum import Enum, auto

class EDirectory(Enum):
    excelDirectory = auto()
    allExcelDirectory = auto()
    jsonDirectory = auto()
    gameConfigDirectory = auto()
    validationDirectory = auto()


class Directory:
    def __init__(self):
        pass


    def Get_Directory(self):
        pass


    def Set_Directory(self):
        pass


class FileConverterDirectory(Directory):
    directoryDic = {}

    def __init__(self, directoryType, filePath):
        self.directoryDic[directoryType] = filePath


    @classmethod
    def Init_Directory(cls):
        pass


    @classmethod
    def Set_Directory(cls):
        pass


def Init_Directory():
    

    while (True):
        yield