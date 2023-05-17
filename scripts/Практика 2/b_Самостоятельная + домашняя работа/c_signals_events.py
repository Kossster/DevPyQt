"""
Реализация программу проверки состояния окна:
Форма для приложения (ui/c_signals_events.ui)

Программа должна обладать следующим функционалом:

1. Возможность перемещения окна по заданным координатам.
2. Возможность получения параметров экрана (вывод производить в plainTextEdit + добавлять время).
    * Кол-во экранов
    * Текущее основное окно
    * Разрешение экрана
    * На каком экране окно находится
    * Размеры окна
    * Минимальные размеры окна
    * Текущее положение (координаты) окна
    * Координаты центра приложения
    * Отслеживание состояния окна (свернуто/развёрнуто/активно/отображено)
3. Возможность отслеживания состояния окна (вывод производить в консоль + добавлять время).
    * При перемещении окна выводить его старую и новую позицию
    * При изменении размера окна выводить его новый размер
"""

from PySide6 import QtWidgets, QtGui, QtCore
import time


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()

    def initUi(self) -> None:
        # Создаю groupBox
        groupBoxMovWin = QtWidgets.QGroupBox("Перемещение окна:")
        groupBoxMoveCoor = QtWidgets.QGroupBox("Переместить в координаты:")
        groupBoxLog = QtWidgets.QGroupBox("Лог")

        # Создаем Lable
        self.LableX = QtWidgets.QLabel("X")
        self.LableY = QtWidgets.QLabel("Y")

        # Создаем pushButton
        self.pushButtonLeftUp = QtWidgets.QPushButton("Лево/Верх")
        self.pushButtonLeftDown = QtWidgets.QPushButton("Лево/Низ")
        self.pushButtonRightUp = QtWidgets.QPushButton("Право/Верх")
        self.pushButtonRightDown = QtWidgets.QPushButton("Право/Низ")
        self.pushButtonCenter = QtWidgets.QPushButton("Центр")
        self.pushButtonMoveCoor = QtWidgets.QPushButton("Переместить")
        self.pushButtonLog = QtWidgets.QPushButton("Получить данные окна")
        self.pushButtonClean = QtWidgets.QPushButton("Отчистить лог")

        # Создаем SpinBox
        self.SpinBoxX = QtWidgets.QSpinBox()
        self.SpinBoxY = QtWidgets.QSpinBox()

        # Создаем plainTextEdit
        self.plainTextEditLog = QtWidgets.QPlainTextEdit()

        # Создаем layout
        self.LeftLayout = QtWidgets.QVBoxLayout()
        self.layoutLeftUpRightUp = QtWidgets.QHBoxLayout()
        self.layoutLeftUpRightUp.addWidget(self.pushButtonLeftUp)
        self.layoutLeftUpRightUp.addWidget(self.pushButtonRightUp)
        self.LeftLayout.addLayout(self.layoutLeftUpRightUp)

        self.LeftLayout.addWidget(self.pushButtonCenter)

        self.layoutLeftDownRightDown = QtWidgets.QHBoxLayout()
        self.layoutLeftDownRightDown.addWidget(self.pushButtonLeftDown)
        self.layoutLeftDownRightDown.addWidget(self.pushButtonRightDown)
        self.LeftLayout.addLayout(self.layoutLeftDownRightDown)

        self.layoutCoor = QtWidgets.QHBoxLayout()
        self.layoutCoor.addWidget(self.LableX)
        self.layoutCoor.addWidget(self.SpinBoxX)
        self.layoutCoor.addWidget(self.LableY)
        self.layoutCoor.addWidget(self.SpinBoxY)
        groupBoxMoveCoor.setLayout(self.layoutCoor)
        self.LeftLayout.addWidget(groupBoxMoveCoor)

        self.LeftLayout.addWidget(self.pushButtonMoveCoor)
        groupBoxMovWin.setLayout(self.LeftLayout)

        self.LayoutPTE = QtWidgets.QVBoxLayout()
        self.LayoutPTE.addWidget(self.plainTextEditLog)
        groupBoxLog.setLayout(self.LayoutPTE)

        self.Layout_1 = QtWidgets.QVBoxLayout()
        self.Layout_1.addWidget(groupBoxLog)
        self.Layout_1.addWidget(self.pushButtonLog)
        self.Layout_1.addWidget(self.pushButtonClean)

        self.layoutMain = QtWidgets.QHBoxLayout()
        self.layoutMain.addWidget(groupBoxMovWin)
        self.layoutMain.addLayout(self.Layout_1)

        self.setLayout(self.layoutMain)

    def initSignals(self) -> None:
        self.pushButtonClean.clicked.connect(self.ClearLog)
        self.pushButtonLog.clicked.connect(self.getScreenInfo)  # цепляем сигнал к кнопке
        self.pushButtonLeftUp.clicked.connect(self.editPosition)
        self.pushButtonLeftDown.clicked.connect(self.editPosition)
        self.pushButtonRightUp.clicked.connect(self.editPosition)
        self.pushButtonRightDown.clicked.connect(self.editPosition)
        self.pushButtonCenter.clicked.connect(self.editPosition)
        self.pushButtonMoveCoor.clicked.connect(self.MoveCoordinates)

    def getScreenInfo(self):
        screens_count = QtWidgets.QApplication.screens()  # создаем переменную с инфой по нашим экранам
        log = self.plainTextEditLog.appendPlainText  # создаем переменную с методом добавления текста в наш plainTextEditLog

        log(time.ctime())  # добавляем в наше plainTextEditLog актуальное время

        log(f"Кол-во экранов:           {len(screens_count)}")  # добавляем инфу о кол-ве экранов
        log(f"Текущее основное окно     {QtWidgets.QApplication.primaryScreen().name()}")
        for screen in screens_count:
            log(f"Разрешение экрана:    {screen.size().width()}x{screen.size().height()}")
        log(f"Окно находится на экране  {QtWidgets.QApplication.screenAt(self.pos()).name()}")
        log(f"Размеры окна:             Ширина {self.size().width()} Высота {self.size().height()}")
        log(f"Минимальные размеры окна: Ширина {self.minimumWidth()} Высота {self.minimumHeight()}")
        log(f"Текущее положение окна X:  {self.pos().x()}    Y:  {self.pos().y()}")
        log(f"Центр приложения:         x = {self.pos().x() + self.width() / 2} y = {self.pos().y() + self.height() / 2}")

    def ClearLog(self):
        self.plainTextEditLog.clear()

    def editPosition(self):
        print(self.sender())
        buttonText = self.sender().text()  # создаем переменную с именем кнопки на которую мы нажали
        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()  # ширина нашего экрана
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()  # высота нашего экрана

        position = {"Лево/Верх":(0, 0),
                    "Лево/Низ": (0, screenHeight-self.height()-70),
                    "Центр": (screenWidth/2 - self.width()/2, screenHeight/2 - self.height()/2),
                    "Право/Верх": (screenWidth - self.width(), 0),
                    "Право/Низ": (screenWidth - self.width(), screenHeight-self.height()-70)}

        self.move(position.get(buttonText)[0], position.get(buttonText)[1])

    def changeEvent(self, event: QtCore.QEvent) -> None:
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                self.plainTextEditLog.appendPlainText(time.ctime() + ": окно свернуто")
            elif self.isMaximized():
                self.plainTextEditLog.appendPlainText(time.ctime() + ": окно развернуто")
        if event.type() == QtCore.QEvent.ActivationChange:
            self.plainTextEditLog.appendPlainText(time.ctime() + ": окно активно")

        QtWidgets.QWidget.changeEvent(self, event)

    def showEvent(self, event: QtGui.QShowEvent) -> None:
        self.plainTextEditLog.appendPlainText(time.ctime() + ": window is show")

        QtWidgets.QWidget.showEvent(self, event)

    def hideEvent(self, event: QtGui.QHideEvent) -> None:
        self.plainTextEditLog.appendPlainText(time.ctime() + ": window is hide")
        QtWidgets.QWidget.hideEvent(self, event)

    def moveEvent(self, event: QtGui.QMoveEvent) -> None:
        print(f"moveEvent:   x = {event.pos().x()}, y = {event.pos().y()}")
        QtWidgets.QWidget.moveEvent(self, event)

    def resizeEvent(self, event: QtGui.QResizeEvent) -> None:
        print(f"resizeEvent: w = {event.size().width()}, h = {event.size().height()}")
        QtWidgets.QWidget.resizeEvent(self, event)

    def MoveCoordinates(self):
        x_val = self.SpinBoxX.value()
        y_val = self.SpinBoxY.value()

        self.move(x_val, y_val)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, "Закрыть окно",
                                                     "Вы хотите закрыть окно?",
                                                     QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                     QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
