#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore
import datetime


def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    w.resize(600, 400)
    w.setWindowTitle("Qtsample")
    #	w.setWindowIcon(QtGue.QIcon("~.png")) #アプリケーションアイコン
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
