"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

from PySide6 import QtWidgets, QtCore
import requests

class CheckSiteTread(QtCore.QThread):

    started_signals = QtCore.Signal()
    finished_signals = QtCore.Signal()
    status_code_signal = QtCore.Signal(int)

    def __init__(self, parent=None, url=""):
        super().__init__(parent)
        self.url = url

    def run(self):
        self.started_signals.emit()
        try:
            response = requests.get(self.url)
            status_code = response.status_code
        except requests.exceptions.RequestException:
            status_code = None

        self.status_code_signal.emit(status_code)
        self.finished_signals.emit()


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.urlLineEdit = QtWidgets.QLineEdit()
        self.checkButton = QtWidgets.QPushButton("Проверить")
        self.statusLabel = QtWidgets.QLabel()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(QtWidgets.QLabel("URL"))
        layout.addWidget(self.urlLineEdit)
        layout.addWidget(self.checkButton)
        layout.addWidget(self.statusLabel)

        self.setLayout(layout)

        self.threadSite = CheckSiteTread()
        self.threadSite.started_signals.connect(self.onTreadStart)
        self.threadSite.finished_signals.connect(self.onTreadFinished)
        self.threadSite.status_code_signal.connect(self.onTreadStatus)

        self.checkButton.clicked.connect(self.onClick)

    def onTreadStart(self):
        self.checkButton.setEnabled(False)
        self.statusLabel.setText("Начали расчет")

    def onTreadFinished(self):
        self.checkButton.setEnabled(True)
        # self.statusLabel.setText("Закончили расчет")

    def onTreadStatus(self, value):
        if value is None:
            self.statusLabel.setText("Сайт недоступен")
        elif value == 200:
            self.statusLabel.setText("Сайт доступен")
        else:
            self.statusLabel.setText(f"Что то не так код:{value}")

    def onClick(self):
        url = self.urlLineEdit.text()
        self.threadSite.url = url
        self.threadSite.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
