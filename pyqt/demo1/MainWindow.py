# -*- coding: utf-8 -*-
'''
TODO:LQD
'''
from PyQt5.QtCore import pyqtSlot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC
from ui_MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QWidget, QVBoxLayout, QPushButton

from matplotlib.pyplot import MultipleLocator

class MainForm(QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_ui()

        self.center()

    def init_ui(self):
        self.setWindowTitle('PyQt5 MainForm')

        # TODO:这里是结合的关键
        self.fig    = plt.Figure()
        self.canvas = FC(self.fig)
        self.canvas.setParent(self.ui.clientWidget)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def on_btnDraw_clicked(self):
        try:
            ax = self.fig.add_subplot(111)
            x = np.linspace(0, 100, 100)
            y = np.random.random(100)
            ax.cla()  # TODO:删除原图，让画布上只有新的一次的图
            ax.plot(x, y)
            self.canvas.draw()  # TODO:这里开始绘制
        except Exception as e:
            print(e)

    @pyqtSlot()
    def on_btnQuit_clicked(self):
        self.close()


