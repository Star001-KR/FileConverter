from enum import Enum, auto
import json
import platform
from Package.Directory.directory import EDirectory
from Package.Directory.directory_func import deco_usedirmethod

class EConfigType(Enum):
    excel = auto()
    data_id = auto()


@deco_usedirmethod(EDirectory.toolConfigDirectory)
def Get_ConfigFromJson(configType, configCategory, jsonPath):
    assert (type(configType) == EConfigType), 'err : wrong param data type input.'
    if configType == EConfigType.excel:
        _configTypeName = 'excel'

    _jsonPath = jsonPath
    
    with open (_jsonPath) as file:
        file_json = json.load(file)
        configSet = file_json[_configTypeName]

    for config in configSet:
        if config == configCategory:
            return configSet[config]

    assert (False), 'err : input wrong config category.'