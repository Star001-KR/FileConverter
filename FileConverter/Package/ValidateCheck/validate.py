from Package.Directory.directory_func import *
from Package.Debug.Error import *
from Package.Debug.log_func import *
from Package.Config.config import *
import openpyxl
import glob
import os

class Validate():
    def __init__(self):
        self._targetSheetName = Get_ConfigFromJson(EConfigType.excel, 'targetSheetName')
        self._columnNameNum = Get_ConfigFromJson(EConfigType.excel, 'columnNameNum')
        self._columnTypeNum = Get_ConfigFromJson(EConfigType.excel, 'columnTypeNum')
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
                Write_Log(ELogTpye.warning, f'warning : continue push [ {_excelName} ] excel data.')
                continue

            _allExcelDataDict[_excelName] = _excelDataDict

        return _allExcelDataDict


    def Get_ColumnNameNum(self):
        return self._columnNameNum


    def Get_KeyColomnName(self):
        return self._keyColumnName


    def Get_ColumnTypeNum(self):
        return self._columnTypeNum


    def Get_NotNullableColumnList(self, excelName):
        assert (type(excelName) == str), f'err : wrong param data type input. ({type(excelName)})'
        if not (excelName in self._allExcelDataDict.keys()):
            assert (False), 'err : wrong param input. (no excel name in all excel data names.)'

        _columnList = []

        _columnNum = 0
        while True:
            _value = self.Get_ExcelValue(excelName, self._columnTypeNum, _columnNum)

            if not _value:
                return _columnList

            else:
                if not _value[len(_value) - 1 : ] == '?':
                    _columnList.append(_columnNum)

            _columnNum += 1


    def Get_ExcelData(self, excelName):
        assert (type(excelName) == str), f'err : wrong param data type input. ({type(excelName)})'
        if not (excelName in self._allExcelDataDict.keys()):
            assert (False), 'err : wrong param input. (no excel name in all excel data names.)'
        
        return self._allExcelDataDict[excelName]


    def Get_ExcelValue(self, excelName, rowNum, colNum):
        assert (type(excelName) == str), 'err : wrong param data type input.'
        if not (excelName in self._allExcelDataDict.keys()):
            assert (False), 'err : wrong param input. (no excel name in all excel data names.)'

        _excelData = self._allExcelDataDict[excelName]
        
        try:
            return _excelData[rowNum][colNum].value

        except:
            return False


    def Get_CheckDataList(self, *checkDataList):
        if not len(checkDataList):
            _dataNameList = [dataName for dataName in self._allExcelDataDict.keys()]

            return _dataNameList
            
        return checkDataList


    def Get_LenExcelRows(self, excelName):
        return len(self.Get_ExcelData(excelName).keys())