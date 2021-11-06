from Package.ValidateCheck.validate_normal import *
from Package.ValidateCheck.validate_config import *

class ValidateSet(NormalValidate, ConfigValidate):
    def __init__(self):
        super().__init__()


@deco_startvalidatelog
def Check_AllValidate(*checkDataList):
    Write_Log(ELogTpye.normal, '----------------------------------------------------------------')
    Write_Log(ELogTpye.normal, 'Start Check All Validate.')
    
    ValidateSet().Check_AllValidate_Config(*checkDataList)
    ValidateSet().Check_AllValidate_Normal(*checkDataList)


@deco_startvalidatelog
def Check_AllValidate_Config(*checkDataList):
    Write_Log(ELogTpye.normal, '----------------------------------------------------------------')
    Write_Log(ELogTpye.normal, 'Start Check All Config Validate.')
    
    ValidateSet().Check_AllValidate_Config(*checkDataList)


@deco_startvalidatelog
def Check_AllValidate_Normal(*checkDataList):
    Write_Log(ELogTpye.normal, '----------------------------------------------------------------')
    Write_Log(ELogTpye.normal, 'Start Check All Normal Validate.')
    
    ValidateSet().Check_AllValidate_Normal(*checkDataList)