"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""
import traceback

from PySide6 import QtWidgets, QtCore

import requests


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.getUrlStatusThread = None

        self.initUi()

        self.initSignals()

    def initUi(self):
        self.lineEditUrl = QtWidgets.QLineEdit()
        self.lineEditUrl.setPlaceholderText("Введите URL")

        self.spinBoxDelay = QtWidgets.QSpinBox()
        self.spinBoxDelay.setMinimum(5)

        self.labelStatus = QtWidgets.QLabel()
        self.labelStatus.setText("Статус сайта")

        self.plainTexteditLog = QtWidgets.QPlainTextEdit()
        self.plainTexteditLog.setReadOnly(True)

        self.pushButtonHandle = QtWidgets.QPushButton("Запустить")
        self.pushButtonHandle.setCheckable(True)

        lay = QtWidgets.QVBoxLayout()
        lay.addWidget(self.lineEditUrl)
        lay.addWidget(self.spinBoxDelay)
        lay.addWidget(self.labelStatus)
        lay.addWidget(self.plainTexteditLog)
        lay.addWidget(self.pushButtonHandle)

        self.setLayout(lay)

    def initSignals(self):
        self.pushButtonHandle.clicked.connect(self.changeButtontext)
        self.pushButtonHandle.clicked.connect(self.handleUrl)

        self.spinBoxDelay.valueChanged.connect(self.setThreadDelay)

    def startThreads(self, url):
        self.getUrlStatusThread = GetUrlStatusThread()
        self.getUrlStatusThread.status_code.connect(self.__changeStatus)
        self.getUrlStatusThread.finished.connect(self.finishThreads)
        self.getUrlStatusThread.url = url
        self.getUrlStatusThread.delay = self.spinBoxDelay.value()
        self.getUrlStatusThread.start()

    def finishThreads(self):
        self.getUrlStatusThread = None
        self.pushButtonHandle.setEnabled(True)
    def handleUrl(self, status):
        if status:
            url = self.lineEditUrl.text()
            if not url.strip():
                QtWidgets.QMessageBox.warning(self, "Ошибка", "Введите URL")
                self.pushButtonHandle.setChecked(False)
                self.pushButtonHandle.setText("Запустить")
                return
            self.startThreads(url)
        else:
            self.getUrlStatusThread.status = False
            self.pushButtonHandle.setEnabled(False)

    def changeButtontext(self, status):
        self.pushButtonHandle.setText("Остановить" if status else "Запустить")

    def __changeStatus(self, status):
        self.plainTexteditLog.appendPlainText(f'status: {status}')

    def setThreadDelay(self, value):
        if self.getUrlStatusThread:
            self.getUrlStatusThread.delay = value


class GetUrlStatusThread(QtCore.QThread):
    status_code = QtCore.Signal(object)

    def __init__(self, url=None, delay=5, parent=None):
        super().__init__(parent)

        self.__url = url
        self.__delay = delay
        self.__status = True

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def delay(self):
        return self.__delay

    @delay.setter
    def delay(self, value):
        self.__delay = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def run(self) -> None:
        if not self.__url:
            self.status_code.emit("URL не задан")
            return

        while self.__status:
            self.status_code.emit(get_status_code(self.__url))
            self.sleep(self.__delay)


def get_status_code(url):
    try:
        responce = requests.get(url)
        return responce.status_code
    except Exception as err:
        return str(err)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
