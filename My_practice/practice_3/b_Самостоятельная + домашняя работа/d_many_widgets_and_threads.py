"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets, QtGui

# from b_systeminfo_widget import WindowCPU
from c_weatherapi_widget import WindowWeather
from test import WindowCPU


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("practice_3")
        win_1 = WindowCPU()
        win_2 = WindowWeather()

        layout = QtWidgets.QHBoxLayout()

        layout.addWidget(win_1)
        layout.addWidget(win_2)

        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MyWindow()
    window.show()

    app.exec()
