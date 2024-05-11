"""
Создание простого окна в ООП стиле
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):  # Наследование от QWidget - пустое окно
    def __init__(self, parent=None) -> None:  # Создание конструктора класса
        super().__init__(parent)  # Вызов конструктора родительского класса (QWidget)
        # для инициализации всех его методов и атрибутов

        #self.show()  метод 'show' можно вызвать прямо внутри класса но лучше так не делать


if __name__ == "__main__":
    app = QtWidgets.QApplication()  # Создание объекта приложения

    window = Window()  # Создание объекта окна
    window.show()  # Показ окна

    app.exec()  # Запуск бесконечного цикла приложения (событий)
