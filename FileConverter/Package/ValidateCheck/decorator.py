from Package.Debug.log_func import *
from Package.Config.config import *
import asyncio
import glob

def deco_validatelog(validate_func):
    def Write_StartLog(checkTypeStr):
        Write_Log(ELogTpye.normal, '----------------------------------------------------------------')
        Write_Log(ELogTpye.normal, f'Start Validate Check : {__CheckType_checkTypeStr(checkTypeStr)}')


    def Write_EndLog(checkTypeStr, errorCount):
        Write_Log(ELogTpye.normal, f'Complete Validate Check : {__CheckType_checkTypeStr(checkTypeStr)}')
        if errorCount:
            Write_Log(ELogTpye.warning, f'(Find {errorCount} Error(s).)')


    def __CheckType_checkTypeStr(checkTypeStr):
        if not (type(checkTypeStr) == str):
            Write_Log(ELogTpye.warning, f'wrong param data type input. ({validate_func.__name__} => deco_vaildatelog)')
            return 'Unknown Check Type'

        return checkTypeStr


    def wrap(self, *checkDataList):
        _checkTypeName = validate_func.__name__.split('_')[1]

        Write_StartLog(_checkTypeName)

        _errCount = validate_func(self, *checkDataList)

        Write_EndLog(_checkTypeName, _errCount)
    return wrap


def deco_runvalicheck(*checkDataList):
    def decorator(validate_func):
        async def main_loop(checkList):
            _futures = [asyncio.ensure_future(wrap(_dataName)) for _dataName in checkList[0]]
            _result = await asyncio.gather(*_futures)

            _allErrCount = 0
            for errCount in _result:
                _allErrCount += errCount
            
            return _allErrCount
        
        def wrap(dataName):
            return validate_func(dataName)
            
        _loop = asyncio.get_event_loop()
        _allErrCount = _loop.run_until_complete(main_loop(checkDataList))
        _loop.close
        
        return _allErrCount
    return decorator


def deco_valiconfigsplit(configType):
    def get_valiDataNColumn(configType):
        assert type(configType) == EValidationConfigType, f'err : wrong config tpye input. (input data type : {type(configType)})'

        _checkDict : dict = Get_ConifgFromYaml(configType)

        return _checkDict

    def decorator(validate_func):
        def wrap():
            _checkDict = get_valiDataNColumn(configType)

            return validate_func(_checkDict)
        return wrap
    return decorator


def deco_startvalidatelog(func):
    def get_targetdatalist(*checkDataList):
        @deco_usedirmethod(EDirectory.excelDirectory)
        def get_allexceldir(excelDir):
            return glob.glob('{0}*.xlsx'.format(excelDir))

        if not len(checkDataList):
            _checkList = get_allexceldir()

        else:
            _checkList = checkDataList

        return _checkList

    def wrap(*checkDataList):
        Write_Log(ELogTpye.normal, '----------------------------------------------------------------')
        Write_Log(ELogTpye.normal, f'Start Check {func.__name__}.')
        Write_Log(ELogTpye.normal, '< check target data table list. >')

        for data in get_targetdatalist(*checkDataList):
            Write_Log(ELogTpye.normal, f'{data}')

        return func(*checkDataList)
    return wrap