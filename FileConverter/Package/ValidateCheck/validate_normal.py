from Package.ValidateCheck.validate import *

class EColumnProperty(Enum):
    design = auto()
    nullable = auto()
    unique = auto()
    normal = auto()


class NormalValidate(Validate):
    def __init__(self):
        super().__init__()


    @deco_validatelog
    def Check_KeyDuplicate(self, *checkDataList):
        _checkDataList = self.Get_CheckDataList(*checkDataList)
        _errCount = 0
        # 재귀함수 이용
        # for dataName in _checkDataList:
        #     for data in range(0, )
        #     pass

        return _errCount


    @deco_validatelog
    def Check_ValueEmpty(self, *checkDataList):
        _checkDataList = self.Get_CheckDataList(*checkDataList)
        _errCount = 0

        return _errCount


    @deco_validatelog
    def Check_ValueDataType(self, *checkDataList):
        _checkDataList = self.Get_CheckDataList(*checkDataList)
        _errCount = 0

        return _errCount


    @deco_validatelog
    def Check_ValueUniqueValue(self, *checkDataList):
        _checkDataList = self.Get_CheckDataList(*checkDataList)
        _errCount = 0

        return _errCount


    def __Get_KeyColumnNum(self, dataName):
        _targetData = self.Get_ExcelData(dataName)
        _columnNum = 0

        for column in _targetData[self.Get_ColumnNameNum()]:
            if column.value == self.Get_KeyColomnName():
                return _columnNum
            
            _columnNum += 1

        Write_Log(ELogTpye.error, f'No [{self.Get_KeyColomnName()} Column] in [{dataName} Data Table]')
        return False