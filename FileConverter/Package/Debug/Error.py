from Package.Debug.Log import *

class ParamDataTypeError(Exception):
    def __init__(self, param, *args: object):
        super().__init__(*args)


