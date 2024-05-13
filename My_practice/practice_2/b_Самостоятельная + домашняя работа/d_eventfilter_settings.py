"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtGui

from d_eventfilter_settings_form import Ui_Form


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self) -> None:
        # self.ui.dial.valueChanged.connect(self.print_data)
        # self.ui.horizontalSlider.valueChanged.connect(self.print_data())
        self.ui.dial.valueChanged.connect(self.lcd_number)
        self.ui.comboBox.currentTextChanged.connect(self.change_data)
        # self.ui.comboBox.currentTextChanged.connect(self.keyPressEvent)
        self.ui.dial.valueChanged.connect(self.change_slider)
        self.ui.horizontalSlider.valueChanged.connect(self.change_dial)

    def change_slider(self):
        self.ui.horizontalSlider.setValue(self.ui.dial.value())

    def change_dial(self):
        self.ui.dial.setValue(self.ui.horizontalSlider.value())

    def change_data(self):
        if self.ui.comboBox.currentIndex() == 0:
            data = bin(self.ui.dial.value())
        elif self.ui.comboBox.currentIndex() == 1:
            data = self.ui.dial.value()
        elif self.ui.comboBox.currentIndex() == 2:
            data = hex(self.ui.dial.value())
        elif self.ui.comboBox.currentIndex() == 3:
            data = oct(self.ui.dial.value())
        self.ui.lcdNumber.display(data)
        return data

    def lcd_number(self):
        self.ui.lcdNumber.display(self.change_data())

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """
        Событие нажатия на клавиатуру

        :param event: QtGui.QKeyEvent
        :return: None
        """
        if event.key() == 43:
            self.ui.dial.setValue(self.ui.dial.value() + 1)
            # self.ui.dial.valueChanged
            print(self.change_data())
        elif event.key() == 45:
            self.ui.dial.setValue(self.ui.dial.value() - 1)
            # self.ui.dial.valueChanged
            print(self.change_data())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
