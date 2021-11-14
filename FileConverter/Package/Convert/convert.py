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
        if (not len(dataNameList)) or dataNameList == None:
            return Write_Log(ELogTpye.warning, f'warning : no data list param input. (Init_Tid function.)')
        
        for dataName in list(dataNameList):
            assert (dataName in Get_ConfigKeyList(EConfigType.last_tid)), f'err : {dataName} is not in Config Key List'
            
            Set_ConfigToJson(EConfigType.last_tid, dataName, 0)