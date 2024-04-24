import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QWidget

app = QtWidgets.QApplication()
mywindow = QtWidgets.QWidget()
mywindow.show()
app.exec()
print("Приложение закрыто!")

#window = QWidget()
#window.setWindowTitle('Простейшее окно')
#window.show()

#sys.exit(app.exec())
