from Package.ValidateCheck.validate import *

class EColumnProperty(Enum):
    design = auto()
    nullable = auto()
    unique = auto()
    normal = auto()


class NormalValidate(Validate):
    def __init__(self):
        super().__init__()


    def Check_KeyDuplicate():
        pass


    def Check_ValueEmpty():
        pass


    def Check_ValueDataType():
        pass


    def Check_ValueUniqueValue():
        pass