from Package.Gui.gui_func import *
from Package.Convert.convert import *
from tkinter import *

class MainScreen():
    # window setting value.
    title = Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'title')
    geometry = (Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'geometry_x'), Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'geometry_y'))
    resizable = (bool(Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'resizeable_x')), bool(Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'resizable_y')))

    buttonSize = (Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'buttonsize_width'), Get_GuiSettingFromJson(EGuiSettingType.main_screen, 'buttonsize_height'))

    def __init__(self, window : Tk):
        # window default ui setting initalize.
        window.title(self.title)
        window.geometry(f'{self.geometry[0]}x{self.geometry[1]}')
        window.resizable(self.resizable[0], self.resizable[1])

        # window variable initialize.
        self._lookPageNumber = 1
        self._lastPageNumber = 0
        
        self.convert = Convert()
        
    # Frame Group : Excel Files.
        self.FG_EXCEL_FILES = LabelFrame(window, text = 'Excel List')
        self.FG_EXCEL_FILES.grid(row = 0, column = 0)

        # Frame : Excel List.
        self.frame_excelList = Frame(self.FG_EXCEL_FILES)
        self.frame_excelList.grid(row = 0, column = 0)

        self.check_excelList = []
        self.checkExcelDict = {}
        for listNum in range(0, len(self.convert.Get_AllExcelList())):
            self.checkExcelDict[self.convert.Get_AllExcelList()[listNum]] = IntVar()
            self.check_excelList.append(Checkbutton(self.frame_excelList, text = self.convert.Get_AllExcelList()[listNum],
                                                    variable = self.checkExcelDict[self.convert.Get_AllExcelList()[listNum]]))
            self.check_excelList[listNum].grid(row = listNum, column = 0, sticky = 'w')

        # Frame : Pages.
        self.frame_pages = Frame(self.FG_EXCEL_FILES)
        self.frame_pages.grid(row = 1, column = 0)


    # Frame Group : Buttons.
        self.FG_BUTTONS = LabelFrame(window, text = 'Buttons')
        self.FG_BUTTONS.grid(row = 0, column = 1)

        # Frame : File Convert
        self.frame_fileConvert = Frame(self.FG_BUTTONS)
        self.frame_fileConvert.grid(row = 0, column = 0)

        self.btn_fileConvert = Button(self.frame_fileConvert, text = 'File Convert', width = self.buttonSize[0], height = self.buttonSize[1], command = lambda : press_btn_fileConvert(self.checkExcelDict))
        self.btn_fileConvert.grid(row = 0, column = 0)

        # Frame : Validate Check
        self.frame_valiCheck = Frame(self.FG_BUTTONS)
        self.frame_valiCheck.grid(row = 0, column = 1)
        
        self.btn_validateCheck = Button(self.frame_valiCheck, text = 'Validate Check', width = self.buttonSize[0], height = self.buttonSize[1], command = press_btn_validateCheck)
        self.btn_validateCheck.grid(row = 0, column = 0)

        # Frame : Run All
        self.frame_runAll = Label(self.FG_BUTTONS)
        self.frame_runAll.grid(row = 1, column = 0, columnspan = 2)
        
        self.btn_runAll = Button(self.frame_runAll, text = 'Run All', width = self.buttonSize[0] * 2 + 2, height = self.buttonSize[1], command = press_btn_runAll)
        self.btn_runAll.grid(row = 0, column = 0)
