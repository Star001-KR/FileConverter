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


def press_btn_fileConvert(checkExcelDict):
     assert (type(checkExcelDict) == dict), 'err : wrong data type input.'

     if (Check_AllValidate()):
          convert = Convert()
          excelNameList = []

          for key, value in checkExcelDict.items():
               if value.get() == 1:
                    excelNameList.append(key)

          for excelName in excelNameList:
               convert.Convert_ExcelToJson(excelName)

     Write_Log(ELogTpye.normal, '----------------------------------------------------------------')
     Write_Log(ELogTpye.normal, 'Complete Run.')


def press_btn_validateCheck():
     if (Check_AllValidate()):
          pass
     
     Write_Log(ELogTpye.normal, '----------------------------------------------------------------')
     Write_Log(ELogTpye.normal, 'Complete Validate Check.')
