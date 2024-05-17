"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""

from PySide6 import QtWidgets, QtGui, QtCore

import psutil
import time

from form_systeminfo import Ui_CPUloadRAMload

from systeminfo import SystemInfo




class WindowCPU(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_CPUloadRAMload()
        self.ui.setupUi(self)
        self.initThreads()

    def initThreads(self):
        self.mythread = SystemInfo()
        self.mythread.start()
        self.runProcess()

    def runProcess(self):
        self.mythread.start()
        self.mythread.systemInfoReceived.connect(self.data_updated)
        self.ui.spinBox.valueChanged.connect(self.data_updated)

    def data_updated(self, data: list) -> None:
        self.ui.lineEdit.setText(str(data[0]))
        self.ui.lineEdit_2.setText(str(data[1]))
        self.mythread.delay = self.ui.spinBox.value()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowCPU()
    window.show()

    app.exec()
