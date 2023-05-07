"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()
    def initUi(self):
        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()
        self.pushButtonMirror = QtWidgets.QPushButton("РАзверни")

        # Создаем слои
        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QVBoxLayout()

        # lineEdit добавляем в горизонтальный слой
        layout1.addWidget(self.lineEditInput)
        layout1.addWidget(self.lineEditMirror)

        # Виджеты(lineEdit и pushButton) добавляем в общий вертикальный слой
        layout2.addLayout(layout1)
        layout2.addWidget(self.pushButtonMirror)

        # Отображаем все в главном окне
        self.setLayout(layout2)
    def initSignals(self):
if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
