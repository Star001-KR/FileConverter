from Package.Directory.directory_func import *
from Package.Config.config import *
from Package.Debug.log_func import *
import glob
import os

class Convert():
    def __init__(self):
        self._dataIdDict = Get_ConfigFromJson(EConfigType.data_id, 'all')
        self._lastTidDict = Get_ConfigFromJson(EConfigType.last_tid, 'all')
        self._dataNameList = Get_ConfigKeyList(EConfigType.data_id)


    def Init_Tid(self, *dataNameList):
        """
        Initalize data tid.
        Input data name list to be initialize in data name list param.
        
        Example 1
        -------
        convert = Convert()

        convert.Init_Tid('dataName1', 'dataName2')
        
        If want initialize all data tid, input magic keyword 'all (or All)' at data name list param.
        
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

        last_tid = self._lastTidDict[dataName]
        last_tid += 1
        
        assert (last_tid <= 999999), f'err : {dataName} tid overflow.'

        Set_ConfigToJson(EConfigType.last_tid, dataName, last_tid)
        
        return last_tid


    @deco_usedirmethod(EDirectory.jsonDirectory)
    def Convert_ExcelToJson(self, dataName, jsonDir):
        assert (dataName in self._dataNameList), f'err : {dataName} is not in data name list.'

        allJsonData = glob.glob('{0}*.json'.format(jsonDir))
        allJsonTidDict = {} # key = data name / value = tid

        for jsonPath in allJsonData:
            _jsonName = str(os.path.basename(jsonPath)).split('.')[0]
            
            if dataName == _jsonName:
                return

        _jsonPath = jsonDir + dataName + '.json'
        with open (_jsonPath, 'w') as file:
            pass