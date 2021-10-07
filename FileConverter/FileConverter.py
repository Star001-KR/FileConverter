# 2021.09.21 / Code By Tae Hyung Kim.

from Package.Debug.log_func import *
from Package.Directory.directory_func import *
from Package.ValidateCheck.validate_set import *


def Init_Tool():
    Init_Log(False)
    
    Write_Log(ELogTpye.normal, 'Init Directory, Log.')


if __name__ == '__main__':
    Init_Tool()
    test = Validate()

    a = NormalValidate()
    a. Check_KeyDuplicate(1)