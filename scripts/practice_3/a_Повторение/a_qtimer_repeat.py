"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets, QtGui, QtCore

import os

import time

from conf import ROOT_FOLDER


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)


        self.initTimer()
        self.initSignals()

    def window_1(self):
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Google Chrome")
        self.setWindowIcon(QtGui.QIcon(os.path.join(ROOT_FOLDER, 'static', 'images', 'free-icon-chrome-888846.png')))

        pixmap = QtGui.QPixmap(os.path.join(ROOT_FOLDER, 'static', 'images', 'free-icon-chrome-888846.png'))
        pixmap_scaled = pixmap.scaled(100, 100)

        label_1 = QtWidgets.QLabel(self)
        label_1.setPixmap(pixmap_scaled)
        label_1.setGeometry(100, 100, 100, 100)

    def window_2(self):
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Telegram Web")
        self.setWindowIcon(QtGui.QIcon(os.path.join(ROOT_FOLDER, 'static', 'images', 'free-icon-telegram-2111646.png')))

        pixmap = QtGui.QPixmap(os.path.join(ROOT_FOLDER, 'static', 'images', 'free-icon-telegram-2111646.png'))
        pixmap_scaled = pixmap.scaled(100, 100)

        label_1 = QtWidgets.QLabel(self)
        label_1.setPixmap(pixmap_scaled)
        label_1.setGeometry(100, 100, 100, 100)

    def initTimer(self) -> None:

        self.timeTimer = QtCore.QTimer()
        self.timeTimer.setInterval(1000)
        self.timeTimer.start()

    def initSignals(self) -> None:

        self.timeTimer.timeout.connect(self.window_1())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
