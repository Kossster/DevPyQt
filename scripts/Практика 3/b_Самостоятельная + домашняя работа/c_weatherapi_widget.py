"""
Реализовать виджет, который будет работать с потоком WeatherHandler из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода широты и долготы (после запуска потока они должны блокироваться)
2. поле для ввода времени задержки (после запуска потока оно должно блокироваться)
3. поле для вывода информации о погоде в указанных координатах
4. поток необходимо запускать и останавливать при нажатии на кнопку
"""

from PySide6 import QtWidgets
from a_threads import WeatherHandler
from ui.ui_form_weather_info import Ui_MainWindow


class WindowWeather(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_latitude.setPlaceholderText("Пример: 59.57")
        self.ui.lineEdit_longitude.setPlaceholderText("Пример: 30.19")
        self.DataCheck()
        self.initThreads()
        self.initSignals()

    def DataCheck(self):
        # if not isinstance(self.ui.lineEdit_longitude.text(), float):
        #     self.ui.label_5_status.setText("Вы ввели некорректное значение долготы")
        #     raise TypeError()
        # if not isinstance(self.ui.lineEdit_latitude.text(), float):
        #     self.ui.label_5_status.setText("Вы ввели некорректное значение широты")
        #     raise TypeError()
        # else:
        self.lat = self.ui.lineEdit_latitude.text()
        self.lon = self.ui.lineEdit_longitude.text()

    def initThreads(self):
        self.WeatherInfo = WeatherHandler(self.lat, self.lon)

    def initSignals(self):
        self.ui.pushButton_start.clicked.connect(self.startThread)

        self.ui.pushButton_finish.clicked.connect(self.stopThread)

    def startThread(self):
        self.WeatherInfo.start()
        self.ui.pushButton_finish.setEnabled(False)
    def stopThread(self):
        self.WeatherInfo._WeatherHandler__status = None
        self.ui.pushButton_start.setEnabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = WindowWeather()
    window.show()

    app.exec()
