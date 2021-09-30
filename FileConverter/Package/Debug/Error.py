from Package.Debug.log_func import *

class ParamDataTypeError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)


class FileNameNotInitError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)