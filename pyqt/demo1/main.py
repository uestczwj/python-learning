from PyQt5.QtWidgets import QApplication
from MainWindow import *
import sys

def ui_main():
    app = QApplication(sys.argv)
    w = MainForm()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    ui_main()