#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import QTimer, SIGNAL, QObject, Qt


class App(QMainWindow):
    """docstring for App"""

    def __init__(self):
        super(App, self).__init__()

    def main(self):
        self.w = QWidget()
        self.w.resize(400, 200)
        self.w.setWindowTitle("SliderSample")

        slider_label = QLabel("Slider (%):")
        self.slider = QSlider(Qt.Horizontal)  # スライダの向き
        self.slider.setRange(0, 100)  # スライダの範囲
        self.slider.setValue(20)  # 初期値
        # スライダのメモリを両方に出す
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.connect(self.slider, SIGNAL("valueChanged(int)"), self.on_draw)

        hbox = QHBoxLayout()
        hbox.addWidget(slider_label)
        hbox.setAlignment(slider_label, Qt.AlignVCenter)
        hbox.addWidget(self.slider)
        hbox.setAlignment(self.slider, Qt.AlignVCenter)

        self.textbox = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(self.textbox)
        vbox.addLayout(hbox)
        self.w.setLayout(vbox)
        self.w.show()

    def on_draw(self):
        self.textbox.setText(str(self.slider.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainApp = App()
    mainApp.main()
    app.exec_()
