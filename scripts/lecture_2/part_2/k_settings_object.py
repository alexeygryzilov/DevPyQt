"""
Работа с классом QSettings (сохранение объектов)
"""

from PySide6 import QtWidgets, QtGui, QtCore


class Window(QtWidgets.QWidget):
    # конструктор класса
    def __init__(self, parent=None):
        super().__init__(parent)    # вызов конструктора родительского класса

        self.ip_list_settings = QtCore.QSettings("IPViewer")    # создание объекта QSettings для хранения натроек

        self.initUi()   # инициализация пользовательского интерфейса

    def initUi(self) -> None:
        """
        Доинициализация Ui

        :return: None
        """

        main_layout = QtWidgets.QVBoxLayout()   # создание вертикального макета для виджетов

        ip_list = self.ip_list_settings.value("ip_list", [])    # получение списка IP-адресов из настроек

        for ip in ip_list:  # вывод каждого IP-адреса в консоль
            print(ip)

        self.lineEdit_1 = QtWidgets.QLineEdit() # Создание виджета QLineEdit для ввода IP-адреса
        if ip_list:
            self.lineEdit_1.setText(ip_list[0])

        self.lineEdit_2 = QtWidgets.QLineEdit()
        if ip_list:
            self.lineEdit_2.setText(ip_list[1])

        self.lineEdit_3 = QtWidgets.QLineEdit()
        if ip_list:
            self.lineEdit_3.setText(ip_list[2])

        main_layout.addWidget(self.lineEdit_1)
        main_layout.addWidget(self.lineEdit_2)
        main_layout.addWidget(self.lineEdit_3)

        self.setLayout(main_layout)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        self.ip_list_settings.setValue(
            "ip_list", [self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text()]
        )


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    myWindow = Window()
    myWindow.show()

    app.exec()
