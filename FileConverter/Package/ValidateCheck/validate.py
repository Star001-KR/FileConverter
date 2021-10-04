from Package.Directory.directory_func import *
from Package.Debug.Error import *
from Package.Debug.log_func import *
import openpyxl
import yaml
import glob
import os

class EConfigType(Enum):
    excel : auto()


class Validate():
    def __init__(self):
        self._targetSheetName = Get_ConfigFromJson(EConfigType.excel, 'targetSheetName')
        self._columnNameNum = Get_ConfigFromJson(EConfigType.excel, 'columnNameNum')
        self._keyColumnName = Get_ConfigFromJson(EConfigType.excel, 'keyColumnName')
        self._targetExcelDataDic = {}
    

    @deco_usedirmethod(EDirectory.excelDirectory)
    def Init_DataListFromExcel(self, exceDir):
        def get_excelSheetDataDict(excelDir, targetSheetName):
            _excelName = str(os.path.basename(excelDir)).split('.')[0]
            
            EXCEL_FILE = openpyxl.load_workbook(excelDir)
            
            for sheetName in EXCEL_FILE.sheetnames:
                if sheetName == targetSheetName:
                    pass
        
        _allExcelData = glob.glob('{0}*.xlsx'.format(exceDir))

        for excelDir in _allExcelData:
            
            get_excelSheetDataDict(excelDir, self._targetSheetName)
        pass


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