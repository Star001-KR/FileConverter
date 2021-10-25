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
        def check_validate(checkDict : dict):
            _errCount = 0
            _checkDataSet = set()

            if not len(checkDataList):
                for key in checkDict.keys():
                    _checkDataSet.add(str(key).split('.')[0])
            
            else:
                for data in checkDataList:
                    for key in checkDict.keys():
                        if data == str(key).split('.')[0]:
                            _checkDataSet.add(data)
            
            for (key, value) in checkDict.items():
                if not str(key).split('.')[0] in _checkDataSet:
                    continue

                _parentData = str(key).split('.')[0]

            return _errCount
        return check_validate()


    @deco_validatelog
    def Check_ValueSizeCompare(self, *checkDataList):
        _errCount = 0

        return _errCount