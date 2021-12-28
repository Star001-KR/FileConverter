# 2021.12.28 / Code By Tae Hyung Kim.

from Package.Gui.main_screen import *

def Init_Tool():
    Init_Log(False)
    
    Write_Log(ELogTpye.normal, 'Init Directory, Log.')


if __name__ == '__main__':
    Init_Tool()

    main_screen = Tk()
    window = MainScreen(main_screen)
    main_screen.mainloop()