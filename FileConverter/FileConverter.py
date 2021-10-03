# 2021.09.21 / Code By Tae Hyung Kim.

from Package.Debug.log_func import *
from Package.Directory.directory_func import *
from Package.ValidateCheck.validate import *


def Init_Tool():
    Init_Log(False)
    
    Write_Log(ELogTpye.normal, 'Init Directory, Log.')
    

@deco_usedirmethod([EDirectory.excelDirectory, EDirectory.jsonDirectory])
def test ():
    print(test)

if __name__ == '__main__':
    Init_Tool()
