# 2021.10.25 / Code By Tae Hyung Kim.

from Package.Debug.log_func import *
from Package.Directory.directory_func import *
from Package.ValidateCheck.validate_set import *

def Init_Tool():
    Init_Log(False)
    
    Write_Log(ELogTpye.normal, 'Init Directory, Log.')


if __name__ == '__main__':
    Init_Tool()
    a = ValidateSet()

    a.Check_KeyDuplicate()
    a.Check_ValueEmpty()
    a.Check_ValueDataType()
    a.Check_ValueUniqueValue()

    a.Check_RefValue()
