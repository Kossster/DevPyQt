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


class Window(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initThreads()
        self.reportCPU()
    def initThreads(self) -> None:
        self.thread = QtCore.QThread()
        self.systemInfo = SystemInfo()
        self.systemInfo.moveToThread(self.thread)
        self.thread.start()

    def reportCPU(self):
        self.ui.label_3.setText(f"{SystemInfo.systemSignal}")








if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
