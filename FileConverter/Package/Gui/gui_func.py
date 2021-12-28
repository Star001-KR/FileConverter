from Package.Debug.log_func import *
from Package.Directory.directory_func import *
from Package.ValidateCheck.validate_set import *
from Package.Convert.convert import *

def press_btn_runAll():
    if (Check_AllValidate()):
        convert = Convert()

        for excelName in convert.Get_AllExcelList():
                convert.Convert_ExcelToJson(excelName)
    
    Write_Log(ELogTpye.normal, '----------------------------------------------------------------')
    Write_Log(ELogTpye.normal, 'Complete Run All.')