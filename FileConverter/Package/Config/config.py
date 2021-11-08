from enum import Enum, auto
from Package.Directory.directory import EDirectory
from Package.Directory.directory_func import deco_usedirmethod
import json
import yaml

class EConfigType(Enum):
    excel = auto()
    data_id = auto()
    last_tid = auto()


class EValidationConfigType(Enum):
    ref_validation = auto()
    value_size_compare = auto()


def Get_ConfigTypeName(configType):
    assert type(configType) == EConfigType or type(configType) == EValidationConfigType, 'err : wrong param data type input.'

    _configEnum = (type(configType) == EConfigType) and EConfigType or EValidationConfigType

    for member in _configEnum:
        if configType == member:
            return member._name_

    assert (False), 'err : no config file value, matches enum member.'


@deco_usedirmethod(EDirectory.toolConfigDirectory)
def Get_ConfigFromJson(configType, configCategory, jsonPath):
    assert (type(configType) == EConfigType), 'err : wrong param data type input.'

    _configTypeName = Get_ConfigTypeName(configType)
    
    with open (jsonPath) as file:
        file_json = json.load(file)
        configSet = file_json[_configTypeName]
    
    # if want return all config in config type input magic keyword 'all (or All)' at configCategory param.
    if configCategory == 'all' or configCategory == 'All':
        return configSet

    else:
        for config in configSet:
            if config == configCategory:
                return configSet[config]

    assert (False), 'err : input wrong config category.'


@deco_usedirmethod(EDirectory.validationDirectory)
def Get_ConifgFromYaml(configType, yamlPath):
    assert (type(configType) == EValidationConfigType), 'err : wrong param data type input.'
    
    _configTypeName = Get_ConfigTypeName(configType)

    with open(yamlPath) as file:
        file_yaml = yaml.safe_load(file)
        configSet = file_yaml[_configTypeName]

    return configSet