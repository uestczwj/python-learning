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
import time
from matplotlib.pyplot import MultipleLocator
from matplotlib.animation import FuncAnimation

class MainForm(QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.fig, self.ax = plt.subplots()
        self.xdata, self.ydata = [], []
        self.ln, = self.ax.plot([], [], 'r-', animated=False)

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

    def init(self):
        self.ax.set_xlim(0, 2 * np.pi)
        self.ax.set_ylim(-1, 1)
        return self.ln,

    def update(self, frame):
        self.xdata.append(frame)
        self.ydata.append(np.sin(frame))
        self.ln.set_data(self.xdata, self.ydata)
        return self.ln,

    @pyqtSlot()
    def on_btnDraw_clicked(self):
         ani = FuncAnimation(self.fig, self.update, frames=np.linspace(0, 2 * np.pi, 128), init_func=self.init, blit=True)
         self.ax.show()

    @pyqtSlot()
    def on_btnQuit_clicked(self):
        self.close()


