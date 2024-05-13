"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль.
При выводе события указывать время, когда произошло событие.
"""

from PySide6 import QtWidgets, QtCore
from time import ctime
from ui.form_b import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.event()
        self.ui.plainTextEdit.insertPlainText(ctime())



    def event(self, event: QtCore.QEvent):
        text_ = event
        self.ui.plainTextEdit.insertPlainText(text_)
        print(text_, ctime())
        return super().event(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
