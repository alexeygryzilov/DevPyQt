"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатие на кнопку
"""
import time
import requests
from PySide6 import QtWidgets, QtCore
from form_weather import Ui_FormWeather
from a_threads import WeatherHandler


class WindowWeather(QtWidgets.QWidget):
    lat = 36.826903
    lon = 10.173742

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui_s = Ui_FormWeather()
        self.ui_s.setupUi(self)
        self.initThreads()
        self.ui_s.radioButton3.setChecked(True)
        self.ui_s.radioButton3.clicked.connect(self.updateDelay)
        self.ui_s.radioButton5.clicked.connect(self.updateDelay)
        self.ui_s.radioButton10.clicked.connect(self.updateDelay)

        self.ui_s.pushButtonGetData.clicked.connect(self.getData)
        self.ui_s.pushButtonStopGetData.clicked.connect(self.stopGetData)

        self.ui_s.lineEditLatitude.setText("36.826903")
        self.ui_s.lineEditLongitude.setText("10.173742")

        self.ui_s.lineEditLatitude.textChanged.connect(self.validateLatitude)
        self.ui_s.lineEditLongitude.textChanged.connect(self.validateLongitude)

        self.ui_s.lineEditLatitude.textChanged.connect(self.stopGetData2)
        self.ui_s.lineEditLongitude.textChanged.connect(self.stopGetData2)

        self.initSignals()

    def updateDelay(self):
        if self.ui_s.radioButton3.isChecked():
            self.WeatherHandler.setDelay(3)
        elif self.ui_s.radioButton5.isChecked():
            self.WeatherHandler.setDelay(5)
        elif self.ui_s.radioButton10.isChecked():
            self.WeatherHandler.setDelay(10)

    def getData(self):
        if not self.validateLatitude() or not self.validateLongitude():
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверные координаты")
            return

        WindowWeather.lat = float(self.ui_s.lineEditLatitude.text())
        WindowWeather.lon = float(self.ui_s.lineEditLongitude.text())
        self.weather_info = WeatherHandler(WindowWeather.lat, WindowWeather.lon)
        self.weather_info.setStatus(True)
        self.weather_info.weatherInfoReceived.connect(self.upgradeWeatherInfo)
        self.weather_info.started.connect(lambda: print("Старт потока"))
        self.weather_info.finished.connect(lambda: print("Конец потока"))

        self.ui_s.textEditData.clear()
        self.ui_s.pushButtonGetData.setEnabled(False)
        self.ui_s.pushButtonStopGetData.setEnabled(True)
        self.weather_info.start()

    def stopGetData(self):
        self.weather_info.setStatus(None)
        self.ui_s.pushButtonStopGetData.setEnabled(False)
        self.ui_s.pushButtonGetData.setEnabled(True)

    def stopGetData2(self):
        self.ui_s.textEditData.setText('<font color="red">Координаты изменены</font>')
        self.weather_info.setStatus(None)
        self.ui_s.pushButtonStopGetData.setEnabled(False)
        self.ui_s.pushButtonGetData.setEnabled(True)

    def upgradeWeatherInfo(self, weather_data):
        latitude = weather_data['latitude']
        longitude = weather_data['longitude']
        currentTime = weather_data['current_weather']['time']
        temperature = weather_data['current_weather']['temperature']
        winddirection = weather_data['current_weather']['winddirection']
        windspeed = weather_data['current_weather']['windspeed']
        self.ui_s.textEditData.append(f"Широта: {latitude}, Долгота: {longitude}")
        self.ui_s.textEditData.append(f"Время: {currentTime}")
        self.ui_s.textEditData.append(f"Температура: {temperature}°C")
        self.ui_s.textEditData.append(f"Направление ветра: {winddirection}")
        self.ui_s.textEditData.append(f"Скорость ветра: {windspeed} м/c")

    def initThreads(self):
        self.weather_info = WeatherHandler(WindowWeather.lat, WindowWeather.lon)
        self.weather_info.weatherInfoReceived.connect(self.upgradeWeatherInfo)
        self.weather_info.start()

    def initSignals(self):
        self.weather_info.started.connect(self.startThread)
        self.weather_info.finished.connect(self.finishThread)

    def startThread(self):
        self.ui_s.lineEditLatitude.setEnabled(False)
        self.ui_s.lineEditLongitude.setEnabled(False)
        self.ui_s.radioButton3.setEnabled(False)
        self.ui_s.radioButton5.setEnabled(False)
        self.ui_s.radioButton10.setEnabled(False)

    def finishThread(self):
        self.ui_s.lineEditLatitude.setEnabled(True)
        self.ui_s.lineEditLongitude.setEnabled(True)
        self.ui_s.radioButton3.setEnabled(True)
        self.ui_s.radioButton5.setEnabled(True)
        self.ui_s.radioButton10.setEnabled(True)

    def validateLatitude(self):
        latitude_text = self.ui_s.lineEditLatitude.text()
        try:
            latitude = float(latitude_text)
            if -180 <= latitude <= 180:
                self.ui_s.lineEditLatitude.setStyleSheet("")
                return latitude
            else:
                self.ui_s.lineEditLatitude.setStyleSheet("background-color: red;")
                self.ui_s.textEditData.setText('<font color="red">Введите корректные координаты</font>')
                self.stopGetData()

        except ValueError:
            self.ui_s.lineEditLatitude.setStyleSheet("background-color: red;")
            self.ui_s.textEditData.setText('<font color="red">Введите корректные координаты</font>')
            self.stopGetData()

    def validateLongitude(self):
        longitude_text = self.ui_s.lineEditLongitude.text()
        try:
            longitude = float(longitude_text)
            if -180 <= longitude <= 180:
                self.ui_s.lineEditLongitude.setStyleSheet("")
                return longitude
            else:
                self.ui_s.lineEditLongitude.setStyleSheet("background-color: red;")
                self.ui_s.textEditData.setText('<font color="red">Введите корректные координаты</font>')
        except ValueError:
            self.ui_s.lineEditLongitude.setStyleSheet("background-color: red;")
            self.ui_s.textEditData.setText('<font color="red">Введите корректные координаты</font>')


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = WindowWeather()
    window.show()

    app.exec()
