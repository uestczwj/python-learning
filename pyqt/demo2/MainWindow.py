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

class MainForm(QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.zero_points = [-10, -2, 5, 14]
        self.pause_time = 0.2

        self.zero_abs = [abs(x) for x in self.zero_points]
        self.x_begin = (max(self.zero_abs) + 2) * (-1)
        self.axis_factor = 1.1
        self.zeros_count = len(self.zero_points)
        self.x_end = abs(self.x_begin)
        self.x_axis = self.x_end * self.axis_factor

        self.x_major_locator = MultipleLocator(1)
        self.y_major_locator = MultipleLocator(1)

        self.ax = plt.gca()
        self.ax.xaxis.set_major_locator(self.x_major_locator)
        self.ax.yaxis.set_major_locator(self.y_major_locator)

        plt.axis([-self.x_axis, self.x_axis, 0, self.x_axis * self.zeros_count])

        self.x = []
        self.y = []

        self.y_min = sum(self.zero_abs)
        self.y_max = 0

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

    def get_y(self, i, zeros_count):
        val = 0
        for j in range(zeros_count):
            val = val + abs(i - self.zero_points[j])

        return val

    def get_y_label(self, zeros_count):
        y_label = ""

        for i in range(zeros_count):
            if self.zero_points[i] > 0:
                y_label = y_label + '|x - ' + str(self.zero_points[i]) + '|'
            elif self.zero_points[i] == 0:
                y_label = y_label + '|x|'
            else:
                y_label = y_label + '|x + ' + str(abs(self.zero_points[i])) + '|'

            if i < zeros_count - 1:
                y_label = y_label + ' + '

        return y_label

    @pyqtSlot()
    def on_btnDraw_clicked(self):
        for i in range(self.x_begin, self.x_end + 1):
            plt.ion()

            ax = self.fig.add_subplot(111)

            self.x.append(i)
            y_val = self.get_y(i, self.zeros_count)

            self.y_min = min(self.y_min, y_val)
            self.y_max = max(self.y_max, y_val)

            self.y.append(y_val)
            ax.plot(self.x, self.y, 'go')
            self.canvas.draw()
            plt.ioff()

            #time.sleep(0.1)
            ax.cla()

    @pyqtSlot()
    def on_btnQuit_clicked(self):
        self.close()


