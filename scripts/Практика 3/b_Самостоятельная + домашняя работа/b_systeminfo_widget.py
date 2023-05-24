"""
Реализовать виджет, который будет работать с потоком SystemInfo из модуля a_threads

Создавать форму можно как в ручную, так и с помощью программы Designer

Форма должна содержать:
1. поле для ввода времени задержки
2. поле для вывода информации о загрузке CPU
3. поле для вывода информации о загрузке RAM
4. поток необходимо запускать сразу при старте приложения
5. установку времени задержки сделать "горячей", т.е. поток должен сразу
реагировать на изменение времени задержки
"""
from PySide6 import QtWidgets, QtCore, QtGui
from a_threads import SystemInfo
from ui.ui_form_sys_info import Ui_MainWindow


class WindowInfo(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initThreads()
        self.initSignals()

    def initThreads(self) -> None:
        self.systemInfo = SystemInfo()
        self.systemInfo.start()

    def initSignals(self):
        self.systemInfo.systemInfoReceived.connect(self.reportCPU)
        # self.ui.pushButton.clicked.connect(self.setDelay)

    def reportCPU(self, list_info):
        if self.ui.spinBox.value() == 0: # TODO при 0 программа тормозит
            self.systemInfo.delay = 1
        else:
            self.systemInfo.delay = self.ui.spinBox.value()
        self.ui.label_3.setText(f"{list_info[0]}%")
        self.ui.label_5.setText(f"{list_info[1]}%")

    # def setDelay(self):
    #     self.systemInfo.delay = self.ui.spinBox.value()



if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = WindowInfo()
    window.show()

    app.exec()
