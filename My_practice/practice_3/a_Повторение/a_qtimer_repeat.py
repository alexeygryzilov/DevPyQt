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
        self.current_window = None
        self.initTimer()
        self.initSignals()
        self.window_2()


    def window_1(self):
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Google Chrome")
        self.setWindowIcon(QtGui.QIcon(os.path.join(ROOT_FOLDER, 'static', 'images', 'free-icon-chrome-888846.png')))

        pixmap = QtGui.QPixmap(os.path.join(ROOT_FOLDER, 'static', 'images', 'free-icon-chrome-888846.png'))
        pixmap_scaled = pixmap.scaled(100, 100)

        label_1 = QtWidgets.QLabel(self)
        label_1.setPixmap(pixmap_scaled)
        label_1.setGeometry(100, 100, 100, 100)
        self.current_window = 1

    def window_2(self):
        self.setGeometry(600, 200, 700, 400)
        self.setWindowTitle("Telegram Web")
        self.setWindowIcon(QtGui.QIcon(os.path.join(ROOT_FOLDER, 'static', 'images', 'free-icon-telegram-2111646.png')))

        pixmap = QtGui.QPixmap(os.path.join(ROOT_FOLDER, 'static', 'images', 'free-icon-telegram-2111646.png'))
        pixmap_scaled = pixmap.scaled(100, 100)

        label_1 = QtWidgets.QLabel(self)
        label_1.setPixmap(pixmap_scaled)
        label_1.setGeometry(100, 100, 100, 100)
        self.current_window = 2

    def initTimer(self) -> None:

        self.myTimer = QtCore.QTimer()
        self.myTimer.setInterval(1000)
        self.myTimer.start()

    def initSignals(self) -> None:
        self.myTimer.timeout.connect(self.change_window)


    def change_window(self):

        if self.current_window == 1:
            window.close()
            self.window_2()
        elif self.current_window == 2:
            window.close()
            self.window_1()

        window.show()
        print('Change')



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
