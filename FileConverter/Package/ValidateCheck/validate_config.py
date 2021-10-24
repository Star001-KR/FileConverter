from Package.ValidateCheck.validate import *
from Package.ValidateCheck.decorator import *

class ConfigValidate(Validate):
    """
    Excel data validation with reference to vaildation config yaml file.
    
    Example
    -------
    @deco_validatelog
    def Check_RefValue(self, *checkDataList):
        @deco_valiconfigsplit(EValidationConfigType.ref_validation)
        def check_validate(parantKeyList, parantValueList, childKeyList, childValueList):
            _errCount = 0

            # Validate Check Code.

            return _errCount
        return check_validate
    """
    def __init__(self):
        super().__init__()


    @deco_validatelog
    def Check_RefValue(self, *checkDataList):
        @deco_valiconfigsplit(EValidationConfigType.ref_validation)
        def check_validate(parantKeyList, parantValueList, childKeyList, childValueList):
            _errCount = 0

            

            return _errCount
        return check_validate


    @deco_validatelog
    def Check_ValueSizeCompare(self, *checkDataList):
        _errCount = 0

        return _errCount