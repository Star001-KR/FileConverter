# 2021.09.21 / Code By Tae Hyung Kim.

from Package.Directory.directory_func import *
from Package.Debug.Log import *

Init_Directory()
print(Get_DirectoryDic())

print(FileConverterDirectory.Get_DirectoryDic()[EDirectory.logs])

Log()