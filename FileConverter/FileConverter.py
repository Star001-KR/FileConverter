# 2021.11.20 / Code By Tae Hyung Kim.

from Package.Debug.log_func import *
from Package.Directory.directory_func import *
from Package.ValidateCheck.validate_set import *
from Package.Convert.convert import *

def Init_Tool():
    Init_Log(False)
    
    Write_Log(ELogTpye.normal, 'Init Directory, Log.')


if __name__ == '__main__':
    Init_Tool()
    Check_AllValidate()

    a = Convert()

    for dataName in a._dataNameList:
        a.Convert_ExcelToJson(dataName)
    