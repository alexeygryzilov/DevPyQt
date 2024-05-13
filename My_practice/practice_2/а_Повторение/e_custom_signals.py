"""
Генерация "кастомных" сигналов и открытие нескольких окон
"""

from PySide6 import QtWidgets, QtCore, QtGui


class Main(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.initChilds()
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        self.setWindowTitle('Lable')
        self.lable_1 = QtWidgets.QLabel(self)
        self.lable_1.setText("<h1>Пройдите регистрацию</h1>")
        self.pushButton = QtWidgets.QPushButton("Зарегистрироваться")


        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lable_1)
        layout.addWidget(self.pushButton)


        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton.clicked.connect(self.childWindow.show)

        #self.childWindow.custom_signal.connect(lambda x: print(x))
        self.childWindow.custom_signal.connect(self.childCustomSignalActivated)

    def initChilds(self) -> None:
        """
        Инициализация дочерних окон

        :return: None
        """

        self.childWindow = Child()  # Обязательно является атрибутом класса (self)
        self.childWindow.setGeometry(800, 180, 300, 200)

    def childCustomSignalActivated(self, text) -> None:
        """
        Метод срабатывает при выполнении
        сигнала custom_signal (в момент вызова emit)

        :param text: текст из дочернего окна
        :return: None
        """

        self.lable_1.setText(text)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Действия при закрытии программы

        :param event: QtGui.QCloseEvent
        :return: None
        """

        self.childWindow.close()


class Child(QtWidgets.QWidget):
    custom_signal = QtCore.Signal(str)  # Обязательно указать тип данных

    def __init__(self, parent=None):
        super().__init__(parent)

        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """
        self.setWindowTitle("QDialog")


        self.lineEdit_1 = QtWidgets.QLineEdit()
        self.lineEdit_1.setPlaceholderText('Введите логин')
        self.lineEdit_2 = QtWidgets.QLineEdit()
        self.lineEdit_2.setPlaceholderText('Введите пароль')
        self.pushButton_1 = QtWidgets.QPushButton("Зарегистрироваться")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.lineEdit_1)
        layout.addWidget(self.lineEdit_2)
        layout.addWidget(self.pushButton_1)

        self.setLayout(layout)

    def initSignals(self) -> None:
        """
        Инициализация сигналов

        :return: None
        """

        self.pushButton_1.clicked.connect(self.changedLineEditText)
        self.pushButton_1.clicked.connect(self.onPushButtonClicked)
        #self.pushButton_1.clicked.connect(self.objectNameChanged)
        #self.pushButton_1.clicked.connect

    def changedLineEditText(self) -> None:
        """
        Метод обрабатывающий изменение текста в lineEdit

        :return: None
        """

        #self.custom_signal.emit("<h1>Добро пожаловать </h1>" + self.lineEdit_1.text())
        self.custom_signal.emit(f"<h1>Добро пожаловать {self.lineEdit_1.text()}</h1>")

    def onPushButtonClicked(self):
        print(f"Password: {hash(self.lineEdit_2.text())}")



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myapp = Main()
    # myapp.custom_signal.connect(lambda data: print(data))
    myapp.show()
    app.exec()
