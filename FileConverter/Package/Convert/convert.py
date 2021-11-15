from Package.Directory.directory_func import *
from Package.Config.config import *
from Package.Debug.log_func import *

class Convert():
    def __init__(self):
        self._dataIdDict = Get_ConfigFromJson(EConfigType.data_id, 'all')
        self._lastTidDict = Get_ConfigFromJson(EConfigType.last_tid, 'all')

        self._jsonDir = self.Init_JsonDir()


    @deco_usedirmethod(EDirectory.jsonDirectory)
    def Init_JsonDir(self, jsonDir):
        return jsonDir


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