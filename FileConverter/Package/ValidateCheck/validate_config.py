from Package.ValidateCheck.validate import *
from Package.ValidateCheck.decorator import *
from Package.Config.config import *

class ConfigValidate(Validate):
    """
    Excel data validation with reference to vaildation config yaml file.
    
    Example
    -------
    @deco_validatelog
    def Check_ExampleValiDef(self, *checkDataList):
        @deco_runvalicheck(self.Get_CheckDataList(*checkDataList))
        async def check_validate(dataName):
            _errCount = 0

            # Validate Check Code.

            return _errCount
        return check_validate
    """
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


def deco_valiconfigsplit(configType):
    def get_valiDataNColumn(configType):
        assert type(configType) == EValidationConfigType, f'err : wrong config tpye input. (input data type : {type(configType)})'

        _checkDict : dict = Get_ConifgFromYaml(configType)

        _parantKeyList = []
        _parantValueList = []

        _childKeyList = []
        _childValueList = []

        for (key, value) in _checkDict.items():
            _parantKeyList.append(str(key).split('.')[0])
            _parantValueList.append(str(key).split('.')[1])
            
            _childKeyList.append(str(value).split('.')[0])
            _childValueList.append(str(value).split('.')[1])
        
        return (_parantKeyList, _parantValueList, _childKeyList, _childValueList)

    def decorator(validate_func):
        def wrap():
            (_parantKeyList, _parantValueList, _childKeyList, _childValueList) = get_valiDataNColumn(configType)

            return validate_func()

        return wrap
    return decorator