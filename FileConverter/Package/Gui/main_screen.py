from Package.Data.config import *
from tkinter import *

class MainScreen():
    title = Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'title')
    geometry = (Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'geometry_x'), Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'geometry_y'))
    resizable = (bool(Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'resizeable_x')), bool(Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'resizable_y')))

    def __init__(self):
        pass

    pass