from Package.ValidateCheck.validate import *

class EColumnProperty(Enum):
    design = auto()
    nullable = auto()
    unique = auto()
    normal = auto()


class NormalValidate(Validate):
    def __init__(self):
        super().__init__()


    @deco_validatelog
    def Check_KeyDuplicate(self, *checkDataList):
        _errCount = 0

        return _errCount


    @deco_validatelog
    def Check_ValueEmpty(self, *checkDataList):
        _errCount = 0

        return _errCount


    @deco_validatelog
    def Check_ValueDataType(self, *checkDataList):
        _errCount = 0

        return _errCount


    @deco_validatelog
    def Check_ValueUniqueValue(self, *checkDataList):
        _errCount = 0

        return _errCount


    def __Get_KeyColumnNum(self, dataName):
        pass