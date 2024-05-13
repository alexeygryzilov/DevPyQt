"""
Файл для повторения темы QSettings

Напомнить про работу с QSettings.

Предлагается создать виджет с plainTextEdit на нём, при закрытии приложения,
сохранять введённый в нём текст с помощью QSettings, а при открытии устанавливать
в него сохранённый текст
"""

from PySide6 import QtWidgets, QtCore, QtGui


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_settings = QtCore.QSettings("TextViewer")
        self.__initUi()

    def __initUi(self):

        text_ = self.text_settings.value("text_", '')
        print(text_)
        self.__plainTextEdit = QtWidgets.QPlainTextEdit()
        if text_:
            self.__plainTextEdit.setPlainText(text_)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.__plainTextEdit)

        self.setLayout(layout)

    def __loadSettings(self):
        pass

    def __saveSettings(self):
        pass

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        Событие закрытия окна

        :param event: QtGui.QCloseEvent
        :return: None
        """

        # Сохранение списка IP-адресов в настройки
        self.text_settings.setValue(
            "text_", self.__plainTextEdit.
        )




if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
