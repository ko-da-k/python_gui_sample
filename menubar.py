#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication, QMainWindow, QAction, QStyle, qApp
from PyQt4.QtCore import QTimer


class Example(QMainWindow):
    """docstring for Example"""

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        exitGUI = QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
        exitAction = QAction(exitGUI, "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(qApp.quit)

        qtInfoGUI = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        qtInfoAction = QAction(qtInfoGUI, "&AboutQt", self)
        qtInfoAction.setShortcut("Ctrl+I")
        qtInfoAction.setStatusTip("Show Qt info")
        qtInfoAction.triggered.connect(qApp.aboutQt)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&Info")
        fileMenu.addAction(qtInfoAction)
        fileMenu.addAction(exitAction)
        menubar.setNativeMenuBar(False)  # for mac

        self.setGeometry(600, 600, 400, 400)
        self.setWindowTitle("menubar")
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
