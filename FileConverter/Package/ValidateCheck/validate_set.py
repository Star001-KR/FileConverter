from Package.ValidateCheck.validate_normal import *
from Package.ValidateCheck.validate_config import *

class ValidateSet(NormalValidate, ConfigValidate):
    def __init__(self):
        super().__init__()


@deco_startvalidatelog
def Check_AllValidate(*checkDataList):
    ErrCount.Init_ErrorCount()

    ValidateSet().Check_AllValidate_Config(*checkDataList)
    ValidateSet().Check_AllValidate_Normal(*checkDataList)

    if not ErrCount.Get_ErrCount():
        return True

    else:
        Write_Log(ELogTpye.warning, 'failed file conversion. (find validate error(s).)')
        
        return False


@deco_startvalidatelog
def Check_ConfigValidate(*checkDataList):
    ValidateSet().Check_AllValidate_Config(*checkDataList)


@deco_startvalidatelog
def Check_NormalValidate(*checkDataList):
    ValidateSet().Check_AllValidate_Normal(*checkDataList)