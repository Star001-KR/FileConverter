from Package.ValidateCheck.validate_normal import *
from Package.ValidateCheck.validate_config import *

class ValidateSet(NormalValidate, ConfigValidate):
    def __init__(self):
        super().__init__()