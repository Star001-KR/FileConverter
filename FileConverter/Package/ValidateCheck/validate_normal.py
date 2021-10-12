from Package.ValidateCheck.validate import *
from Package.ValidateCheck.decorator import *

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
        @deco_runvalicheck(self.Get_CheckDataList(*checkDataList))
        async def check_validate(dataName):
            _valueList = []
            _errCount = 0
            
            _loopCount = 0
            for rowNum in range(2, self.Get_LenExcelRows(dataName) - 1):
                _value = self.Get_ExcelValue(dataName, rowNum, self.Get_KeyColumnNum(dataName))
                _loopCount += 1

                if _value in _valueList:
                    Write_Log(ELogTpye.error, f'Key Duplicate : {dataName} - Row : {_loopCount}')
                    _errCount += 1
                    
                    continue

                _valueList.append(_value)

            return _errCount
        return check_validate
 

    @deco_validatelog
    def Check_ValueEmpty(self, *checkDataList):
        @deco_runvalicheck(self.Get_CheckDataList(*checkDataList))
        async def check_validate(dataName):
            _notNullableColumnList = self.Get_NotNullableColumnList(dataName)
            _errCount = 0

            for row in range(2, self.Get_LenExcelRows(dataName) - 1):
                for col in _notNullableColumnList:
                    if self.Get_ExcelValue(dataName, row, col) == None or self.Get_ExcelValue(dataName, row, col) == '':
                        Write_Log(ELogTpye.error, f'Empty Value : {dataName} - Row : {row + 1} / Column : {col + 1}')
                        _errCount += 1

            return _errCount
        return check_validate


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


    def Get_KeyColumnNum(self, dataName):
        _targetData = self.Get_ExcelData(dataName)
        _columnNum = 0

        for column in _targetData[self.Get_ColumnNameNum()]:
            if column.value == self.Get_KeyColomnName():
                return _columnNum
            
            _columnNum += 1

        Write_Log(ELogTpye.error, f'No [{self.Get_KeyColomnName()} Column] in [{dataName} Data Table]')
        return False