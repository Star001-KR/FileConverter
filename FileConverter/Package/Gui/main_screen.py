from Package.Gui.gui_func import *
from tkinter import *

class MainScreen():
    # window setting value.
    title = Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'title')
    geometry = (Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'geometry_x'), Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'geometry_y'))
    resizable = (bool(Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'resizeable_x')), bool(Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'resizable_y')))

    def __init__(self, window : Tk):
        # window default ui setting initalize.
        window.title(self.title)
        window.geometry(f'{self.geometry[0]}x{self.geometry[1]}')
        window.resizable(self.resizable[0], self.resizable[1])

        # window variable initialize.
        self._lookPageNumber = 1
        self._lastPageNumber = 0
        
        
    # Field Group : Excel Files.
        self.FG_EXCEL_FILES = LabelFrame(window, text = 'Excel Files')
        self.FG_EXCEL_FILES.grid(row = 0, column = 0)

        # Frame : Excel List.
        self.frame_excelList = LabelFrame(self.FG_EXCEL_FILES, text = f'Excel List ({self._lookPageNumber} Page.)')
        self.frame_excelList.grid(row = 0, column = 0)

        # Frame : Pages.
        self.frame_pages = Frame(self.FG_EXCEL_FILES)
        self.frame_pages.grid(row = 1, column = 0)