from Package.ValidateCheck.validate import *
from Package.ValidateCheck.decorator import *

class ConfigValidate(Validate):
    def __init__(self):
        super().__init__()


    @deco_validatelog
    def Check_RefValue(self, *checkDataList):
        _errCount = 0

        return _errCount


    @deco_validatelog
    def Check_ValueSizeCompare(self, *checkDataList):
        _errCount = 0

        return _errCount