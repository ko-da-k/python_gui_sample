#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import datetime


class Example(QtGui.QMainWindow):
    """docstring for Example"""

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle("statusbar")
        self.show()

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.time_draw)
        timer.start(1000)  # msec

    def time_draw(self):
        d = datetime.datetime.today()
        daystr = d.strftime("%Y-%m-%d %H:%M:%S")
        self.statusBar().showMessage(daystr)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
