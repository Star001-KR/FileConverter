# 2021.12.06 / Code By Tae Hyung Kim.

from Package.Debug.log_func import *
from Package.Directory.directory_func import *
from Package.ValidateCheck.validate_set import *
from Package.Convert.convert import *
from Package.Gui.main_screen import *

def Init_Tool():
    Init_Log(False)
    
    Write_Log(ELogTpye.normal, 'Init Directory, Log.')


if __name__ == '__main__':
    Init_Tool()
    Check_AllValidate()

    a = Convert()
    b = MainScreen()

    for excelName in a.Get_AllExcelList():
        a.Convert_ExcelToJson(excelName)

    print(b.title)
    print(b.resizable)