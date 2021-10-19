from Package.ValidateCheck.validate import *
from Package.ValidateCheck.decorator import *
import yaml

class ConfigValidate(Validate):
    def __init__(self):
        super().__init__()
        self._validationDir = self.Init_ValidationConfig_Dir()


    @deco_usedirmethod(EDirectory.validationDirectory)
    def Init_ValidationConfig_Dir(self, yamlDir):
        return yamlDir


    @deco_validatelog
    def Check_RefValue(self, *checkDataList):
        _errCount = 0

        return _errCount


    @deco_validatelog
    def Check_ValueSizeCompare(self, *checkDataList):
        _errCount = 0

        return _errCount