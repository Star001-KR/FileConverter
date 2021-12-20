# 2021.12.20 / Code By Tae Hyung Kim.

from Package.Gui.main_screen import *

def Init_Tool():
    Init_Log(False)
    
    Write_Log(ELogTpye.normal, 'Init Directory, Log.')


if __name__ == '__main__':
    Init_Tool()
    #Check_AllValidate()

    main_screen = Tk()
    window = MainScreen(main_screen)
    main_screen.mainloop()

    a = Convert()

    for excelName in a.Get_AllExcelList():
        a.Convert_ExcelToJson(excelName)