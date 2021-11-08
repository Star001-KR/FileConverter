from Package.Directory.directory_func import *
from Package.Config.config import *

class Convert():
    def __init__(self):
        self._dataIdDict = Get_ConfigFromJson(EConfigType.data_id, 'all')
        self._lastTidDict = Get_ConfigFromJson(EConfigType.last_tid, 'all')

        self._jsonDir = self.Init_JsonDir()


    @deco_usedirmethod(EDirectory.jsonDirectory)
    def Init_JsonDir(self, jsonDir):
        return jsonDir