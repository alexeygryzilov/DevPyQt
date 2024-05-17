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

from PySide6 import QtWidgets, QtGui,QtCore

import psutil
import time

from form_systeminfo import Ui_CPUloadRAMload

class SystemInfo(QtCore.QThread):
    systemInfoReceived = QtCore.Signal(list) # TODO Создайте экземпляр класса Signal и передайте ему в конструктор тип данных передаваемого значения (в текущем случае list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.delay = None  # TODO создайте атрибут класса self.delay = None, для управлением задержкой получения данных

    def run(self) -> None:  # TODO переопределить метод run
        if self.delay is None:  # TODO Если задержка не передана в поток перед его запуском
            self.delay = 1  # TODO то устанавливайте значение 1

        while True:  # TODO Запустите бесконечный цикл получения информации о системе
            cpu_value = psutil.cpu_percent()# TODO с помощью вызова функции cpu_percent() в пакете psutil получите загрузку CPU
            ram_value = psutil.virtual_memory().percent  # TODO с помощью вызова функции virtual_memory().percent в пакете psutil получите загрузку RAM
            data = [cpu_value, ram_value]
            self.systemInfoReceived.emit(data)  # TODO с помощью метода .emit передайте в виде списка данные о загрузке CPU и RAM
            time.sleep(1)  # TODO с помощью функции .sleep() приостановите выполнение цикла на время self.delay
            print("CPU value", cpu_value, "RAM value", ram_value)


class WindowCPU(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        # self.data_list_settings = QtCore.QSettings("MyData")
        self.ui = Ui_CPUloadRAMload()
        self.ui.setupUi(self)
        self.initSignals()
        self.initThreads()

    def initThreads(self):

        self.mythread = SystemInfo()


    def initSignals(self):


        self.ui.pushButton.clicked.connect(self.runProcess)
        self.ui.spinBox.valueChanged.connect(self.runProcess())
        #self.mythread.systemInfoReceived.connect(self.ui.lineEdit.setText("start"))
        #self.mythread.started.connect(lambda: print(psutil.cpu_percent()) )

    def runProcess(self):
        #self.ui.pushButton.setEnabled(False)
        self.mythread.start()
        self.mythread.systemInfoReceived.connect(self.data_updated)
        #self.ui.lineEdit.setText()
        print('started')
        print('Spixbox', self.ui.spinBox.value())

    def data_updated(self, data: list) ->None:

        self.ui.lineEdit.setText(str(data[0]))
        self.ui.lineEdit_2.setText(str(data[1]))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowCPU()
    window.show()

    app.exec()
