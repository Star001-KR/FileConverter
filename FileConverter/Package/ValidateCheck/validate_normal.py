from Package.ValidateCheck.validate import *
from Package.ValidateCheck.decorator import *

class EColumnProperty(Enum):
    design = auto()
    nullable = auto()
    unique = auto()
    normal = auto()


class NormalValidate(Validate):
    """
    Validation by excel data table unit (without config.json).
    
    Example
    -------
    @deco_validatelog
    def Check_ExampleValiDef(self, *checkDataList):
        @deco_runvalicheck(self.Get_CheckDataList(*checkDataList))
        async def check_validate(dataName):
            _errCount = 0

            # Validate Check Code.

            return _errCount
        return check_validate
    """
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
        @deco_runvalicheck(self.Get_CheckDataList(*checkDataList))
        async def check_validate(dataName):
            _dataTypeList = []
            _notNullableColumnList = self.Get_NotNullableColumnList(dataName)
            _errCount = 0

            _columnNum = 0
            while True:
                _typeValue = self.Get_ExcelValue(dataName, self.columnTypeNum, _columnNum)

                if not _typeValue:
                    break

                _dataTypeList.append(_typeValue)
                _columnNum += 1
            
            if not type(_notNullableColumnList) == bool:
                for row in range(2, self.Get_LenExcelRows(dataName) - 1):
                    for col in range(0, _columnNum):
                        _value = self.Get_ExcelValue(dataName, row, col)

                        if _value == None and not col in _notNullableColumnList:
                            continue
                        
                        if _dataTypeList[col].startswith('int'):
                            if not type(_value) == int:
                                Write_Log(ELogTpye.error, f'Data Type : {dataName} - Row : {row + 1} / Column : {col + 1}')
                                _errCount += 1

                        elif _dataTypeList[col].startswith('float'):
                            if not type(_value) == float and not type(_value) == int:
                                Write_Log(ELogTpye.error, f'Data Type : {dataName} - Row : {row + 1} / Column : {col + 1}')
                                _errCount += 1

            return _errCount
        return check_validate


    @deco_validatelog
    def Check_ValueUniqueValue(self, *checkDataList):
        @deco_runvalicheck(self.Get_CheckDataList(*checkDataList))
        async def check_validate(dataName):
            _uniqueColumnList = self.Get_UniqueColumnList(dataName)
            _errCount = 0

            _valueList = []
            if not type(_uniqueColumnList) == bool or _uniqueColumnList:
                for col in _uniqueColumnList:

                    _valueList.clear()
                    for row in range(2, self.Get_LenExcelRows(dataName) - 1):
                        _value = self.Get_ExcelValue(dataName, row, col)

                        if _value in _valueList:
                            Write_Log(ELogTpye.error, f'Unique Value : {dataName} - Row : {row + 1} / Column : {col + 1}')
                            _errCount += 1

                            continue

                        _valueList.append(_value)

            return _errCount
        return check_validate