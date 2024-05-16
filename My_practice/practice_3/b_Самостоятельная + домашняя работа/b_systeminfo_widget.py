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

from PySide6 import QtWidgets, QtGui

from form_systeminfo import Ui_CPUloadRAMload


class WindowCPU(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.data_list_settings = QtCore.QSettings("MyData")
        self.ui = Ui_CPUloadRAMload()
        self.ui.setupUi(self)
        # self.initSignals()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowCPU()
    window.show()

    app.exec()
