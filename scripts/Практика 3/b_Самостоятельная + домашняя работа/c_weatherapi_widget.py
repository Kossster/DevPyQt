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
        self.initSignals()

    def initSignals(self):
        self.ui.pushButton_start.clicked.connect(self.latitudeCheck)
        self.ui.pushButton_start.clicked.connect(self.longitudeCheck)
        self.ui.pushButton_start.clicked.connect(self.startThreads)
        self.ui.pushButton_finish.clicked.connect(self.stopThreads)

    def latitudeCheck(self):
        received_latitude = self.ui.lineEdit_latitude.text()
        try:
            latitude = float(received_latitude)
            if not -180 <= latitude <= 180:
                self.ui.lineEdit_latitude.clear()
                self.ui.lineEdit_latitude.setPlaceholderText("Должно быть вида **.**")
                self.ui.label_5_status.setText("Вы ввели некорректное значение широты")
            else:
                self.ui.label_5_status.clear()
                print("Широта введена корректно")
                self.true_latitude = latitude
        except ValueError:
            print("Широта введена НЕ корректно")
            self.ui.lineEdit_latitude.clear()
            self.ui.lineEdit_latitude.setPlaceholderText("Должно быть вида **.**")
            self.ui.label_5_status.setText("Вы ввели некорректное значение широты")

    def longitudeCheck(self):
        received_longitude = self.ui.lineEdit_longitude.text()
        try:
            longitude = float(received_longitude)
            if not -180 <= longitude <= 180:
                self.ui.lineEdit_longitude.clear()
                self.ui.lineEdit_longitude.setPlaceholderText("Должно быть вида **.**")
                self.ui.label_5_status.setText("Вы ввели некорректное значение долготы")
            else:
                self.ui.label_5_status.clear()
                print("Долгота введена корректно")
                self.true_longitude = longitude
        except ValueError:
            self.ui.lineEdit_longitude.clear()
            print("Долгота введена НЕ корректно")
            self.ui.lineEdit_longitude.setPlaceholderText("Должно быть вида **.**")
            self.ui.label_5_status.setText("Вы ввели некорректное значение долготы")

    def startThreads(self):
        self.WeatherHandlerInform = WeatherHandler(self.true_latitude, self.true_longitude)
        self.WeatherHandlerInform.setDelay(self.ui.spinBox_delay.value())
        self.WeatherHandlerInform.start()
        self.WeatherHandlerInform.WeatherInfo.connect(self.show_weather)
        self.show_weather()

    def stopThreads(self):
        self.WeatherHandlerInform.quit()
        self.WeatherHandlerInform.setStatus(False)
        self.ui.label_5_status.setText("Поток остановлен")

    def show_weather(self, weather_data):
        latitude = weather_data['latitude']
        longitude = weather_data['longitude']
        currentTime = weather_data['current_weather']['time']
        temperature = weather_data['current_weather']['temperature']
        winddirection = weather_data['current_weather']['winddirection']
        windspeed = weather_data['current_weather']['windspeed']
        self.ui.plainTextEdit_Inform.appendPlainText(f"Широта: {latitude}, Долгота: {longitude}")
        self.ui.plainTextEdit_Inform.appendPlainText(f"Время: {currentTime}")
        self.ui.plainTextEdit_Inform.appendPlainText(f"Температура: {temperature}°C")
        self.ui.plainTextEdit_Inform.appendPlainText(f"Направление ветра: {winddirection}")
        self.ui.plainTextEdit_Inform.appendPlainText(f"Скорость ветра: {windspeed} м/c")



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = WindowWeather()
    window.show()

    app.exec()
