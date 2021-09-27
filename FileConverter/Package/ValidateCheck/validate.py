from Package.Directory.directory_func import *
from Package.Debug.Error import *
import openpyxl
import yaml

class Validate():
    def __init__(self):
        self._targetSheetName = "Sheet1"
        self._targetExcelDataDic = {}
        pass


class NormalValidate(Validate):
    def __init__(self):
        super().__init__()


class ConfigValidate(Validate):
    def __init__(self):
        super().__init__()


def Get_ExcelDataToLib(directoryList, targetSheetName):
    try:
        if type(directoryList) == str:
            pass

        elif type(directoryList) == list:
            pass

        else:
            raise ParamDataTypeError
            #return 'err : wrong directory type input. (need str or list)'

    except ParamDataTypeError:
        pass

    except:
        pass