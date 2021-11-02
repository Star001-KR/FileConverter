from Package.ValidateCheck.validate import *
from Package.ValidateCheck.decorator import *

class ConfigValidate(Validate):
    """
    Excel data validation with reference to vaildation config yaml file.
    
    Example
    -------
    @deco_validatelog
    def Check_RefValue(self, *checkDataList):
        @deco_valiconfigsplit(EValidationConfigType.ref_validation)
        def check_validate(parantKeyList, parantValueList, childKeyList, childValueList):
            _errCount = 0

            # Validate Check Code.

            return _errCount
        return check_validate
    """
    def __init__(self):
        super().__init__()


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
        _errCount = 0

        return _errCount


    def __Get_CheckDataSet(self, checkDict, *checkDataList):
        _checkDataSet = set()

        if not len(checkDataList):
            for key in checkDict.keys():
                _checkDataSet.add(str(key).split('.')[0])
            
        else:
            for data in checkDataList:
                for key in checkDict.keys():
                    if data == str(key).split('.')[0]:
                        _checkDataSet.add(data)

        return _checkDataSet