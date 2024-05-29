from form import Ui_Form

from PySide6 import QtWidgets, QtGui, QtCore

from threads import SystemInfo

import psutil


class TaskMonitorWindow(QtWidgets.QWidget):

    def __init__(self, choice=None, parent=None):
        super().__init__(parent)

        self.choice = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initThreads()
        self.initSignals()
        self.ui.radioButton_2.setChecked(True)

        self.ui.pushButton_8.setEnabled(False)

    def initThreads(self):

        self.mythread = SystemInfo()

    def initSignals(self):

        self.ui.radioButton.clicked.connect(self.updateDelay)
        self.ui.radioButton_2.clicked.connect(self.updateDelay)
        self.ui.radioButton_3.clicked.connect(self.updateDelay)
        self.ui.radioButton_4.clicked.connect(self.updateDelay)
        self.ui.pushButton.clicked.connect(self.set_choice_1)
        self.ui.pushButton_2.clicked.connect(self.set_choice_2)
        self.ui.pushButton_3.clicked.connect(self.set_choice_3)
        self.ui.pushButton_4.clicked.connect(self.set_choice_4)
        self.ui.pushButton_5.clicked.connect(self.set_choice_5)
        self.ui.pushButton_6.clicked.connect(self.set_choice_6)
        self.ui.pushButton_7.clicked.connect(self.get_choice)
        # self.ui.pushButton_7.clicked.connect(lambda: print("Поток запущен"))

        # self.mythread.systemInfoReceived.connect(self.info_updated)
        # self.ui.pushButton_8.clicked.connect(lambda: print("Поток остановлен"))
        self.ui.pushButton_8.clicked.connect(self.finishThread)

    def updateDelay(self):
        if self.ui.radioButton.isChecked():
            self.setDelay(1)
        elif self.ui.radioButton_2.isChecked():
            self.setDelay(5)
        elif self.ui.radioButton_3.isChecked():
            self.setDelay(10)
        elif self.ui.radioButton_4.isChecked():
            self.setDelay(30)

    def setDelay(self, value):
        self.mythread.delay = value
        print('Delay', value)

    def set_choice_1(self):
        self.choice = 1
        self.ui.pushButton_7.setEnabled(True)

    def set_choice_2(self):
        self.choice = 2
        self.ui.pushButton_7.setEnabled(True)

    def set_choice_3(self):
        self.choice = 3
        self.ui.pushButton_7.setEnabled(True)

    def set_choice_4(self):
        self.choice = 4
        self.ui.pushButton_7.setEnabled(True)

    def set_choice_5(self):
        self.choice = 5
        self.ui.pushButton_7.setEnabled(True)

    def set_choice_6(self):
        self.choice = 6
        self.ui.pushButton_7.setEnabled(True)

    def startThread(self):

        self.ui.plainTextEdit.clear()
        self.mythread.status = True
        self.ui.pushButton_7.clicked.connect(self.mythread.start)
        self.mythread.start()
        self.mythread.systemInfoReceived.connect(self.info_updated)
        self.ui.pushButton_8.setEnabled(True)
        print("Поток запущен")
        self.ui.pushButton_7.setEnabled(False)

    def get_choice(self):
        print(f'Choice =  {self.choice}')

        if not self.choice:
            self.ui.pushButton_7.setEnabled(False)
            QtWidgets.QMessageBox.warning(self, "Не выбран тип информации", "Выберите тип информации")
            return
        else:
            self.startThread()

    def info_updated(self, data):

        if self.choice == 1:
            self.ui.plainTextEdit.setPlainText(f"Процессор: {str(data[0])}\n"
                                               f"Количество ядер: {str(data[1])}\n"
                                               f"Текущая загрузка: {str(data[2])} %")
        elif self.choice == 2:
            self.ui.plainTextEdit.setPlainText(f"Общий объём оперативной памяти: {(data[3] / 1024 ** 3) :.2f} ГБ\n"
                                               f"Текущая загрузка оперативной памяти: {str(data[4])} %")

        elif self.choice == 3:
            self.ui.plainTextEdit.setPlainText(f"Количество жестких дисков: {str(data[5])}\n"
                                               f"Информация по каждому диску:\n"
                                               f"{self.get_data(data)[0]}\n"
                                               f"{self.get_data(data)[1]}")

        elif self.choice == 4:
            self.ui.plainTextEdit.setPlainText(f"Работающие процессы: {len(data[7])}\n\n"
                                               f"Процессы: {str(data[7])}")

        elif self.choice == 5:
            self.ui.plainTextEdit.setPlainText(f"Службы: {len(data[8])}\n\n"
                                               f"Службы: {str(data[7])}")

        elif self.choice == 6:
            self.ui.plainTextEdit.setPlainText("Задачи:")

    def get_data(self, data):
        list_ = []
        for disk in data[9]:
            disk_ = psutil.disk_usage(disk)
            info = f'{disk}  total= {(disk_[0] / 1024 ** 3) : .2f} ГБ  used= {(disk_[1] / 1024 ** 3) : .2f} ГБ  free= {(disk_[2] / 1024 ** 3) : .2f} ГБ  percent= {disk_[3]}'
            list_.append(info)
        return list_


    def finishThread(self):

        self.mythread.status = False
        print("Поток остановлен")
        self.ui.plainTextEdit.clear()
        self.ui.pushButton_7.setEnabled(True)
        self.ui.pushButton_8.setEnabled(False)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = TaskMonitorWindow()
    window.show()

    app.exec()

