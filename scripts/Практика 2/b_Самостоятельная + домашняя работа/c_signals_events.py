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

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()

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

        self.layoutMain = QtWidgets.QHBoxLayout()
        self.layoutMain.addWidget(groupBoxMovWin)
        self.layoutMain.addLayout(self.Layout_1)

        self.setLayout(self.layoutMain)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
