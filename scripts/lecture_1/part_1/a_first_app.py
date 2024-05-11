import sys

from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)    # Создаём объект 'app' в единственном числе
app.exec()                      # Запуск бесконечного цикла событий

print("Приложение закрыто!")
