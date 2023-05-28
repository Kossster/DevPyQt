"""
Реализовать окно, которое будет объединять в себе сразу два предыдущих виджета
"""
from PySide6 import QtWidgets
from c_weatherapi_widget import WindowWeather
from b_systeminfo_widget import WindowInfo


class Window(QtWidgets.QMainWindow):  # наследуемся от того же класса, что и форма в QtDesigner
    def __init__(self, parent=None):
        super().__init__(parent)
        self.centralwidget = QtWidgets.QWidget(self)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.app1 = WindowWeather()
        self.app2 = WindowInfo()
        self.horizontalLayout.addWidget(self.app1)
        self.horizontalLayout.addWidget(self.app2)
        self.setCentralWidget(self.centralwidget)


if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
