#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import QTimer,SIGNAL,QObject
import datetime

class Example(QMainWindow):
	"""docstring for Example"""
	def __init__(self):
		super(Example, self).__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(600,600,400,400)
		self.setWindowTitle("textedit")

		self.w = QWidget()

		label = QLabel("QTextEdit:")
		self.text = QTextEdit(self)
		hbox = QHBoxLayout()
		hbox.addWidget(label)
		hbox.addWidget(self.text)

		self.w.setLayout(hbox)
		self.setCentralWidget(self.w)

		self.timer = QTimer()
		QObject.connect(self.timer,SIGNAL("timeout()"),self.countup)
		self.timer.start(1000)

		self.show()

	def countup(self):
		self.text.append("A")


def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()