"""
Создание окна на основе QWidget
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.setWindowTitle("My first window")

        # Настройка компоновки окна
        pushbut = QtWidgets.QPushButton("Текст кнопки")
        checkbox = QtWidgets.QCheckBox("Флажок")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(pushbut)
        layout.addWidget(checkbox)

        self.setLayout(layout)
        self.setGeometry(100, 200, 400, 300)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
