from PySide6 import QtWidgets, QtGui
from conf import ROOT_FOLDER
import os


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("My first window")
        #self.setWindowIcon(QtGui.QIcon("C:/Users/4769003/OneDrive/Рабочий стол/FEI logo"))
        self.setWindowIcon(QtGui.QIcon(os.path.join(ROOT_FOLDER, 'static', 'images', 'python.png')))
        self.setGeometry(200, 300, 500, 250 )
        self.frameGeometry().width()

        print(self.pos())
        print(self.size())
        print(self.frameGeometry())
        print(self.width(), self.height())

        self.setMinimumWidth(200)
        self.setMinimumHeight(100)
        self.setMaximumSize(700, 350)



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
