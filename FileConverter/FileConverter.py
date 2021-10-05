# 2021.09.21 / Code By Tae Hyung Kim.

from Package.Debug.log_func import *
from Package.Directory.directory_func import *
from Package.ValidateCheck.validate import *


def Init_Tool():
    Init_Log(False)
    
    Write_Log(ELogTpye.normal, 'Init Directory, Log.')
    

if __name__ == '__main__':
    Init_Tool()
    test = Validate()

    print(test.Get_ExcelValue('Monster', 0, 5))