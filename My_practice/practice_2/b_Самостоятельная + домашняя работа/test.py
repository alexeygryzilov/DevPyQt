from PySide6 import QtWidgets, QtGui

from c_signals_events_form import Ui_Form

app_1 = QtGui.QGuiApplication([])
print(len(QtGui.QGuiApplication.screens()))

main_screen = QtGui.QGuiApplication.screens()[0]
print(main_screen.size().height())

for screen in QtGui.QGuiApplication.screens():
    print(screen.geometry(), screen.size())
    print(screen.size().width())