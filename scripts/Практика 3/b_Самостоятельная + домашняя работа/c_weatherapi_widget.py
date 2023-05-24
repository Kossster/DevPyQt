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
import re


class WindowWeather(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit_latitude.setPlaceholderText("Пример: 59.57")
        self.ui.lineEdit_longitude.setPlaceholderText("Пример: 30.19")
        self.test()
        self.lat = True
        self.lon = True
        self.initSignals()
        self.ui.pushButton_finish.setEnabled(False)

    def DataCheck(self):
        pattern = r"\d+\.\d+"
        if not re.fullmatch(pattern, self.ui.lineEdit_latitude.text()):
            self.ui.lineEdit_latitude.clear()
            self.ui.lineEdit_latitude.setPlaceholderText("Должно быть вида **.**")
            self.ui.label_5_status.setText("Вы ввели некорректное значение")

        if not re.fullmatch(pattern, self.ui.lineEdit_longitude.text()):
            self.ui.lineEdit_longitude.clear()
            self.ui.lineEdit_longitude.setPlaceholderText("Должно быть вида **.**")
            self.ui.label_5_status.setText("Вы ввели некорректное значение")
        else:
            self.lat = self.ui.lineEdit_latitude.text()
            self.lon = self.ui.lineEdit_longitude.text()
            self.ui.label_5_status.clear()

    def initThreads(self):
        self.weatherInfo = WeatherHandler(self.lat, self.lon)
        self.weatherInfo.WeatherInfo.connect(self.passInform)

    def initSignals(self):
        self.ui.pushButton_start.clicked.connect(self.startThread)
        self.ui.pushButton_finish.clicked.connect(self.stopThread)


    def startThread(self):
        self.DataCheck()
        self.initThreads()
        self.weatherInfo.start()
        self.passDelay()
        self.passInform()
        self.ui.pushButton_finish.setEnabled(True)

    def passDelay(self):
        self.weatherInfo.setDelay(self.ui.spinBox_delay.value())

    def passInform(self):
        self.ui.plainTextEdit_Inform.appendPlainText(f"{self.weatherInfo.WeatherInfo}")

    def stopThread(self):
        self.weatherInfo.quit()
        self.ui.plainTextEdit_Inform.clear()
        self.ui.pushButton_finish.setEnabled(False)

    def test(self):
        self.ui.lineEdit_latitude.setText("59.57")
        self.ui.lineEdit_longitude.setText("30.19")


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = WindowWeather()
    window.show()

    app.exec()
