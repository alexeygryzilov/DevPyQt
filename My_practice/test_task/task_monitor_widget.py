from form import Ui_Form

from PySide6 import QtWidgets, QtGui, QtCore

from threads import SystemInfo


class TaskMonitorWindow(QtWidgets.QWidget):

    def __init__(self, choice=None, parent=None):
        super().__init__(parent)

        self.choice = choice
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initThreads()
        self.initSignals()
        self.ui.radioButton.setChecked(True)
        self.ui.radioButton_2.clicked.connect(self.updateDelay)
        self.ui.radioButton_3.clicked.connect(self.updateDelay)
        self.ui.radioButton_4.clicked.connect(self.updateDelay)
        #self.ui.pushButton_7.setEnabled(False)

    def updateDelay(self):
        if self.ui.radioButton.isChecked():
            self.handler.setDelay(1)
        elif self.ui.radioButton_2.isChecked():
            self.handler.setDelay(5)
        elif self.ui.radioButton_3.isChecked():
            self.handler.setDelay(10)
        elif self.ui.radioButton_4.isChecked():
            self.handler.setDelay(30)

    def initThreads(self):

        self.mythread = SystemInfo()

    def initSignals(self):

        self.ui.pushButton_7.clicked.connect(self.make_choice)
        #self.ui.pushButton.clicked.connect(lambda: self.ui.pushButton_7.setEnabled(True))
        self.ui.pushButton_7.clicked.connect(lambda: print("Поток запущен"))
        self.ui.pushButton_7.clicked.connect(self.mythread.start)

        self.mythread.systemInfoReceived.connect(self.info_updated)
        self.ui.pushButton_8.clicked.connect(lambda: print("Поток остановлен"))

    def make_choice(self):
        print('Choice')
        if self.ui.pushButton.clicked:
            self.choice = 1
            self.ui.pushButton_7.setEnabled(True)
        else:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Выберите тип информации")
            return self.ui.pushButton_7.setEnabled(False)

    def info_updated(self, data):

        self.ui.plainTextEdit.setPlainText(f"Процессор: {str(data[0])}\n"
                                           f"Количество ядер: {str(data[1])}\n"
                                           f"Текущая загрузка: {str(data[2])}")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = TaskMonitorWindow()
    window.show()

    app.exec()
