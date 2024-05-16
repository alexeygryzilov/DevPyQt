"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events_form.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

from PySide6 import QtWidgets, QtGui
from time import ctime
from c_signals_events_form import Ui_Form


class Window(QtWidgets.QWidget):
    # class Screens(QtGui.QGuiApplication):
    #     def __init__(self, parent=None):
    #         super().__init__(parent)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initSignals()

    def initSignals(self) -> None:
        self.ui.spinBoxX.textChanged.connect(self.onspinBoxXY)
        self.ui.spinBoxY.textChanged.connect(self.onspinBoxXY)
        self.ui.pushButtonMoveCoords.clicked.connect(self.onspinBoxXY)
        self.ui.pushButtonLT.clicked.connect(self.moveLT)
        self.ui.pushButtonRT.clicked.connect(self.moveRT)
        self.ui.pushButtonLB.clicked.connect(self.moveLB)
        self.ui.pushButtonRB.clicked.connect(self.moveRB)
        self.ui.pushButtonCenter.clicked.connect(self.moveC)
        self.ui.pushButtonGetData.clicked.connect(self.onPushButtonGetDataClicked)

    def onPushButtonGetDataClicked(self) -> None:
        screens = QtGui.QGuiApplication.screens()
        screen = screens[0]

        data = f' Количество экранов: {len(screens)}' \
               f'\n Текущее соновное окно: {QtWidgets.QWidget.objectName(self)}' \
               f'\n Разрешение экрана: {screen.size().width()} x {screen.size().height()}' \
               f'\n Имя экрана: {screen.name()}' \
               f'\n Размеры окна: {self.width()} X {self.height()}' \
               f'\n Минимальные размеры окна: {self.minimumWidth()} x {self.minimumHeight()}' \
               f'\n Тущее положение (координаты) окна: {self.x()}, {self.y()}' \
               f'\n Координаты центра приложения: {self.x() + self.width() // 2}, {self.y() + self.height() // 2}' \
               f'\n Состояние окна: {self.whatsThis()}'

        self.ui.plainTextEdit.setPlainText(data)

    def onspinBoxXY(self) -> None:
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def moveLT(self) -> None:
        self.move(0, 0)

    def moveRT(self) -> None:
        screen = QtGui.QGuiApplication.screens()[0]
        self.move(screen.size().width() - self.width(), 0)

    def moveLB(self) -> None:
        screen = QtGui.QGuiApplication.screens()[0]
        self.move(0, screen.size().height() - self.height())

    def moveRB(self) -> None:
        screen = QtGui.QGuiApplication.screens()[0]
        self.move(screen.size().width() - self.width(), screen.size().height() - self.height())

    def moveC(self) -> None:
        screen = QtGui.QGuiApplication.screens()[0]
        center_x = (screen.size().width() - self.width()) // 2
        center_y = (screen.size().height() - self.height()) // 2
        self.move(center_x, center_y)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Событие изменения положения окна

        :param event: QtGui.QMoveEvent
        :return: None
        """
        print(f'Старая позиция: {event.oldPos().x()}, {event.oldPos().y()} ', ctime())
        print(f'Новая позиция:  {event.pos().x()}, {event.pos().y()} ', ctime())

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        """
        Событие изменения размеров окна
        """
        # print(type(event))
        print(f'Новый размер: {event.size().width()} X {event.size().height()} ', ctime())



if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
