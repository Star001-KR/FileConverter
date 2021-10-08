from enum import Enum, auto
import json
import platform

class EConfigType(Enum):
    excel = auto()


def Get_ConfigFromJson(configType, configCategory):
    def get_configDirectory():
        _isMac = (platform.system() == "Darwin") and True or False
        
        return (_isMac) and 'Config/config.json' or 'Config\\config.json'

    assert (type(configType) == EConfigType), 'err : wrong param data type input.'
    if configType == EConfigType.excel:
        _configTypeName = 'excel'

    jsonPath = get_configDirectory()
    
    with open (jsonPath) as file:
        file_json = json.load(file)
        configSet = file_json[_configTypeName]

    for config in configSet:
        if config == configCategory:
            return configSet[config]

    assert (False), 'err : input wrong config category.'