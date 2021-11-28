from Package.Directory.directory_func import *
from Package.Data.config import *
from Package.Data.excel import *
from Package.Debug.log_func import *
import glob
import os

class Convert(Excel):
    def __init__(self):
        self._targetSheetName = Get_ConfigFromJson(EConfigType.excel, 'targetSheetName')
        self._columnNameNum = Get_ConfigFromJson(EConfigType.excel, 'columnNameNum')
        self._columnTypeNum = Get_ConfigFromJson(EConfigType.excel, 'columnTypeNum')
        self._keyColumnName = Get_ConfigFromJson(EConfigType.excel, 'keyColumnName')
        
        self._allExcelDataDict = self.Init_DataListFromExcel()

        self._dataIdDict = Get_ConfigFromJson(EConfigType.data_id, 'all')
        self._lastTidDict = Get_ConfigFromJson(EConfigType.last_tid, 'all')
        self._dataNameList = Get_ConfigKeyList(EConfigType.data_id)

        self._tidString = Get_ConfigFromJson(EConfigType.excel, 'tidString')


    @property
    def tidString(self):
        return self._tidString


    def Init_Tid(self, *dataNameList):
        """
        * Initalize data tid.
        * Input data name list to be initialize in data name list param.
        
        Example 1
        -------
        convert = Convert()

        convert.Init_Tid('dataName1', 'dataName2')
        
        * If want initialize all data tid, input magic keyword 'all (or All)' at data name list param.
        
        Example 2
        -------
        convert = Convert()

        convert.Init_Tid('all')
        """
        if (not len(dataNameList)) or dataNameList == None:
            return Write_Log(ELogTpye.warning, f'warning : no data list param input. (Init_Tid function.)')
        
        # if want initalize all data tid, input magic keyword 'all (or All)' at data name list param.
        if len(dataNameList) == 1 and (dataNameList[0] == 'all' or dataNameList[0] == 'All'):
            dataNameList = Get_ConfigKeyList(EConfigType.last_tid)

        for dataName in list(dataNameList):
            assert (dataName in Get_ConfigKeyList(EConfigType.last_tid)), f'err : {dataName} is not in Config Key List'
            
            Set_ConfigToJson(EConfigType.last_tid, dataName, 0)
        

    def Create_Tid(self, dataName):
        assert (dataName in self._dataNameList), f'err : {dataName} is not in data name list.'

        self._lastTidDict[dataName] += 1
        
        assert (self._lastTidDict[dataName] <= 999999), f'err : {dataName} tid overflow.'

        Set_ConfigToJson(EConfigType.last_tid, dataName, self._lastTidDict[dataName])
        
        return self._lastTidDict[dataName]


    @deco_usedirmethod(EDirectory.jsonDirectory)
    def Convert_ExcelToJson(self, dataName, jsonDir):
        assert (dataName in self._dataNameList), f'err : {dataName} is not in data name list.'

        _jsonPath = jsonDir + dataName + '.json'

        allJsonData = glob.glob('{0}*.json'.format(jsonDir))
        allJsonTidDict = {} # key = id / value = tid

        for jsonPath in allJsonData:
            _jsonName = str(os.path.basename(jsonPath)).split('.')[0]
            
            if dataName == _jsonName:
                with open (_jsonPath) as file:
                    try:
                        _jsonData =  json.load(file)
                        
                        for row in _jsonData:
                            allJsonTidDict[row[self._keyColumnName]] = row[self._tidString]

                    except KeyError:
                            Write_Log(ELogTpye.warning, f'worng json data row. {dataName} row : {row}')
                
                    except:
                        pass

        if not len(allJsonTidDict):
            _dumpList = []
            _rowData = {}

            for row in range(self._columnTypeNum + 1, self.Get_LenExcelRows(dataName)):
                _rowData.clear()
                
                _columnNum = 0
                while True:
                    _value = self.Get_ExcelValue(dataName, row, _columnNum)

                    if (not _value) and (not _columnNum in self.Get_NotNullableColumnList(dataName)):
                        _rowData[self.tidString] = self.Create_Tid(dataName)
                        _dumpList.append(dict(_rowData))
                        break

                    else:
                        if _columnNum in self.Get_NotNullableColumnList(dataName):
                            _rowData[self.Get_ExcelValue(dataName, self._columnNameNum, _columnNum)] = _value
                        
                        _columnNum += 1

        with open (_jsonPath, 'w') as file:
            json.dump(_dumpList, file, indent = 4)
                