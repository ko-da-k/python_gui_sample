#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication,QMainWindow,QAction,QStyle,qApp,QIcon
from PyQt4.QtCore import QTimer

class Example(QMainWindow):
	"""docstring for Example"""
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		exitAction = QAction(QIcon("exit.png"),"Exit",self)
		exitAction.setShortcut("Ctrl+Q")
		exitAction.triggered.connect(qApp.quit)

		pythonAction = QAction(QIcon("pythonlogo.png"),"Python",self)
		pythonAction.setShortcut("Ctrl+P")
		pythonAction.triggered.connect(qApp.quit)

		qtInfoAction = QAction(QIcon("qtlogo.png"),"qtinfo",self)
		qtInfoAction.setShortcut("Ctrl+I")
		qtInfoAction.triggered.connect(qApp.aboutQt)

		self.toolbar = self.addToolBar("toolbar")
		self.toolbar.addAction(exitAction)
		self.toolbar.addAction(pythonAction)
		self.toolbar.addAction(qtInfoAction)

		self.setGeometry(600,600,400,400)
		self.setWindowTitle("toolbar")
		self.show()

def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()