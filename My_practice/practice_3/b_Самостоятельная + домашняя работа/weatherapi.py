import time
import requests
import psutil
from PySide6 import QtCore


class WeatherHandler(QtCore.QThread):
    # TODO Пропишите сигналы, которые считаете нужными
    data_responsed = QtCore.Signal(object)

    def __init__(self, lat, lon, parent=None):
        super().__init__(parent)

        self.__api_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        self.__delay = 10
        self.__status = None

    def setDelay(self, delay) -> None:
        """
        Метод для установки времени задержки обновления сайта

        :param delay: время задержки обновления информации о доступности сайта
        :return: None
        """

        self.__delay = delay

    def run(self) -> None:
        # TODO настройте метод для корректной работы
        pass

        while self.__status:
            # TODO Примерный код ниже

            response = requests.get(self.__api_url)
            data = response.json()
            self.data_responsed.emit(data)
            self.sleep(self.__delay)

