"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
"""

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.label = None
        self.__initUi()

    def __initUi(self):
        self.setFixedSize(300, 100)

        self.label = QtWidgets.QLabel("<h1>Красивая кнопка</h1>")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.installEventFilter(self)  # Установка фильтра событий на конкретный виджет

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        Настройка дополнительного поведения виджетов

        :param watched: QtCore.QObject
        :param event: QtCore.QEvent
        :return: bool
        """

        if watched == self.label and event.type() == QtCore.QEvent.Type.MouseButtonPress:


            print("mouse pressed")

        return super(Window, self).eventFilter(watched, event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
