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

from c_signals_events_form import Ui_Form

for screen in QtGui.QGuiApplication.screens():
    print(screen.geometry(), screen.size())

main_screen = QtGui.QGuiApplication.screens()[0]
print(main_screen.geometry().height())


class Window(QtWidgets.QWidget):



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


    def onspinBoxXY(self) -> None:
        self.move(self.ui.spinBoxX.value(), self.ui.spinBoxY.value())

    def moveLT(self) -> None:
        self.move(0,0)




    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        """
        Событие изменения положения окна

        :param event: QtGui.QMoveEvent
        :return: None
        """

        print(event.oldPos())
        print(event.pos())
        print(event.type())
        for screen in QtGui.QGuiApplication.screens():
            print(screen.geometry(), screen.size())

        print(self.maximumSize())
        print(self.width(), self.height())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()



    app.exec()
