"""
конец 1 части 2 лекции
"""

from PySide6 import QtWidgets, QtCore

class MyPressedButton(QtWidgets.QPushButton):

    def __init__(self, title, parent=None):
        super().__init__(parent)

        self.setText(title)

    def mousePressEvent(self, event):
        print("Нажатие на кнопку")

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        b_1 = QtWidgets.QPushButton("Кнопка 1")
        b_2 = MyPressedButton("Кнопка 2")

        lay = QtWidgets.QVBoxLayout()
        lay.addWidget(b_1)
        lay.addWidget(b_2)

        self.setLayout(lay)

if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()