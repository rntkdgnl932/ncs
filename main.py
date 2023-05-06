
from PyQt5.QtWidgets import *
import sys

import main_p

sys.path.append('C:/nightcrow/mymodule')

import os.path

if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = main_p.MyApp()

        # Back up the reference to the exceptionhook
        sys._excepthook = sys.excepthook

        # Set the exception hook to our wrapping function
        sys.excepthook = main_p.my_exception_hook

        sys.exit(app.exec_())
    except Exception as e:
        print(e)
        print("프로그램 꺼지기전 정지")
        os.system("pause")
