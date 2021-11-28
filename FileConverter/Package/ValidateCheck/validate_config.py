from Package.Data.excel import *
from Package.ValidateCheck.decorator import *

class ConfigValidate(Excel):
    """
    Excel data validation with reference to vaildation config yaml file.
    
    Example
    -------
    @deco_validatelog
    def Check_ValueSizeCompare(self, *checkDataList):
        @deco_valiconfigsplit(EValidationConfigType.ref_validation)
        def check_validate(checkDict : dict):
            errCount = 0
            checkDataSet = self.__Get_CheckDataSet(checkDict, *checkDataList)

            # Validate Check Code.

            return errCount
        return check_validate()
    """
    def __init__(self):
        super().__init__()


    def Check_AllValidate_Config(self, *checkDataList):
        self.Check_RefValue(*checkDataList)
        self.Check_ValueSizeCompare(*checkDataList)


    @deco_validatelog
    def Check_RefValue(self, *checkDataList):
        @deco_valiconfigsplit(EValidationConfigType.ref_validation)
        def check_validate(checkDict : dict):
            errCount = 0
            checkDataSet = self.__Get_CheckDataSet(checkDict, *checkDataList)
            
            for (key, value) in checkDict.items():
                if not str(key).split('.')[0] in checkDataSet:
                    continue
                
                _checkDataTable = str(key).split('.')[0]
                _checkColumnName = str(key).split('.')[1]
                _checkColumnNum = self.Get_ColumnNum(_checkDataTable, _checkColumnName)
                
                for checkDataRow in range(2, self.Get_LenExcelRows(_checkDataTable)):
                    _checkData = self.Get_ExcelValue(_checkDataTable, checkDataRow, _checkColumnNum)
                    
                    _refDataTable = str(value).split('.')[0]
                    _refColumnName = str(value).split('.')[1]
                    _refColumnNum = self.Get_ColumnNum(_refDataTable, _refColumnName)
                    
                    _isFine = False
                    for refDataRow in range(2, self.Get_LenExcelRows(_refDataTable)):
                        if self.Get_ExcelValue(_refDataTable, refDataRow, _refColumnNum) == _checkData:
                            _isFine = True
                            break
                    
                    if not _isFine:
                        Write_Log(ELogTpye.error, f'Ref Value : {_checkDataTable} - Column : {_checkColumnNum + 1} / Row : {checkDataRow + 1}')
                        errCount += 1
            
            return errCount
        return check_validate()


    @deco_validatelog
    def Check_ValueSizeCompare(self, *checkDataList):
        @deco_valiconfigsplit(EValidationConfigType.value_size_compare)
        def check_validate(checkDict : dict):
            errCount = 0
            checkDataSet = self.__Get_CheckDataSet(checkDict, *checkDataList)
            
            for (key, value) in checkDict.items():
                if not str(key).split('.')[0] in checkDataSet:
                    continue
                
                assert str(key).split('.')[0] == str(value).split('.')[0], f'err : small data table is not same from big data table.({str(key).split(".")[0]} / {str(value).split(".")[0]})'

                _checkDataTable = str(key).split('.')[0]

                _checkColumnName_big = str(key).split('.')[1]
                _checkColumnNum_big = self.Get_ColumnNum(_checkDataTable, _checkColumnName_big)

                _checkColumnName_small = str(value).split('.')[1]
                _checkColumnNum_small = self.Get_ColumnNum(_checkDataTable, _checkColumnName_small)

                for row in range(2, self.Get_LenExcelRows(_checkDataTable)):
                    if self.Get_ExcelValue(_checkDataTable, row, _checkColumnNum_big) == None or self.Get_ExcelValue(_checkDataTable, row, _checkColumnNum_small) == None:
                        continue

                    elif not self.Get_ExcelValue(_checkDataTable, row, _checkColumnNum_big) >= self.Get_ExcelValue(_checkDataTable, row, _checkColumnNum_small):
                        Write_Log(ELogTpye.error, f'Value Size : {_checkDataTable} - BigColumn : {_checkColumnNum_big + 1}, SmallColumn : {_checkColumnNum_small + 1} / Row : {row + 1}')
                        errCount += 1

            return errCount
        return check_validate()


    def __Get_CheckDataSet(self, checkDict, *checkDataList):
        checkDataSet = set()

        if not len(checkDataList):
            for key in checkDict.keys():
                checkDataSet.add(str(key).split('.')[0])
            
        else:
            for data in checkDataList:
                for key in checkDict.keys():
                    if data == str(key).split('.')[0]:
                        checkDataSet.add(data)

        return checkDataSet