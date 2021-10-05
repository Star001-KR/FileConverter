from Package.Directory.directory_func import *
from Package.Debug.Error import *
from Package.Debug.log_func import *
import enum
import openpyxl
import yaml
import glob
import os

class EConfigType(Enum):
    excel = auto()


class Validate():
    def __init__(self):
        self._targetSheetName = Get_ConfigFromJson(EConfigType.excel, 'targetSheetName')
        self._columnNameNum = Get_ConfigFromJson(EConfigType.excel, 'columnNameNum')
        self._keyColumnName = Get_ConfigFromJson(EConfigType.excel, 'keyColumnName')
        
        self._allExcelDataDict = self.Init_DataListFromExcel()
    

    @deco_usedirmethod(EDirectory.excelDirectory)
    def Init_DataListFromExcel(self, exceDir):
        def get_excelSheetDataDict(excelDir, targetSheetName):
            _excelName = str(os.path.basename(excelDir)).split('.')[0]
            
            EXCEL_FILE = openpyxl.load_workbook(excelDir)
            
            for sheetName in EXCEL_FILE.sheetnames:
                if sheetName == targetSheetName:
                    _dataDict = {}
                    _rowNum = 0

                    for rowData in EXCEL_FILE[sheetName].rows:
                        _dataDict[_rowNum] = rowData
                        _rowNum += 1

                    return _dataDict

            Write_Log(ELogTpye.warning, f'warning : no target sheet in [ {_excelName} ] excel data.')

            return False
        
        _allExcelData = glob.glob('{0}*.xlsx'.format(exceDir))
        _allExcelDataDict = {}

        for excelDir in _allExcelData:
            _excelName = str(os.path.basename(excelDir)).split('.')[0]
            _excelDataDict = get_excelSheetDataDict(excelDir, self._targetSheetName)

            if not _excelDataDict:
                Write_Log(ELogTpye.warning, f'continue push [ {_excelName} ] excel data.')
                continue

            _allExcelDataDict[_excelName] = _excelDataDict

        return _allExcelDataDict
                
        
class NormalValidate(Validate):
    def __init__(self):
        super().__init__()


class ConfigValidate(Validate):
    def __init__(self):
        super().__init__()


def Get_ConfigFromJson(configType, configCategory):
    assert (type(configType) == EConfigType), 'err : wrong param data type input.'
    if configType == EConfigType.excel:
        _configTypeName = 'excel'

    isMac = (platform.system() == "Darwin") and True or False
    jsonPath = (isMac) and 'Config/config.json' or 'Config\\config.json'
    
    with open (jsonPath) as file:
        file_json = json.load(file)
        configSet = file_json[_configTypeName]

    for config in configSet:
        if config == configCategory:
            return configSet[config]

    assert (False), 'err : input wrong config category.'